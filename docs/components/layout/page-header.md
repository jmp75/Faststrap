# PageHeader

`PageHeader` renders a reusable page title, subtitle, optional eyebrow, badge, and action area.

## Quick Start

```python
from faststrap import PageHeader, Button, Badge

PageHeader(
    "Reports",
    eyebrow="Analytics",
    subtitle="Quarterly performance and exports.",
    badge=Badge("Live", variant="success"),
    actions=[
        Button("Export", variant="secondary", outline=True),
        Button("New Report", variant="primary"),
    ],
)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `title` | `str` | required | Main page heading. |
| `subtitle` | `str | None` | `None` | Muted supporting copy below the title. |
| `eyebrow` | `str | None` | `None` | Small uppercase label above the heading. |
| `badge` | `Any | None` | `None` | Inline badge or status element beside the title. |
| `actions` | `Any | list[Any] | tuple[Any, ...] | None` | `None` | Right-aligned action content. |
| `**kwargs` | `Any` | `{}` | Additional HTML/HTMX/data/ARIA attributes. |

## Notes

- On small screens, the actions stack below the title.
- On large screens, the title and actions align horizontally with `justify-content-between`.

## API Reference

::: faststrap.components.layout.page_header.PageHeader
    options:
        show_source: true
        heading_level: 4
