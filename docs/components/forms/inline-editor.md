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

## Complete HTMX Flow

This is the simplest read/edit loop:

```python
from fasthtml.common import fast_app
from faststrap import InlineEditor

app, rt = fast_app()

title = "Quarterly planning"


def title_editor(editing: bool = False):
    return InlineEditor(
        "title",
        title,
        editing=editing,
        endpoint="/title",
        edit_endpoint="/title/edit",
        id="title-editor",
        method="patch",
    )


@rt("/")
def home():
    return title_editor()


@rt("/title/edit")
def edit_title():
    return title_editor(editing=True)


@rt("/title", methods=["PATCH"])
async def save_title(request):
    global title
    form = await request.form()
    title = form.get("title", "")
    return title_editor()
```

The important idea: the edit endpoint returns `editing=True`, and the save endpoint returns the read view again.

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
