# Building Custom Components

Faststrap components are plain Python functions that return FastHTML elements. You do not need a class hierarchy to extend the framework.

## Minimal Component

```python
from typing import Any

from fasthtml.common import Div


def ProductCard(*children: Any, **kwargs: Any) -> Div:
    return Div(*children, cls="product-card", **kwargs)
```

That works, but it does not yet follow the full Faststrap conventions.

## Recommended Component Pattern

Use `@register`, `resolve_defaults`, `UNSET`, `merge_classes`, and `convert_attrs` when the component should behave like a first-class Faststrap component.

```python
from typing import Any

from fasthtml.common import Div, H3, P
from faststrap import UNSET, merge_classes, register, resolve_defaults
from faststrap.utils.attrs import convert_attrs


@register(category="display")
def ProductCard(
    title: str,
    description: str,
    *,
    variant: str | None = UNSET,
    elevated: bool | None = UNSET,
    **kwargs: Any,
) -> Div:
    cfg = resolve_defaults(
        "ProductCard",
        variant=variant,
        elevated=elevated,
    )

    classes = ["product-card"]
    if cfg.get("variant"):
        classes.append(f"border-{cfg['variant']}")
    if cfg.get("elevated"):
        classes.append("shadow-sm")

    attrs = convert_attrs(kwargs)
    return Div(
        H3(title),
        P(description),
        cls=merge_classes(*classes, attrs.pop("cls", "")),
        **attrs,
    )
```

## Why Each Helper Matters

| Helper | Why it matters |
| --- | --- |
| `@register` | Makes the component discoverable through the registry. |
| `UNSET` | Preserves the difference between omitted values and explicit `None`. |
| `resolve_defaults` | Applies global defaults set with `set_component_defaults()`. |
| `merge_classes` | Composes Bootstrap, Faststrap, and user classes safely. |
| `convert_attrs` | Converts Python-friendly attributes like `hx_get` and `data_bs_toggle`. |

## HTMX Attributes

Always run `convert_attrs()` before passing arbitrary `**kwargs` to FastHTML elements. This is what makes Faststrap-style `hx_*`, `data_bs_*`, and `aria_*` attributes work.

```python
attrs = convert_attrs(kwargs)
return Div("Search", hx_get="/search", **attrs)
```

## Styling With Theme Variants

For custom components that need light and dark styling, pair a stable class with `theme_variant_css()`.

```python
from faststrap import theme_variant_css

ProductCardStyles = theme_variant_css(
    ".product-card",
    light={"background": "#ffffff"},
    dark={"background": "#0f172a", "color": "#e2e8f0"},
)
```

## Checklist

- Use children-first APIs when the component wraps content.
- Use keyword-only parameters for component options.
- Use `UNSET` for parameters that should participate in global defaults.
- Use `convert_attrs()` for pass-through HTML, HTMX, ARIA, and data attributes.
- Add a stable class hook such as `faststrap-product-card`.
- Register public components with the right category and `requires_js` flag.
- Keep JavaScript optional unless the component is explicitly an integration.
