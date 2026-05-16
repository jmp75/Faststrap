# Avatar

`Avatar` and `AvatarGroup` render people, teams, or accounts with a consistent Bootstrap-friendly shape. Use images when available, and fall back to initials when not.

## Import

```python
from faststrap import Avatar, AvatarGroup
```

## Basic Usage

```python
Avatar(name="Ada Lovelace")
Avatar(name="Grace Hopper", src="/static/grace.jpg")
```

## With Presence

```python
Avatar(
    name="Katherine Johnson",
    status="online",
    status_variant="success",
)
```

## Avatar Groups

```python
AvatarGroup(
    Avatar(name="Ada Lovelace"),
    Avatar(name="Grace Hopper"),
    Avatar(name="Katherine Johnson"),
    max_visible=2,
    total=5,
)
```

`AvatarGroup` shows the visible avatars and adds a `+N` counter when there are more people than the visible limit.

## Parameters

### `Avatar`

| Param | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `name` | `str \| None` | `None` | Display name used for title, ARIA label, and generated initials. |
| `src` | `str \| None` | `None` | Optional image URL. |
| `alt` | `str \| None` | `None` | Image alt text. Defaults to `name`. |
| `initials` | `str \| None` | `None` | Explicit initials override. |
| `size` | `xs \| sm \| md \| lg \| xl` | `md` | Avatar size. |
| `shape` | `circle \| rounded \| square` | `circle` | Avatar shape. |
| `variant` | `str` | `secondary` | Bootstrap text/background variant for initials. |
| `status` | `str \| None` | `None` | Optional status label. Common values: `online`, `busy`, `away`, `offline`. |
| `status_variant` | `str \| None` | `None` | Bootstrap variant for the status dot. |
| `**kwargs` | `Any` | | Extra attributes. |

### `AvatarGroup`

| Param | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `*avatars` | `Any` | | Avatar components. |
| `max_visible` | `int \| None` | `None` | Maximum avatars to show before adding a `+N` counter. |
| `total` | `int \| None` | `None` | Total people count when not all avatars are passed. |
| `size` | `xs \| sm \| md \| lg \| xl` | `md` | Size for the generated `+N` counter avatar. |
| `overlap` | `bool` | `True` | Overlap avatars with negative margin. |
| `**kwargs` | `Any` | | Extra group attributes. |

::: faststrap.components.display.avatar.Avatar
    options:
        show_source: true
        heading_level: 3

::: faststrap.components.display.avatar.AvatarGroup
    options:
        show_source: true
        heading_level: 3
