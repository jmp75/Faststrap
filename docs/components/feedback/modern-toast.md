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

| Component | Param | Type | Description |
| :--- | :--- | :--- | :--- |
| `ModernToast` | `title` | `str` | Main toast title. |
| `ModernToast` | `message` | `str | None` | Optional message. |
| `ModernToast` | `variant` | `VariantType` | Semantic Bootstrap variant. |
| `ModernToast` | `position` | `ToastPositionType` | Preferred stack position metadata. |
| `ModernToast` | `duration` | `int` | Duration in milliseconds. |
| `ModernToast` | `style` | `solid | soft | glass` | Visual style class. |
| `ModernToast` | `action` | `Any | None` | Optional action component. |
| `ModernToastStack` | `*toasts` | `Any` | Toast children. |
| `ModernToastStack` | `position` | `ToastPositionType` | Fixed stack position. |

::: faststrap.components.feedback.modern_toast.ModernToast
    options:
        show_source: true
        heading_level: 3

::: faststrap.components.feedback.modern_toast.ModernToastStack
    options:
        show_source: true
        heading_level: 3
