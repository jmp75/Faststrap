"""Bootstrap Confirm Dialog component."""

from typing import Any

from fasthtml.common import Div, P

from ...core.registry import register
from ...core.types import VariantType
from ..feedback.modal import Modal
from ..forms.button import Button

HtmxMethod = str


def _apply_hx_method(attrs: dict[str, Any], method: HtmxMethod, url: str) -> None:
    normalized = method.lower()
    if normalized == "get":
        attrs["hx_get"] = url
    elif normalized == "put":
        attrs["hx_put"] = url
    elif normalized == "patch":
        attrs["hx_patch"] = url
    elif normalized == "delete":
        attrs["hx_delete"] = url
    else:
        attrs["hx_post"] = url


@register(category="feedback", requires_js=True)
def ConfirmDialog(
    message: str | Any,
    *,
    confirm_text: str = "Confirm",
    cancel_text: str = "Cancel",
    title: str = "Confirm Action",
    variant: VariantType = "danger",
    dialog_id: str | None = None,
    hx_confirm_method: str = "post",
    hx_confirm_url: str | None = None,
    hx_target: str | None = None,
    hx_swap: str | None = None,
    **kwargs: Any,
) -> Div:
    """Bootstrap Confirmation Dialog (pre-configured Modal).

    A modal designed for confirming destructive actions.

    Args:
        message: Body text
        confirm_text: Text for confirm button
        cancel_text: Text for cancel button
        title: Modal title
        variant: Variant for confirm button (danger, primary, etc.)
        dialog_id: ID for the modal
        hx_confirm_method: HTMX method for confirm button (post, delete, put, get)
        hx_confirm_url: URL to call on confirmation
        hx_target: HTMX target
        hx_swap: HTMX swap strategy
        **kwargs: Additional HTML attributes passed to Modal

    Returns:
        Modal component

    Example:
        >>> ConfirmDialog(
        ...     "Are you sure you want to delete this?",
        ...     hx_confirm_url="/delete/1",
        ...     confirm_text="Delete",
        ...     variant="danger"
        ... )
    """
    # Build confirm button with HTMX attributes
    btn_attrs: dict[str, Any] = {
        "variant": variant,
        "data_bs_dismiss": "modal",
    }

    if hx_confirm_url:
        # We pass hx arguments directly to Button
        _apply_hx_method(btn_attrs, hx_confirm_method, hx_confirm_url)

    if hx_target:
        btn_attrs["hx_target"] = hx_target

    if hx_swap:
        btn_attrs["hx_swap"] = hx_swap

    footer = Div(
        Button(cancel_text, variant="secondary", data_bs_dismiss="modal"),
        Button(confirm_text, **btn_attrs),
        cls="d-flex justify-content-end gap-2",
    )

    return Modal(
        P(message) if isinstance(message, str) else message,
        title=title,
        footer=footer,
        modal_id=dialog_id,
        centered=True,
        **kwargs,
    )


@register(category="feedback")
def ConfirmAction(
    *children: Any,
    url: str,
    confirm: str = "Are you sure?",
    method: HtmxMethod = "post",
    target: str | None = None,
    swap: str | None = None,
    variant: VariantType = "danger",
    **kwargs: Any,
) -> Any:
    """HTMX-friendly action button with a browser confirmation prompt.

    Use this when a full modal is too heavy and the action can be confirmed
    with HTMX's built-in `hx-confirm` behavior.
    """
    btn_attrs: dict[str, Any] = {
        "variant": variant,
        "hx_confirm": confirm,
    }
    _apply_hx_method(btn_attrs, method, url)
    if target:
        btn_attrs["hx_target"] = target
    if swap:
        btn_attrs["hx_swap"] = swap
    btn_attrs.update(kwargs)
    return Button(*children, **btn_attrs)
