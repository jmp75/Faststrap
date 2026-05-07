"""Stepper components for multi-step workflows."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import A, Div, Span

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs
from ...utils.icons import Icon

StepStatus = Literal["complete", "current", "pending", "error"]
StepperOrientation = Literal["horizontal", "vertical"]

STEP_VARIANTS = {
    "complete": "success",
    "current": "primary",
    "pending": "secondary",
    "error": "danger",
}


@register(category="display")
@beta
def StepperStep(
    title: str,
    *,
    description: str | None = None,
    status: StepStatus = "pending",
    step: int | str | None = None,
    icon: str | None = None,
    href: str | None = None,
    **kwargs: Any,
) -> Div:
    """Render a single step for Stepper."""
    user_cls = kwargs.pop("cls", "")
    variant = STEP_VARIANTS.get(status, "secondary")
    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "faststrap-stepper-step d-flex align-items-start gap-2 flex-grow-1",
            f"is-{status}",
            user_cls,
        ),
        "data_status": status,
        "aria_current": "step" if status == "current" else None,
    }
    attrs.update(convert_attrs(kwargs))

    marker_content: Any = step
    if icon:
        marker_content = Icon(icon, aria_hidden="true")
    elif status == "complete":
        marker_content = Icon("check", aria_hidden="true")
    elif step is None:
        marker_content = ""

    marker = Span(
        marker_content,
        cls=(
            "faststrap-stepper-marker rounded-circle d-inline-flex "
            f"align-items-center justify-content-center text-bg-{variant} fw-semibold"
        ),
        style={"width": "2rem", "height": "2rem", "min-width": "2rem"},
        aria_hidden="true",
    )
    label = Div(
        Span(title, cls="fw-semibold d-block"),
        Span(description, cls="small text-muted") if description else "",
        cls="min-w-0",
    )
    content = Div(marker, label, cls="d-flex align-items-start gap-2")
    if href:
        content = A(content, href=href, cls="text-decoration-none text-reset")

    return Div(content, **attrs)


@register(category="display")
@beta
def Stepper(
    *steps: Any,
    orientation: StepperOrientation = "horizontal",
    numbered: bool = True,
    **kwargs: Any,
) -> Div:
    """Render a progress stepper for onboarding, setup, or checkout flows."""
    user_cls = kwargs.pop("cls", "")
    direction_cls = "flex-column" if orientation == "vertical" else "flex-column flex-md-row"
    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "faststrap-stepper d-flex gap-3",
            direction_cls,
            user_cls,
        ),
        "role": "list",
        "data_fs_stepper": "true",
        "data_orientation": orientation,
    }
    attrs.update(convert_attrs(kwargs))

    rendered_steps = []
    for index, step_item in enumerate(steps, start=1):
        if isinstance(step_item, str):
            step_item = StepperStep(step_item, step=index if numbered else None)
        rendered_steps.append(Div(step_item, role="listitem", cls="flex-grow-1"))

    return Div(*rendered_steps, **attrs)
