# Visual Cards

`FlipCard`, `TiltCard`, `RevealCard`, and `GlowCard` are CSS-only visual card primitives for premium landing pages, portfolios, dashboards, and product surfaces.

They are part of core Faststrap and use Bootstrap/Faststrap theme variables. No JavaScript is required.

## Quick Start

```python
from faststrap import Button, FlipCard, GlowCard, RevealCard, TiltCard

FlipCard(
    front="Plan summary",
    back=Button("Upgrade", variant="light"),
    height="260px",
)

TiltCard("Hover me", cls="card-body")

RevealCard(
    "/static/room.jpg",
    "Harbor Suite",
    description="Private terrace, skyline view.",
    action=Button("View Room", variant="light"),
)

GlowCard("Important metric", glow_color="#38bdf8", intensity="high", cls="card-body")
```

## Components

| Component | Purpose |
| --- | --- |
| `FlipCard` | Two-sided card that flips on hover or focus-within. |
| `TiltCard` | Card with subtle 3D lift on hover. |
| `RevealCard` | Image card with a hover-revealed overlay. |
| `GlowCard` | Card with configurable glow intensity and color. |

## Parameters

### `FlipCard`

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `front` | `Any` | required | Front face content. |
| `back` | `Any` | required | Back face content. |
| `height` | `str \| None` | `300px` | Card height. |
| `width` | `str \| None` | `100%` | Card width. |
| `duration` | `str \| None` | `0.6s` | Flip animation duration. |

### `RevealCard`

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `img_src` | `str` | required | Image URL. |
| `title` | `str` | required | Overlay heading and default image alt text. |
| `description` | `str \| None` | `None` | Overlay copy. |
| `action` | `Any \| None` | `None` | Optional action element. |
| `alt` | `str \| None` | `title` | Image alt text. |
| `height` | `str \| None` | `300px` | Card height. |

### `GlowCard`

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `glow_color` | `str \| None` | `var(--bs-primary)` | CSS color for the glow. |
| `intensity` | `low \| medium \| high` | `medium` | Glow strength. |

## Notes

- These components are marked `@beta` because they are visual primitives newly absorbed into core.
- `faststrap-visual.css` is loaded automatically by `add_bootstrap()`.
- Motion respects `prefers-reduced-motion`.

## API Reference

::: faststrap.components.display.visual_cards.FlipCard

::: faststrap.components.display.visual_cards.TiltCard

::: faststrap.components.display.visual_cards.RevealCard

::: faststrap.components.display.visual_cards.GlowCard
