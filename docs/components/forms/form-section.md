# FormSection

`FormSection` groups related form fields under an optional title, description, divider, and action row.

## Quick Start

```python
from faststrap import Button, FormSection, Input

FormSection(
    Input(name="name", label="Name"),
    Input(name="email", label="Email", type="email"),
    title="Profile",
    description="Public account details.",
    actions=Button("Save", variant="primary"),
)
```

## Parameters

| Name | Type | Default | Description |
| --- | --- | --- | --- |
| `*fields` | `Any` | required | Field components or arbitrary content. |
| `title` | `str | None` | `None` | Section heading. |
| `description` | `str | None` | `None` | Muted helper copy below the heading. |
| `actions` | `Any | list[Any] | tuple[Any, ...] | None` | `None` | Right-aligned section actions. |
| `divider` | `bool` | `True` | Adds a top border and spacing before the section. |
| `**kwargs` | `Any` | `{}` | Additional HTML/HTMX/data/ARIA attributes. |

## Notes

- Use `divider=False` for the first section in a form.
- `FormSection` is layout-only; validation still belongs to `FormGroup`, `LiveValidationField`, and server-side form handling.
