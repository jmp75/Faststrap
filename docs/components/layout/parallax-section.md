# ParallaxSection

`ParallaxSection` renders a CSS-only background image section with a configurable overlay. It is useful for landing pages, editorial sections, hero breaks, and showcase pages.

## Quick Start

```python
from faststrap import Button, ParallaxSection

ParallaxSection(
    Button("Explore rooms", variant="light"),
    img_src="/static/hotel.jpg",
    height="520px",
    overlay_opacity=0.45,
)
```

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `*children` | `Any` | empty | Content centered inside the section overlay. |
| `img_src` | `str` | required | Background image URL. |
| `height` | `str \| None` | `500px` | Section height. |
| `overlay_opacity` | `float \| None` | `0.5` | Overlay opacity clamped between `0` and `1`. |

## Notes

- Mobile browsers often handle `background-attachment: fixed` poorly, so Faststrap automatically falls back to normal scrolling below `768px`.
- `faststrap-visual.css` is loaded automatically by `add_bootstrap()`.
- Treat `img_src` like any other image URL: pass trusted/static paths, not unescaped user input.

## API Reference

::: faststrap.components.layout.parallax.ParallaxSection
