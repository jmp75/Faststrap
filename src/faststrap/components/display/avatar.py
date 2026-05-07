"""Avatar and AvatarGroup components."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div, Img, Span

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs

AvatarSize = Literal["xs", "sm", "md", "lg", "xl"]
AvatarShape = Literal["circle", "rounded", "square"]

AVATAR_SIZES: dict[str, str] = {
    "xs": "1.5rem",
    "sm": "2rem",
    "md": "2.5rem",
    "lg": "3rem",
    "xl": "4rem",
}


def _initials_from_name(name: str | None, fallback: str = "?") -> str:
    if not name:
        return fallback
    parts = [part for part in name.replace("-", " ").split() if part]
    if not parts:
        return fallback
    if len(parts) == 1:
        return parts[0][:2].upper()
    return f"{parts[0][0]}{parts[-1][0]}".upper()


def _shape_class(shape: AvatarShape) -> str:
    return {
        "circle": "rounded-circle",
        "rounded": "rounded",
        "square": "rounded-0",
    }[shape]


@register(category="display")
@beta
def Avatar(
    name: str | None = None,
    *,
    src: str | None = None,
    alt: str | None = None,
    initials: str | None = None,
    size: AvatarSize = "md",
    shape: AvatarShape = "circle",
    variant: str = "secondary",
    status: str | None = None,
    status_variant: str | None = None,
    **kwargs: Any,
) -> Span:
    """Render a user avatar from an image or initials."""
    dimension = AVATAR_SIZES.get(size, AVATAR_SIZES["md"])
    user_cls = kwargs.pop("cls", "")
    classes = [
        "faststrap-avatar",
        "d-inline-flex",
        "align-items-center",
        "justify-content-center",
        "position-relative",
        "fw-semibold",
        "text-uppercase",
        "overflow-hidden",
        _shape_class(shape),
    ]
    if not src:
        classes.extend([f"text-bg-{variant}"])

    attrs: dict[str, Any] = {
        "cls": merge_classes(" ".join(classes), user_cls),
        "style": {
            "width": dimension,
            "height": dimension,
            "min-width": dimension,
            "font-size": f"calc({dimension} * 0.38)",
        },
        "title": name,
        "aria_label": alt or name or "Avatar",
    }
    attrs.update(convert_attrs(kwargs))

    if src:
        content: Any = Img(
            src=src,
            alt=alt or name or "",
            cls="w-100 h-100 object-fit-cover",
        )
    else:
        content = Span(initials or _initials_from_name(name), aria_hidden="true")

    children = [content]
    if status:
        dot_variant = status_variant or {
            "online": "success",
            "busy": "danger",
            "away": "warning",
            "offline": "secondary",
        }.get(status, "secondary")
        children.append(
            Span(
                cls=(
                    "position-absolute bottom-0 end-0 rounded-circle "
                    f"bg-{dot_variant} border border-2 border-body"
                ),
                style={
                    "width": "25%",
                    "height": "25%",
                    "min-width": "0.55rem",
                    "min-height": "0.55rem",
                },
                aria_label=status,
            )
        )

    return Span(*children, **attrs)


@register(category="display")
@beta
def AvatarGroup(
    *avatars: Any,
    max_visible: int | None = None,
    total: int | None = None,
    size: AvatarSize = "md",
    overlap: bool = True,
    **kwargs: Any,
) -> Div:
    """Render a compact group of avatars."""
    visible = list(avatars)
    hidden_count = 0
    if max_visible is not None and max_visible >= 0:
        hidden_count = max(0, len(visible) - max_visible)
        visible = visible[:max_visible]

    if total is not None:
        hidden_count = max(hidden_count, total - len(visible))

    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-avatar-group d-inline-flex align-items-center", user_cls),
        "role": "group",
        "aria_label": "Avatar group",
    }
    attrs.update(convert_attrs(kwargs))

    wrapped = []
    for index, avatar in enumerate(visible):
        style = {"z-index": str(len(visible) - index)}
        if overlap and index > 0:
            style["margin-left"] = "-0.5rem"
        wrapped.append(
            Span(
                avatar,
                cls="d-inline-flex rounded-circle border border-2 border-body",
                style=style,
            )
        )

    if hidden_count > 0:
        counter_style = {"margin-left": "-0.5rem"} if overlap and wrapped else {}
        wrapped.append(
            Span(
                Avatar(initials=f"+{hidden_count}", size=size, variant="light", shape="circle"),
                cls="d-inline-flex rounded-circle border border-2 border-body",
                style=counter_style,
            )
        )

    return Div(*wrapped, **attrs)
