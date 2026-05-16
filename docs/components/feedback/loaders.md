# CSS Loaders

Faststrap ships additional CSS-only loaders for interfaces that need more personality than the default Bootstrap `Spinner`.

Use these for loading states, background jobs, AI generation status, and dashboard refreshes. They are dependency-free and theme-aware.

## Quick Start

```python
from faststrap import (
    DotsLoader,
    RingLoader,
    WaveLoader,
    PulseLoader,
    PolygonLoader,
    TypewriterLoader,
    ShadowLoader,
    ProgressRing,
)

DotsLoader(variant="info", label="Searching")
RingLoader(size="48px", variant="success")
WaveLoader(variant="warning")
PulseLoader(size="lg", variant="danger")
PolygonLoader(label="Preparing report")
TypewriterLoader("Generating...")
ShadowLoader("Training...")
ProgressRing(72, variant="success")
```

## Components

| Component | Purpose |
| --- | --- |
| `DotsLoader` | Three bouncing dots. |
| `RingLoader` | Spinning segmented ring. |
| `WaveLoader` | Vertical wave bars. |
| `PulseLoader` | Pulsing circle. |
| `PolygonLoader` | Shape-shifting geometric loader. |
| `TypewriterLoader` | Text reveal/typewriter loader. |
| `ShadowLoader` | Text shadow loading effect. |
| `ProgressRing` | SVG circular progress indicator. |

## Common Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `variant` | `str \| None` | `primary` | Bootstrap variant color. |
| `label` | `str \| None` | `Loading...` | Accessible label for screen readers. |
| `size` | `str \| sm \| md \| lg` | component-specific | Loader size. |

## ProgressRing

```python
ProgressRing(
    42,
    max_value=100,
    variant="primary",
    show_text=True,
    label="Profile completion",
)
```

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `value` | `int \| float` | required | Current value. |
| `max_value` | `int \| float` | `100` | Maximum value. |
| `show_text` | `bool` | `True` | Show percentage label in the center. |

## Accessibility

- Loader components render `role="status"` and include visually hidden labels.
- `ProgressRing` renders `role="progressbar"` with `aria-valuenow`, `aria-valuemin`, and `aria-valuemax`.
- Animations respect `prefers-reduced-motion`.

## API Reference

::: faststrap.components.feedback.loaders.DotsLoader

::: faststrap.components.feedback.loaders.RingLoader

::: faststrap.components.feedback.loaders.WaveLoader

::: faststrap.components.feedback.loaders.PulseLoader

::: faststrap.components.feedback.loaders.PolygonLoader

::: faststrap.components.feedback.loaders.TypewriterLoader

::: faststrap.components.feedback.loaders.ShadowLoader

::: faststrap.components.feedback.loaders.ProgressRing
