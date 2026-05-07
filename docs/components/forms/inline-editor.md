# Inline Editor

`InlineEditor` renders a read state and an edit state for small pieces of content. It is designed for HTMX partial replacement workflows without custom JavaScript.

## Import

```python
from faststrap import InlineEditor
```

## Read Mode

```python
InlineEditor(
    name="title",
    value="Quarterly planning",
    endpoint="/tasks/1/title",
    edit_endpoint="/tasks/1/title/edit",
    id="task-title",
)
```

In read mode, the edit button can request `edit_endpoint` and replace the editor target with the edit form.

## Edit Mode

```python
InlineEditor(
    name="title",
    value="Quarterly planning",
    endpoint="/tasks/1/title",
    editing=True,
    id="task-title",
)
```

In edit mode, the form posts to `endpoint` using HTMX and swaps the response back into the same editor container.

## Patch Endpoint

```python
InlineEditor(
    name="headline",
    value="Launch brief",
    endpoint="/briefs/42/headline",
    method="patch",
    editing=True,
    id="brief-headline",
)
```

## Parameters

| Param | Type | Description |
| :--- | :--- | :--- |
| `name` | `str` | Input name. |
| `value` | `str` | Current raw value. |
| `display` | `str | None` | Optional display value for read mode. |
| `editing` | `bool` | Render the edit form instead of read mode. |
| `endpoint` | `str | None` | Save endpoint. |
| `edit_endpoint` | `str | None` | Endpoint that returns edit mode markup. |
| `method` | `post | put | patch` | HTMX save method. |
| `input_type` | `str` | Input type for edit mode. |
| `hx_target` | `str | None` | HTMX swap target. Defaults to the component `id` when available. |
| `hx_swap` | `str` | HTMX swap mode. |

::: faststrap.components.forms.inline_editor.InlineEditor
    options:
        show_source: true
        heading_level: 3
