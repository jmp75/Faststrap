# FeatureGrid

`Feature` and `FeatureGrid` are landing-page pattern components for value propositions, product capabilities, and benefits sections.

## Quick Start

```python
from faststrap import Feature, FeatureGrid

FeatureGrid(
    Feature(
        "FastHTML native",
        "Build Bootstrap interfaces directly from Python.",
        icon="lightning-charge",
    ),
    Feature(
        "HTMX ready",
        "Use hx_* attributes without custom JavaScript.",
        icon="arrow-repeat",
    ),
    Feature(
        "Themeable",
        "Stay aligned with Bootstrap and Faststrap themes.",
        icon="palette",
    ),
    columns=3,
)
```

## Parameters

### `Feature`

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `title` | `str` | required | Feature title. |
| `description` | `str` | required | Supporting feature copy. |
| `icon` | `str \| Any \| None` | `None` | Bootstrap icon name or custom element. |
| `icon_cls` | `str` | `"bg-primary text-white"` | Classes for the icon wrapper. |
| `icon_wrapper_cls` | `str \| None` | `None` | Extra icon wrapper classes. |
| `title_cls` | `str` | `"fs-4 fw-bold"` | Title classes. |
| `description_cls` | `str` | `"text-muted"` | Description classes. |
| `icon_wrapper_attrs` | `dict \| None` | `None` | Extra icon wrapper attributes. |
| `title_attrs` | `dict \| None` | `None` | Extra title attributes. |
| `description_attrs` | `dict \| None` | `None` | Extra description attributes. |
| `**kwargs` | `Any` | | Extra root attributes. |

### `FeatureGrid`

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `*features` | `Any` | | Feature elements. |
| `columns` | `int` | `3` | Number of columns at the medium breakpoint. |
| `row_cls` | `str \| None` | `None` | Extra row classes. |
| `col_cls` | `str \| None` | `None` | Extra column classes. |
| `row_attrs` | `dict \| None` | `None` | Extra row attributes. |
| `col_attrs` | `dict \| None` | `None` | Extra column attributes. |
| `**kwargs` | `Any` | | Extra root attributes. |

## API Reference

::: faststrap.components.patterns.feature.Feature

::: faststrap.components.patterns.feature.FeatureGrid
