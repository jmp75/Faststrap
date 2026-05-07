"""Timeline components for activity and audit feeds."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import H6, Div, P, Small, Span

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs
from ...utils.icons import Icon

TimelineDensity = Literal["comfortable", "compact"]


@register(category="display")
@beta
def TimelineItem(
    title: str,
    *,
    description: Any | None = None,
    time: str | None = None,
    icon: str | None = None,
    variant: str = "primary",
    active: bool = False,
    meta: Any | None = None,
    **kwargs: Any,
) -> Div:
    """Render one event in a timeline."""
    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-timeline-item position-relative d-flex gap-3", user_cls),
        "data_fs_timeline_item": "true",
    }
    attrs.update(convert_attrs(kwargs))

    marker_cls = merge_classes(
        "faststrap-timeline-marker rounded-circle d-inline-flex align-items-center justify-content-center",
        f"text-bg-{variant}",
        "shadow-sm" if active else "",
    )
    marker = Span(
        Icon(icon, aria_hidden="true") if icon else "",
        cls=marker_cls,
        style={"width": "2rem", "height": "2rem", "min-width": "2rem"},
        aria_hidden="true",
    )

    body_parts: list[Any] = [
        Div(
            H6(title, cls="mb-1"),
            Small(time, cls="text-muted") if time else "",
            cls="d-flex flex-wrap align-items-baseline justify-content-between gap-2",
        )
    ]
    if description:
        body_parts.append(P(description, cls="mb-1 text-muted"))
    if meta:
        body_parts.append(Div(meta, cls="mt-2"))

    return Div(marker, Div(*body_parts, cls="flex-grow-1 min-w-0"), **attrs)


@register(category="display")
@beta
def Timeline(
    *items: Any,
    density: TimelineDensity = "comfortable",
    **kwargs: Any,
) -> Div:
    """Render a vertical timeline of events."""
    user_cls = kwargs.pop("cls", "")
    spacing_cls = "gap-3" if density == "compact" else "gap-4"
    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "faststrap-timeline d-flex flex-column position-relative",
            spacing_cls,
            user_cls,
        ),
        "data_fs_timeline": "true",
    }
    attrs.update(convert_attrs(kwargs))
    return Div(*items, **attrs)
