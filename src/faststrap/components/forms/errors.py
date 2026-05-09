"""Helpers for mapping backend validation errors to FormGroup."""

from __future__ import annotations

from collections.abc import Iterable, Mapping
from typing import Any, Literal

from fasthtml.common import H6, Div, Li, Ul

from ...core.registry import register
from ...core.theme import UNSET, resolve_defaults
from ...utils.attrs import convert_attrs
from ..feedback.alert import Alert
from .formgroup import FormGroup


def extract_field_error(errors: Mapping[str, Any] | None, field: str) -> str | None:
    """Extract a single displayable error message for a field."""
    if not errors or field not in errors:
        return None
    value = errors[field]
    if isinstance(value, str):
        return value
    if isinstance(value, (list, tuple)):
        if not value:
            return None
        return str(value[0])
    if isinstance(value, dict):
        if "msg" in value:
            return str(value["msg"])
        if "message" in value:
            return str(value["message"])
    return str(value)


def map_formgroup_validation(
    errors: Mapping[str, Any] | None,
    field: str,
) -> dict[str, Any]:
    """Return FormGroup-ready validation flags for a given field."""
    error = extract_field_error(errors, field)
    return {
        "error": error,
        "is_invalid": bool(error),
    }


@register(category="forms")
def ValidationMessage(
    message: str | None,
    *,
    state: Literal["invalid", "valid", "neutral"] = "invalid",
    **kwargs: Any,
) -> Div | None:
    """Render a Bootstrap-compatible validation feedback message.

    This is useful for HTMX live validation endpoints that return only the
    small feedback fragment for one field.
    """
    if not message:
        return None

    cls = kwargs.pop("cls", "")
    state_cls = {
        "invalid": "invalid-feedback d-block",
        "valid": "valid-feedback d-block",
        "neutral": "form-text text-muted",
    }[state]
    attrs: dict[str, Any] = {"cls": f"{state_cls} {cls}".strip()}
    attrs.update(convert_attrs(kwargs))
    return Div(message, **attrs)


@register(category="forms")
def LiveValidationField(
    input_element: Any,
    validate_url: str,
    *,
    label: str | None = None,
    help_text: str | None = None,
    error: str | None = None,
    success: str | None = None,
    is_invalid: bool = False,
    is_valid: bool = False,
    required: bool = False,
    method: Literal["get", "post"] = "post",
    trigger: str = "blur changed delay:300ms",
    target: str = "closest .mb-3",
    swap: str = "outerHTML",
    indicator: str | None = None,
    **kwargs: Any,
) -> Any:
    """FormGroup wrapper that wires an input for HTMX live validation.

    The validation endpoint should return a replacement `FormGroup` or another
    fragment compatible with the configured `hx_target`/`hx_swap`.
    """
    if hasattr(input_element, "attrs"):
        if method == "get":
            input_element.attrs["hx-get"] = validate_url
        else:
            input_element.attrs["hx-post"] = validate_url
        input_element.attrs["hx-trigger"] = trigger
        input_element.attrs["hx-target"] = target
        input_element.attrs["hx-swap"] = swap
        if indicator:
            input_element.attrs["hx-indicator"] = indicator

    return FormGroup(
        input_element,
        label=label,
        help_text=help_text,
        error=error,
        success=success,
        is_invalid=is_invalid,
        is_valid=is_valid,
        required=required,
        **kwargs,
    )


@register(category="forms")
def FormErrorSummary(
    errors: Mapping[str, Any] | Iterable[str] | str | None,
    *,
    title: str = "Please fix the following",
    variant: str | None = UNSET,
    heading_cls: str | None = UNSET,
    list_cls: str | None = None,
    show_field_names: bool = True,
    dismissible: bool | None = UNSET,
    **kwargs: Any,
) -> Any | None:
    """Render a compact alert summary for validation errors."""
    if not errors:
        return None

    cfg = resolve_defaults(
        "Alert",
        variant=variant,
        dismissible=dismissible,
        heading_cls=heading_cls,
    )
    c_variant = cfg.get("variant", variant)
    c_dismissible = cfg.get("dismissible", dismissible)
    c_heading_cls = cfg.get("heading_cls", heading_cls) or "alert-heading h6 mb-2"

    items: list[str] = []

    if isinstance(errors, Mapping):
        for field, _value in errors.items():
            message = extract_field_error(errors, field)
            if message is None:
                continue
            if show_field_names:
                items.append(f"{field}: {message}")
            else:
                items.append(message)
    elif isinstance(errors, str):
        items.append(errors)
    elif isinstance(errors, Iterable):
        for value in errors:
            if value is None:
                continue
            items.append(str(value))

    if not items:
        return None

    list_class = list_cls or "mb-0"
    list_el = Ul(*(Li(item) for item in items), cls=list_class)
    content = Div(
        H6(title, cls=c_heading_cls),
        list_el,
    )
    return Alert(
        content,
        variant=c_variant,
        dismissible=c_dismissible,
        **kwargs,
    )


@register(category="forms")
def FormGroupFromErrors(
    input_element: Any,
    field: str,
    errors: Mapping[str, Any] | None = None,
    **kwargs: Any,
) -> Any:
    """Build FormGroup and auto-apply backend error state for one field."""
    mapping = map_formgroup_validation(errors, field)
    return FormGroup(input_element, **mapping, **kwargs)
