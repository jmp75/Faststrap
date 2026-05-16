# SidebarNavbar

`SidebarNavbar` renders vertical navigation for dashboards, admin panels, and internal tools.

## Quick Start

```python
from faststrap import SidebarNavbar

SidebarNavbar(
    ("Dashboard", "/dashboard", "house"),
    ("Users", "/users", "people"),
    ("Settings", "/settings", "gear"),
    brand="Ops Console",
    theme="dark",
)
```

Tuple items use `(label, href)` or `(label, href, icon)`. Icons use Bootstrap Icons names without the `bi-` prefix.

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `*items` | `Any` | | Tuple items or `SidebarNavItem` components. |
| `brand` | `str \| None` | `None` | Brand label. |
| `brand_href` | `str` | `"/"` | Brand link target. |
| `position` | `str \| None` | `UNSET` | `"left"` or `"right"`. |
| `width` | `str \| None` | `UNSET` | CSS width value, defaulting to `250px`. |
| `collapsible` | `bool \| None` | `UNSET` | Adds a sidebar ID for mobile collapse patterns. |
| `theme` | `str \| None` | `UNSET` | `"dark"` or `"light"`. |
| `sticky` | `bool \| None` | `UNSET` | Adds `sticky-top`. |
| `**kwargs` | `Any` | | Extra root attributes. |

## Individual Items

```python
from faststrap import SidebarNavItem

SidebarNavItem("Dashboard", href="/dashboard", icon="speedometer2", active=True)
```

## Notes

- For full dashboard page composition, pair this with `DashboardLayout`.
- The component sets `min-height: 100vh` and the configured width inline.
- `collapsible=True` adds `id="sidebarNav"`; avoid multiple collapsible sidebars with the same ID on one page.

## API Reference

::: faststrap.components.navigation.sidebar_navbar.SidebarNavbar

::: faststrap.components.navigation.sidebar_navbar.SidebarNavItem
