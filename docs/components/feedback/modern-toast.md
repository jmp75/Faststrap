# ModernToast

`ModernToast` is an opinionated alternative to the core Bootstrap `Toast`. It is for polished app-style notifications with configurable position, duration, variant, and visual style.

Use core `Toast` when you want Bootstrap's native toast structure. Use `ModernToast` when you want a more modern product UI surface.

## Import

```python
from faststrap import ModernToast, ModernToastStack
```

## Basic Usage

```python
ModernToast(
    "Saved",
    "Your changes were applied.",
    variant="success",
)
```

## With Position, Duration, And Style

```python
ModernToast(
    "Invite sent",
    "We emailed the new team member.",
    variant="success",
    position="top-end",
    duration=4000,
    style="glass",
)
```

## Toast Stack

```python
ModernToastStack(
    ModernToast("Saved", variant="success"),
    ModernToast("Sync delayed", "Trying again soon.", variant="warning"),
    position="bottom-end",
)
```

## With Action

```python
ModernToast(
    "Project archived",
    "You can restore it from settings.",
    variant="warning",
    action=Button("Undo", variant="link"),
)
```

## Parameters

### `ModernToast`

| Param | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `title` | `str` | required | Main toast title. |
| `message` | `str \| None` | `None` | Optional message. |
| `variant` | `VariantType` | `info` | Semantic Bootstrap variant. |
| `position` | `ToastPositionType` | `top-end` | Preferred stack position metadata. |
| `duration` | `int` | `4000` | Duration metadata in milliseconds. |
| `style` | `solid \| soft \| glass` | `glass` | Visual style class. |
| `icon` | `str \| None` | `None` | Bootstrap icon override. |
| `action` | `Any \| None` | `None` | Optional action component. |
| `dismissible` | `bool` | `True` | Shows the close button. |
| `**kwargs` | `Any` | | Extra attributes. |

### `ModernToastStack`

| Param | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `*toasts` | `Any` | | Toast children. |
| `position` | `ToastPositionType` | `top-end` | Fixed stack position. |
| `gap` | `int` | `2` | Bootstrap grid gap utility suffix. |
| `**kwargs` | `Any` | | Extra attributes. |

## Behavior Notes

- `ModernToast` is an opinionated static surface, not Bootstrap's native toast plugin.
- The close button removes the toast with a tiny inline handler.
- `duration` is emitted as metadata for app/runtime integrations; it does not auto-dismiss by itself unless your app adds that behavior.

::: faststrap.components.feedback.modern_toast.ModernToast
    options:
        show_source: true
        heading_level: 3

::: faststrap.components.feedback.modern_toast.ModernToastStack
    options:
        show_source: true
        heading_level: 3
