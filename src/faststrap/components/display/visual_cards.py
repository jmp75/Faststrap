"""Visual card primitives with CSS-only interaction effects."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import H4, Div, Img, P

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import UNSET, resolve_defaults
from ...utils.attrs import convert_attrs

GlowIntensity = Literal["low", "medium", "high"]


def _merge_style(base: str, user_style: Any) -> str:
    """Merge required inline styles with user-provided string styles."""
    if isinstance(user_style, str) and user_style.strip():
        return f"{base.rstrip('; ')}; {user_style.strip()}"
    return base


@register(category="display")
@beta
def FlipCard(
    front: Any,
    back: Any,
    *,
    height: str | None = UNSET,
    width: str | None = UNSET,
    duration: str | None = UNSET,
    **kwargs: Any,
) -> Div:
    """Render a CSS-only 3D flip card.

    Args:
        front: Content for the front face.
        back: Content for the back face.
        height: Card height. Defaults to ``300px``.
        width: Card width. Defaults to ``100%``.
        duration: Flip animation duration. Defaults to ``0.6s``.
        **kwargs: Additional HTML attributes.
    """
    cfg = resolve_defaults("FlipCard", height=height, width=width, duration=duration)
    c_height = cfg.get("height") or "300px"
    c_width = cfg.get("width") or "100%"
    c_duration = cfg.get("duration") or "0.6s"

    user_cls = kwargs.pop("cls", "")
    user_style = kwargs.pop("style", None)
    style = _merge_style(
        f"height: {c_height}; width: {c_width}; --faststrap-flip-duration: {c_duration};",
        user_style,
    )

    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-flip-card", user_cls),
        "style": style,
    }
    attrs.update(convert_attrs(kwargs))

    return Div(
        Div(
            Div(front, cls="faststrap-flip-card-front card"),
            Div(back, cls="faststrap-flip-card-back card"),
            cls="faststrap-flip-card-inner",
        ),
        **attrs,
    )


@register(category="display")
@beta
def TiltCard(*children: Any, **kwargs: Any) -> Div:
    """Render a card with a subtle 3D hover lift."""
    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-tilt-card card", user_cls),
    }
    attrs.update(convert_attrs(kwargs))
    return Div(*children, **attrs)


@register(category="display")
@beta
def RevealCard(
    img_src: str,
    title: str,
    *,
    description: str | None = None,
    action: Any | None = None,
    alt: str | None = None,
    height: str | None = UNSET,
    **kwargs: Any,
) -> Div:
    """Render an image card that reveals content on hover.

    Args:
        img_src: Background image URL.
        title: Overlay heading.
        description: Optional overlay copy.
        action: Optional action element, such as a ``Button``.
        alt: Image alt text. Defaults to ``title``.
        height: Card height. Defaults to ``300px``.
        **kwargs: Additional HTML attributes.
    """
    cfg = resolve_defaults("RevealCard", height=height)
    c_height = cfg.get("height") or "300px"

    user_cls = kwargs.pop("cls", "")
    user_style = kwargs.pop("style", None)
    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-reveal-card card", user_cls),
        "style": _merge_style(f"height: {c_height};", user_style),
    }
    attrs.update(convert_attrs(kwargs))

    overlay_children: list[Any] = [H4(title, cls="mb-2")]
    if description:
        overlay_children.append(P(description, cls="mb-3"))
    if action:
        overlay_children.append(action)

    return Div(
        Img(src=img_src, alt=alt or title, cls="faststrap-reveal-image"),
        Div(*overlay_children, cls="faststrap-reveal-overlay"),
        **attrs,
    )


@register(category="display")
@beta
def GlowCard(
    *children: Any,
    glow_color: str | None = UNSET,
    intensity: GlowIntensity | None = UNSET,
    **kwargs: Any,
) -> Div:
    """Render a card with an animated glow on hover."""
    cfg = resolve_defaults("GlowCard", glow_color=glow_color, intensity=intensity)
    c_color = cfg.get("glow_color") or "var(--bs-primary)"
    c_intensity = cfg.get("intensity") or "medium"

    user_cls = kwargs.pop("cls", "")
    user_style = kwargs.pop("style", None)
    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-glow-card card", f"glow-{c_intensity}", user_cls),
        "style": _merge_style(f"--faststrap-glow-color: {c_color};", user_style),
    }
    attrs.update(convert_attrs(kwargs))
    return Div(*children, **attrs)
