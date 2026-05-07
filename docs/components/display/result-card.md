# Result Card

`ResultCard` presents the outcome of an action: saved settings, failed submissions, empty flows, or follow-up next steps.

It is intentionally small, semantic, and HTMX-friendly. Success and info states use `role="status"`; warning and error states use `role="alert"`.

## Import

```python
from faststrap import ResultCard, Button
```

## Basic Usage

```python
ResultCard(
    title="Settings saved",
    message="Your preferences have been updated.",
    status="success",
)
```

## Error State

```python
ResultCard(
    title="Could not save",
    message="Please review the highlighted fields and try again.",
    status="error",
)
```

## With Action

```python
ResultCard(
    title="Invite sent",
    message="We emailed the new team member.",
    status="success",
    action=Button("View team", href="/team", variant="primary"),
)
```

## Parameters

| Param | Type | Description |
| :--- | :--- | :--- |
| `title` | `str` | Main result title. |
| `message` | `str | None` | Optional supporting message. |
| `status` | `success | error | warning | info` | Semantic result state. |
| `icon` | `str | None` | Bootstrap icon name override. |
| `action` | `Any | None` | Optional action component. |
| `compact` | `bool` | Use tighter spacing. |

::: faststrap.components.display.result_card.ResultCard
    options:
        show_source: true
        heading_level: 3
