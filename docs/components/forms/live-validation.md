# Live Validation

`LiveValidationField` and `ValidationMessage` help you build HTMX-powered form validation without writing custom JavaScript.

## Quick Start

```python
from faststrap import Input, LiveValidationField

LiveValidationField(
    Input(name="email", placeholder="you@example.com"),
    validate_url="/validate/email",
    label="Email",
    help_text="We will validate this when the field changes.",
)
```

The input receives HTMX attributes and the server endpoint should return a replacement fragment compatible with the configured target and swap behavior.

## Returning A Validation Message

```python
from faststrap import ValidationMessage


@app.post("/validate/email")
def validate_email(email: str):
    if "@" not in email:
        return ValidationMessage("Enter a valid email address.", state="invalid")
    return ValidationMessage("Looks good.", state="valid")
```

## Parameters

### `LiveValidationField`

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `input_element` | `Any` | required | Input component or FastHTML element to augment with HTMX attributes. |
| `validate_url` | `str` | required | Endpoint called for validation. |
| `label` | `str \| None` | `None` | Optional form label. |
| `help_text` | `str \| None` | `None` | Helper text shown under the input. |
| `error` | `str \| None` | `None` | Error text for invalid state. |
| `success` | `str \| None` | `None` | Success text for valid state. |
| `is_invalid` | `bool` | `False` | Marks the field invalid. |
| `is_valid` | `bool` | `False` | Marks the field valid. |
| `required` | `bool` | `False` | Marks the label/input as required. |
| `method` | `"get" \| "post"` | `"post"` | HTTP method for validation request. |
| `trigger` | `str` | `"blur changed delay:300ms"` | HTMX trigger string. |
| `target` | `str` | `"closest .mb-3"` | HTMX target for the response. |
| `swap` | `str` | `"outerHTML"` | HTMX swap strategy. |
| `indicator` | `str \| None` | `None` | Optional HTMX loading indicator selector. |
| `**kwargs` | `Any` | | Extra `FormGroup` attributes. |

### `ValidationMessage`

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `message` | `str \| None` | required | Message to render. Returns `None` when empty. |
| `state` | `"invalid" \| "valid" \| "neutral"` | `"invalid"` | Bootstrap feedback style. |
| `**kwargs` | `Any` | | Extra HTML attributes. |

## Notes

- `LiveValidationField` mutates the provided input element when it exposes an `attrs` mapping.
- The default target replaces the nearest `.mb-3`, which matches Faststrap's `FormGroup` wrapper.
- Return a full field wrapper when using `swap="outerHTML"`, or return only a message when you target a feedback container.

## API Reference

::: faststrap.components.forms.errors.LiveValidationField

::: faststrap.components.forms.errors.ValidationMessage
