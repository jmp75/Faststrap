# GlassNavbar

`GlassNavbar` renders a premium frosted-glass Bootstrap navbar. It is useful for landing pages and showcase apps where the nav sits over a gradient, image, or layered background.

## Quick Start

```python
from faststrap import GlassNavbar

GlassNavbar(
    ("Home", "/"),
    ("Features", "/features"),
    ("Pricing", "/pricing"),
    brand="NovaFlow",
    blur_strength="medium",
    transparency=0.82,
    theme="light",
)
```

Tuple items use `(label, href)` or `(label, href, active)`.

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `*items` | `Any` | | Tuple items or custom nav item components. |
| `brand` | `str \| None` | `None` | Brand label. |
| `brand_href` | `str` | `"/"` | Brand link target. |
| `blur_strength` | `"low" \| "medium" \| "high"` | `UNSET` | Backdrop blur amount. |
| `transparency` | `float \| None` | `UNSET` | Background alpha from `0.0` to `1.0`. |
| `theme` | `str \| None` | `UNSET` | `"light"` or `"dark"` styling. |
| `sticky` | `bool \| None` | `UNSET` | Adds `sticky-top`. |
| `expand` | `str \| None` | `UNSET` | Collapse breakpoint such as `lg` or `xl`. |
| `**kwargs` | `Any` | | Extra nav attributes. |

## Notes

- Requires Bootstrap JavaScript for the mobile collapse toggler.
- The generated collapse ID is currently `glassNavbarContent`, so avoid rendering multiple `GlassNavbar` components on the same page.
- The glass effect depends on browser support for `backdrop-filter`.

## API Reference

::: faststrap.components.navigation.glass_navbar.GlassNavbar

::: faststrap.components.navigation.glass_navbar.GlassNavItem
