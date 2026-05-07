# GSAP Motion

GSAP Motion is an optional integration for richer, opinionated animation. Core Faststrap still uses `Fx` for zero-JS effects; use this integration only when a project explicitly wants GSAP.

## Install

```bash
pip install "faststrap[gsap]"
```

The extra is intentionally lightweight. GSAP itself is loaded from CDN by `add_gsap(app)` unless you pass a custom URL.

## App Setup

```python
from fasthtml.common import FastHTML
from faststrap import add_bootstrap, add_gsap

app = FastHTML()
add_bootstrap(app)
add_gsap(app)
```

`add_gsap(app)` is idempotent, so repeated startup wiring will not add duplicate script tags.

## Component Motion

```python
from faststrap import Card, Gsap

Card(
    "Revenue is up 12%",
    header="Today",
    **Gsap.attrs("fade-up", duration=0.5, delay=0.1),
)
```

## Reveal Wrapper

```python
from faststrap import Button, GsapReveal

GsapReveal(
    Button("Save", variant="primary"),
    preset="pop",
)
```

## Presets

- `fade`
- `fade-up`
- `fade-down`
- `slide-left`
- `slide-right`
- `scale`
- `pop`

## Philosophy

- GSAP is never required for core Faststrap components.
- Server-rendered markup remains usable without GSAP.
- The runtime respects `prefers-reduced-motion`.
- Use GSAP for premium motion, guided flows, and showcase-level polish, not basic layout behavior.
