# Architecture And Render Model

Faststrap is a function-first component library for FastHTML. Components are Python functions that return FastHTML elements, which FastHTML serializes into HTML responses.

## Mental Model

```python
Card(
    "Hello",
    header="Greeting",
    cls="shadow-sm",
)
```

Becomes a FastHTML element tree, then HTML similar to:

```html
<div class="card shadow-sm">
  <div class="card-header">Greeting</div>
  <div class="card-body">Hello</div>
</div>
```

## Request Flow

1. Your FastHTML route returns Faststrap components.
2. Faststrap components compose FastHTML elements.
3. FastHTML serializes those elements into HTML.
4. HTMX attributes such as `hx_get` become normal `hx-get` attributes.
5. Bootstrap CSS/JS comes from `add_bootstrap()` or your own asset setup.

## Component Shape

Most components follow this pattern:

```python
Component(*children, option=None, **kwargs)
```

The convention is:

- Positional arguments are usually rendered children.
- Keyword arguments configure component behavior.
- `cls`, `style`, `data_*`, `aria_*`, and `hx_*` are passed through as HTML attributes.

## Attribute Conversion

Faststrap uses `convert_attrs()` so Python-friendly kwargs become HTML attributes:

| Python kwarg | HTML output |
| --- | --- |
| `hx_get="/items"` | `hx-get="/items"` |
| `data_bs_toggle="modal"` | `data-bs-toggle="modal"` |
| `aria_label="Close"` | `aria-label="Close"` |
| `cls="btn"` | `class="btn"` |

If you author custom components, always pass `**kwargs` through `convert_attrs()` before rendering. See [Building Custom Components](custom-components.md).

## Asset Injection

`add_bootstrap(app)` attaches CSS and JavaScript assets to the FastHTML app headers. Depending on your settings, assets can be served locally or from CDN.

```python
from fasthtml.common import FastHTML
from faststrap import add_bootstrap

app = FastHTML()
add_bootstrap(app)
```

Call it during app setup, not inside a request handler.

## Defaults And Theme State

`set_component_defaults()` configures process-global defaults. It is thread-safe, but it should still be treated as startup configuration.

```python
from faststrap import set_component_defaults

set_component_defaults("Button", variant="secondary")
```

Use `None` to clear a global default for one component call. Use `UNSET` when writing wrapper components. See [Component Defaults](../api/defaults.md).

## Registry

The registry stores component metadata such as category and JavaScript requirements. It powers discovery APIs and helps AI agents reuse existing components.

```python
from faststrap import find_components

find_components("toast")
```

See [Component Registry](../api/registry.md).

## Core vs Optional Integrations

Core Faststrap components stay Bootstrap/FastHTML/HTMX-first. Optional integrations such as GSAP, ChartJS, Markdown, and MapView may load extra frontend/runtime assets when explicitly requested.

This keeps the default framework lightweight while still supporting richer applications.
