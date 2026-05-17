# Placeholder

`Placeholder`, `PlaceholderCard`, and `PlaceholderButton` render Bootstrap skeleton-loading UI for content that is still loading.

Use them when you want a layout-preserving loading state instead of a spinner. Placeholders are especially useful for cards, lists, dashboard metrics, and delayed HTMX regions.

## Import

```python
from faststrap import Placeholder, PlaceholderButton, PlaceholderCard
```

## Basic Usage

```python
Placeholder(width="100%")
Placeholder(width="75%", animation="glow")
Placeholder(width="50%", variant="primary")
```

## Card Skeleton

```python
PlaceholderCard(animation="glow")
PlaceholderCard(show_image=False, animation="wave")
```

## Button Skeleton

```python
PlaceholderButton(width="120px", animation="glow")
```

## Parameters

| Component | Key Parameters | Notes |
| --- | --- | --- |
| `Placeholder` | `width`, `height`, `animation`, `variant`, `size` | Low-level skeleton span. |
| `PlaceholderCard` | `show_image`, `show_title`, `show_text`, `animation` | Prebuilt card-shaped loading state. |
| `PlaceholderButton` | `width`, `animation`, `variant` | Button-shaped skeleton. |

All three accept `**kwargs`, including `cls`, `id`, `style`, `data_*`, and `aria_*` attributes.

## Accessibility

Wrap loading regions with appropriate status text when users need to know that content is changing:

```python
Div(
    PlaceholderCard(animation="glow"),
    aria_busy="true",
    aria_label="Loading account summary",
)
```

## API Reference

::: faststrap.components.feedback.placeholder.Placeholder
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.feedback.placeholder.PlaceholderCard
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.feedback.placeholder.PlaceholderButton
    options:
        show_source: true
        heading_level: 4
