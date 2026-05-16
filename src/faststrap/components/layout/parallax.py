"""Visual layout sections."""

from __future__ import annotations

from typing import Any

from fasthtml.common import Div

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import UNSET, resolve_defaults
from ...utils.attrs import convert_attrs


@register(category="layout")
@beta
def ParallaxSection(
    *children: Any,
    img_src: str,
    height: str | None = UNSET,
    overlay_opacity: float | None = UNSET,
    **kwargs: Any,
) -> Div:
    """Render a CSS-only parallax-style background section."""
    cfg = resolve_defaults(
        "ParallaxSection",
        height=height,
        overlay_opacity=overlay_opacity,
    )
    c_height = cfg.get("height") or "500px"
    c_opacity = cfg.get("overlay_opacity")
    if c_opacity is None:
        c_opacity = 0.5
    c_opacity = min(1.0, max(0.0, float(c_opacity)))

    user_cls = kwargs.pop("cls", "")
    user_style = kwargs.pop("style", "")
    base_style = f"background-image: url('{img_src}'); height: {c_height};"
    if isinstance(user_style, str) and user_style.strip():
        base_style = f"{base_style} {user_style.strip()}"

    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-parallax-section", user_cls),
        "style": base_style,
    }
    attrs.update(convert_attrs(kwargs))

    return Div(
        Div(
            *children,
            cls="faststrap-parallax-overlay",
            style=f"--faststrap-parallax-overlay-opacity: {c_opacity};",
        ),
        **attrs,
    )
