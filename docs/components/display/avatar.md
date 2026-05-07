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

| Param | Type | Description |
| :--- | :--- | :--- |
| `name` | `str | None` | Display name used for alt text and generated initials. |
| `src` | `str | None` | Optional image URL. |
| `alt` | `str | None` | Image alt text. Defaults to `name`. |
| `initials` | `str | None` | Explicit initials override. |
| `size` | `sm | md | lg | xl` | Avatar size. |
| `shape` | `circle | rounded | square` | Avatar shape. |
| `variant` | `str` | Bootstrap text/background variant for initials. |
| `status` | `str | None` | Optional status label stored in `data-status`. |
| `status_variant` | `str | None` | Bootstrap variant for the status dot. |

::: faststrap.components.display.avatar.Avatar
    options:
        show_source: true
        heading_level: 3

::: faststrap.components.display.avatar.AvatarGroup
    options:
        show_source: true
        heading_level: 3
