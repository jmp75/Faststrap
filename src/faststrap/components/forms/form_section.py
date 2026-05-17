"""Form layout helpers."""

from __future__ import annotations

from typing import Any

from fasthtml.common import H3, Div, P

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs


@register(category="forms")
@beta
def FormSection(
    *fields: Any,
    title: str | None = None,
    description: str | None = None,
    actions: Any | list[Any] | tuple[Any, ...] | None = None,
    divider: bool = True,
    **kwargs: Any,
) -> Div:
    """Group related form controls under a section heading."""
    user_cls = kwargs.pop("cls", "")

    children: list[Any] = []
    if title or description:
        header_children: list[Any] = []
        if title:
            header_children.append(H3(title, cls="h5 mb-1"))
        if description:
            header_children.append(P(description, cls="text-muted mb-0"))
        children.append(Div(*header_children, cls="mb-3"))

    children.append(Div(*fields, cls="d-grid gap-3"))

    if actions is not None:
        action_children = list(actions) if isinstance(actions, (list, tuple)) else [actions]
        children.append(
            Div(*action_children, cls="d-flex flex-wrap gap-2 justify-content-end mt-3")
        )

    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "faststrap-form-section",
            "border-top pt-4 mt-4" if divider else "",
            user_cls,
        )
    }
    attrs.update(convert_attrs(kwargs))
    return Div(*children, **attrs)
