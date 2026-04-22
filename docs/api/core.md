# API Reference

This section provides automatically generated documentation from the FastStrap source code. It is useful for looking up exact parameter names and types.

## Core Utilities

::: faststrap.core.theme.resolve_defaults
    options:
        show_root_heading: true
        show_source: true

::: faststrap.core.base.merge_classes
    options:
        show_root_heading: true
        show_source: true

## Attributes Helper

Use `convert_attrs()` when authoring custom FastStrap components or wrappers.
It converts Python-friendly kwargs such as `hx_get`, `data_bs_toggle`,
`aria_label`, `style={...}`, and `css_vars={...}` into valid HTML attributes.

```python
from faststrap import convert_attrs

attrs = {"cls": "btn btn-primary"}
attrs.update(
    convert_attrs(
        {
            "hx_post": "/save",
            "hx_target": "#result",
            "data": {"mode": "inline"},
            "css_vars": {"brand_color": "#5B6CFF"},
        }
    )
)
```

For component authors, routing `**kwargs` through `convert_attrs(kwargs)` is the
standard way to preserve HTMX support and attribute conversion consistently.

::: faststrap.utils.attrs.convert_attrs
    options:
        show_root_heading: true
        show_source: true

## Application Setup

::: faststrap.core.assets.add_bootstrap
    options:
        show_root_heading: true
        show_source: true

::: faststrap.utils.static_management.get_faststrap_static_url
    options:
        show_root_heading: true
        show_source: true

## Theme System

Notes:
- `add_bootstrap()` supports `font_family` and `font_weights` for Google Fonts injection.
- `set_component_defaults()` modifies process-global defaults. Configure it at application startup.
- `convert_attrs()` is available from `faststrap` directly for custom components and wrappers.
- `BaseComponent` / `Component` are extension points for third-party class-based components; built-ins remain function-based.
- `BaseComponent.merge_attrs()` applies `convert_attrs()` so class-based components keep the same attribute conversion behavior as function-based components.

### When To Use `BaseComponent`

Use `BaseComponent` only when a class-based API is genuinely helpful, for example:

- stateful third-party component libraries
- reusable abstractions with internal helper methods
- advanced wrappers that benefit from inheritance

For normal FastStrap components, prefer plain function-based components such as
`Button(...)`, `Card(...)`, or `Row(...)`. That remains the default style across
the framework.

::: faststrap.core.theme.create_theme
    options:
        show_root_heading: true
        show_source: true

::: faststrap.core.theme.set_component_defaults
    options:
        show_root_heading: true
        show_source: true

::: faststrap.core.theme.reset_component_defaults
    options:
        show_root_heading: true
        show_source: true
