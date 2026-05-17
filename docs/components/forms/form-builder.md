# FormBuilder.from_pydantic (Beta)

`FormBuilder.from_pydantic()` generates a Bootstrap-styled form from a Pydantic model.

!!! warning "Pydantic v2 required"
    `FormBuilder.from_pydantic()` reads `model_fields`, which is the Pydantic v2 model API. Pydantic v1 models are not supported by this helper.

!!! info "Naming update in v0.6.1"
    Starting in Faststrap `v0.6.1`, the preferred import is `FormBuilder` to avoid confusion
    with FastHTML's native `Form` element.

    - `v0.6.1+`: `from faststrap import FormBuilder`
    - `v0.6.0 and earlier`: `from faststrap import Form`
    - `Form` remains available as a compatibility alias, but new code should prefer `FormBuilder`.

## Import

```python
from faststrap import FormBuilder
```

## Basic Usage

```python
from pydantic import BaseModel, EmailStr

class Signup(BaseModel):
    email: EmailStr
    age: int
    marketing_opt_in: bool = False

form = FormBuilder.from_pydantic(Signup, action="/signup")
```

## Supported Field Mapping (MVP)

- `str` -> text input
- `EmailStr` -> email input
- `int` -> number input
- `float` -> number input (`step="any"`)
- `bool` -> checkbox
- `Literal[...]` -> select
- `Enum` -> select

## Options

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `model_class` | `type[Any]` | required | Pydantic `BaseModel` class. |
| `action` | `str \| None` | `None` | Form submit URL. |
| `method` | `str` | `"post"` | Form method. |
| `include` | `list[str] \| None` | `None` | Include only selected fields. |
| `exclude` | `list[str] \| None` | `None` | Exclude selected fields. |
| `submit_label` | `str` | `"Submit"` | Submit button text. |
| `submit_variant` | `str` | `"primary"` | Bootstrap button variant. |
| `form_cls` | `str` | `""` | Extra form classes. |
| `button_cls` | `str` | `""` | Extra submit button classes. |
| `**kwargs` | `Any` | | Extra form attributes, including HTMX attributes. |

## HTMX Submit Example

```python
FormBuilder.from_pydantic(
    Signup,
    hx_post="/signup",
    hx_target="#signup-result",
    hx_swap="outerHTML",
    submit_label="Create account",
)
```

## Validation Flow

Use `FormErrorSummary`, `FormGroupFromErrors`, `LiveValidationField`, and `ValidationMessage` when you need server-side error rendering or live field validation. `FormBuilder.from_pydantic()` focuses on generating the initial Bootstrap-styled form.

## Backward Compatibility

If you are maintaining a project pinned below `v0.6.1`, this older import still works:

```python
from faststrap import Form

form = Form.from_pydantic(Signup, action="/signup")
```

## API Reference

::: faststrap.components.forms.form.FormBuilder
    options:
        show_source: true
        heading_level: 4

::: faststrap.components.forms.form.Form
    options:
        show_source: true
        heading_level: 4
