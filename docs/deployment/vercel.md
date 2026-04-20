# Deploying to Vercel

## Prerequisites

- Stateless app (no SSE, WebSockets, background workers, in-memory state)
- `use_cdn=True` in `add_bootstrap()` (required for Faststrap-managed assets on serverless)
- Python 3.10+

## Project Structure

```text
my-app/
|-- assets/
|   `-- custom.css
|-- main.py
|-- requirements.txt
|-- .vercelignore
`-- vercel.json
```

## Step 1 - Configure main.py

```python
import os
from pathlib import Path

from fasthtml.common import FastHTML, Link
from faststrap import add_bootstrap, mount_assets, Card, Button, Input

app = FastHTML()
add_bootstrap(app, use_cdn=True, include_favicon=False)

# Mount local assets for local development only.
# On Vercel, vercel.json serves assets/** statically.
if not os.getenv("VERCEL"):
    mount_assets(app, str(Path(__file__).parent / "assets"), url_path="/assets")

app.hdrs = app.hdrs + [
    Link(rel="stylesheet", href="/assets/custom.css?v=1"),
]

@app.route("/")
def home():
    return Card(
        Input("email", input_type="email", label="Email", required=True),
        Button("Sign In", variant="primary", cls="w-100", hx_post="/login"),
        header="Welcome back",
    )

# Correct: expose bare app object
# Wrong: do not call serve() in serverless entrypoint
```

## Step 2 - requirements.txt

```text
python-fasthtml
faststrap
```

## Step 3 - vercel.json

```json
{
  "$schema": "https://openapi.vercel.sh/vercel.json",
  "builds": [
    { "src": "assets/**", "use": "@vercel/static" },
    { "src": "main.py", "use": "@vercel/python" }
  ],
  "rewrites": [
    { "source": "/(.*)", "destination": "/main.py" }
  ]
}
```

Use `rewrites`, not a catch-all `routes` rule, when your app also serves project assets such as `/assets/custom.css`.

## Step 4 - .vercelignore

```text
.git
.venv
.pytest_cache
pytest-cache-files-*
__pycache__
*.pyc
*.pyo
*.pyd
```

## Step 5 - Deploy

```bash
npm i -g vercel
vercel
```

Set env vars as needed, for example: `vercel env add DATABASE_URL`.

## Connecting to an External Backend

```python
Button(
    "Save",
    hx_post="https://api.yourapp.com/save",
    hx_target="#result",
)
```

Backend CORS must expose HTMX headers:

```python
expose_headers=[
    "HX-Location", "HX-Redirect", "HX-Refresh",
    "HX-Trigger", "HX-Reswap", "HX-Retarget",
]
```

Without `expose_headers`, preset response helpers such as `toast_response()` and `hx_redirect()` fail cross-origin.

For `htmx` requests from a Faststrap app on Vercel to a separate FastAPI backend:

- keep the Faststrap app fully stateless
- allow CORS from your Vercel frontend origin
- expose HTMX response headers from the backend
- avoid relying on in-memory process state between requests

This architecture works well for forms, filtering, CRUD flows, and partial-page updates.

## What Does Not Work on Vercel

- SSE (Server-Sent Events)
- WebSockets
- Background workers
- In-memory state between requests
- Filesystem writes

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| 404 on Bootstrap CSS/JS or icons | `use_cdn=True` not set | Add `use_cdn=True` to `add_bootstrap()` |
| 404 on `/assets/custom.css` or local images | Catch-all routing is intercepting static files | Serve `assets/**` with `@vercel/static` and use `rewrites` instead of catch-all `routes` |
| App works locally, 500 on Vercel | `serve()` called in main.py | Remove `serve()` call |
| HTMX response helpers not working cross-origin | Missing `expose_headers` | Add all `HX-*` headers to backend CORS `expose_headers` |
| Cold start delay | Serverless cold starts | Expected; reduced on paid plans |

## Key Point

`use_cdn=True` only covers Faststrap-managed assets such as Bootstrap CSS/JS, Bootstrap Icons, and Faststrap CSS. It does not automatically publish your app's own CSS, images, or other project files. Those must still be served explicitly by your deployment setup.
