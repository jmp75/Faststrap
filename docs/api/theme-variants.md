# Theme Variant CSS

`theme_variant_css()` creates light/dark CSS blocks that follow Faststrap's `data-bs-theme` convention.

Use it when custom app styling should stay aligned with Bootstrap and Faststrap theme switching without hand-writing duplicate selectors everywhere.

## Quick Start

```python
from faststrap import theme_variant_css

theme_variant_css(
    ".premium-card",
    light={
        "background": "rgba(255, 255, 255, .86)",
        "border": "1px solid rgba(15, 23, 42, .08)",
    },
    dark={
        "background": "rgba(15, 23, 42, .72)",
        "border": "1px solid rgba(255, 255, 255, .12)",
    },
)
```

This returns a FastHTML `Style` element similar to:

```css
[data-bs-theme="light"] .premium-card {
  background: rgba(255, 255, 255, .86);
  border: 1px solid rgba(15, 23, 42, .08);
}

[data-bs-theme="dark"] .premium-card {
  background: rgba(15, 23, 42, .72);
  border: 1px solid rgba(255, 255, 255, .12);
}
```

## When To Use It

- You are building a custom component with branded surfaces.
- You support both light and dark mode.
- You want one Python helper to generate both CSS variants.
- You are writing showcase-level UI where generic Bootstrap surfaces are not enough.

## API Reference

::: faststrap.core.theme.theme_variant_css
