"""Reusable page-level header component."""

from __future__ import annotations

from typing import Any

from fasthtml.common import H1, Div, P, Span

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs


@register(category="layout")
@beta
def PageHeader(
    title: str,
    *,
    subtitle: str | None = None,
    eyebrow: str | None = None,
    badge: Any | None = None,
    actions: Any | list[Any] | tuple[Any, ...] | None = None,
    **kwargs: Any,
) -> Div:
    """Render a page title area with optional subtitle and actions."""
    user_cls = kwargs.pop("cls", "")

    title_children: list[Any] = []
    if eyebrow:
        title_children.append(Span(eyebrow, cls="text-uppercase text-muted small fw-semibold"))

    heading_children: list[Any] = [title]
    if badge is not None:
        heading_children.append(Span(badge, cls="ms-2 align-middle"))
    title_children.append(H1(*heading_children, cls="h2 mb-1"))

    if subtitle:
        title_children.append(P(subtitle, cls="text-muted mb-0"))

    children: list[Any] = [Div(*title_children)]
    if actions is not None:
        if isinstance(actions, (list, tuple)):
            action_children = list(actions)
        else:
            action_children = [actions]
        children.append(Div(*action_children, cls="d-flex flex-wrap gap-2 align-items-center"))

    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "d-flex flex-column flex-lg-row align-items-lg-center justify-content-between gap-3 mb-4",
            user_cls,
        )
    }
    attrs.update(convert_attrs(kwargs))
    return Div(*children, **attrs)
