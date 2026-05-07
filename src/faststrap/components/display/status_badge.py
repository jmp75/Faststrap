"""Semantic status badge components."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Span

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...core.types import VariantType
from ...utils.attrs import convert_attrs
from ...utils.icons import Icon
from .badge import Badge

StatusType = Literal[
    "success",
    "warning",
    "error",
    "danger",
    "info",
    "neutral",
    "pending",
    "active",
    "inactive",
]

STATUS_VARIANTS: dict[StatusType, VariantType] = {
    "success": "success",
    "active": "success",
    "warning": "warning",
    "pending": "warning",
    "error": "danger",
    "danger": "danger",
    "info": "info",
    "neutral": "secondary",
    "inactive": "secondary",
}

STATUS_ICONS = {
    "success": "check-circle",
    "active": "check-circle",
    "warning": "exclamation-triangle",
    "pending": "clock",
    "error": "x-circle",
    "danger": "x-circle",
    "info": "info-circle",
    "neutral": "circle",
    "inactive": "dash-circle",
}


@register(category="display")
@beta
def StatusBadge(
    label: str,
    *,
    status: StatusType = "neutral",
    variant: VariantType | None = None,
    icon: str | None = None,
    show_dot: bool = False,
    pill: bool = True,
    **kwargs: Any,
) -> Span:
    """Render a semantic status badge."""
    resolved_variant = variant or STATUS_VARIANTS.get(status, "secondary")
    resolved_icon = icon if icon is not None else STATUS_ICONS.get(status)
    user_cls = kwargs.pop("cls", "")
    content: list[Any] = []

    if show_dot:
        content.append(
            Span(
                cls="rounded-circle d-inline-block",
                style={"width": "0.45rem", "height": "0.45rem", "background": "currentColor"},
                aria_hidden="true",
            )
        )
    elif resolved_icon:
        content.append(Icon(resolved_icon, cls="me-1", aria_hidden="true"))

    content.append(label)
    return Badge(
        *content,
        variant=resolved_variant,
        pill=pill,
        cls=merge_classes(
            "faststrap-status-badge d-inline-flex align-items-center gap-1", user_cls
        ),
        data_status=status,
        **kwargs,
    )


@register(category="display")
@beta
def BadgeGroup(
    *badges: Any,
    gap: int = 2,
    align: str = "center",
    **kwargs: Any,
) -> Span:
    """Render a wrapping group of badges or chips."""
    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes(
            f"faststrap-badge-group d-inline-flex flex-wrap align-items-{align} gap-{gap}",
            user_cls,
        ),
    }
    attrs.update(convert_attrs(kwargs))
    return Span(*badges, **attrs)
