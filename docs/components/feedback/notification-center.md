# NotificationCenter

Dropdown notification hub built on Bootstrap dropdowns.

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="dropdown">
      <button class="btn btn-link position-relative" type="button">
        <i class="bi bi-bell"></i>
        <span class="badge bg-danger position-absolute top-0 start-100 translate-middle">2</span>
      </button>
      <div class="dropdown-menu dropdown-menu-end show position-static">
        <span class="dropdown-header text-uppercase">Notifications</span>
        <a class="dropdown-item" href="#">New report ready</a>
        <a class="dropdown-item" href="#">Server maintenance</a>
      </div>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import NotificationCenter

NotificationCenter(
    ("New report ready", "/reports/1"),
    ("Server maintenance", "/status"),
    count=2,
)
```
  </div>
</div>

---

## Items

Each item can be:

- a `(label, href)` tuple
- a plain string
- a custom FastHTML node

```python
NotificationCenter(
    ("Payment failed", "/billing"),
    "No new alerts",
)
```

---

## Lazy Load With HTMX

```python
NotificationCenter(
    count=5,
    endpoint="/notifications",
    hx_swap="innerHTML",
)
```

When `endpoint` is provided, the dropdown menu is loaded on click.

---

## Customization

- `badge_variant` controls the badge color
- `menu_cls` and `button_cls` let you style the dropdown
- `max_items` caps visible items
- `empty_text` sets the empty state

---

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `*items` | `Any` | | Notification items. Tuples, strings, and custom nodes are supported. |
| `count` | `int \| None` | `None` | Badge count. Omit to hide the badge. |
| `title` | `str` | `"Notifications"` | Dropdown header text. |
| `endpoint` | `str \| None` | `None` | Optional HTMX endpoint loaded when the bell is clicked. |
| `center_id` | `str \| None` | `None` | Explicit wrapper ID. Auto-generated when omitted. |
| `menu_cls` | `str \| None` | `None` | Extra dropdown menu classes. |
| `button_cls` | `str \| None` | `None` | Extra toggle button classes. |
| `badge_variant` | Bootstrap variant | `UNSET` | Badge color variant. Defaults to `danger`. |
| `empty_text` | `str` | `"No notifications"` | Empty dropdown text. |
| `max_items` | `int \| None` | `None` | Limit initially rendered items. |
| `hx_swap` | `str \| None` | `"innerHTML"` | HTMX swap style for lazy-loaded menu content. |
| `push_url` | `bool` | `False` | Push URL for HTMX loads. |
| `**kwargs` | `Any` | | Extra wrapper attributes. |

---

## Security Notes

If you load notifications over HTMX, ensure the endpoint is authenticated and returns only the current user's data.

---

## API Reference

::: faststrap.components.feedback.notification_center.NotificationCenter
    options:
        show_source: true
        heading_level: 4
