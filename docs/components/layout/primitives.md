# Layout Primitives

`Stack`, `Cluster`, and `Center` cover the flexbox layouts you write constantly while keeping markup Bootstrap-native and dependency-free.

## Quick Start

```python
from faststrap import Stack, Cluster, Center, Button

Stack(
    "Profile",
    "Billing",
    "Security",
    gap=3,
)

Cluster(
    Button("Save", variant="primary"),
    Button("Cancel", variant="secondary", outline=True),
    justify="end",
)

Center(
    "Nothing selected yet",
    min_height="40vh",
    max_width="32rem",
)
```

## Parameters

| Component | Key Parameters | Notes |
| --- | --- | --- |
| `Stack` | `gap`, `align`, `justify` | Vertical `d-flex flex-column` composition. |
| `Cluster` | `gap`, `align`, `justify`, `wrap` | Horizontal action rows, filter chips, and toolbar groups. |
| `Center` | `min_height`, `max_width`, `text_center` | Empty states, hero copy, and centered panels. |

All three accept `**kwargs`, including `cls`, `id`, `style`, `hx_*`, `data_*`, and `aria_*` attributes.

## Notes

- These are intentionally zero-JS and use Bootstrap utility classes.
- `gap` maps to Bootstrap's `gap-*` scale.
- `align` maps to `align-items-*`; `justify` maps to `justify-content-*`.
