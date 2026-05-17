"""Small layout primitives for common flexbox compositions."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import UNSET, resolve_defaults
from ...utils.attrs import convert_attrs

Align = Literal["start", "center", "end", "stretch", "baseline"]
Justify = Literal["start", "center", "end", "between", "around", "evenly"]


def _align_class(value: str | None) -> str:
    return f"align-items-{value}" if value else ""


def _justify_class(value: str | None) -> str:
    return f"justify-content-{value}" if value else ""


def _merge_style(base: str, user_style: Any) -> str:
    if isinstance(user_style, str) and user_style.strip():
        if not base.strip():
            return user_style.strip()
        return f"{base.rstrip('; ')}; {user_style.strip()}"
    return base


@register(category="layout")
@beta
def Stack(
    *children: Any,
    gap: int | str | None = UNSET,
    align: Align | None = UNSET,
    justify: Justify | None = UNSET,
    **kwargs: Any,
) -> Div:
    """Render a vertical flex stack with a Bootstrap gap scale."""
    cfg = resolve_defaults("Stack", gap=gap, align=align, justify=justify)
    c_gap = cfg.get("gap")
    if c_gap is None:
        c_gap = 3
    c_align = cfg.get("align")
    c_justify = cfg.get("justify")

    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "d-flex flex-column",
            f"gap-{c_gap}",
            _align_class(c_align),
            _justify_class(c_justify),
            user_cls,
        )
    }
    attrs.update(convert_attrs(kwargs))
    return Div(*children, **attrs)


@register(category="layout")
@beta
def Cluster(
    *children: Any,
    gap: int | str | None = UNSET,
    align: Align | None = UNSET,
    justify: Justify | None = UNSET,
    wrap: bool | None = UNSET,
    **kwargs: Any,
) -> Div:
    """Render a horizontal wrapping cluster for action rows and chips."""
    cfg = resolve_defaults("Cluster", gap=gap, align=align, justify=justify, wrap=wrap)
    c_gap = cfg.get("gap")
    if c_gap is None:
        c_gap = 2
    c_align = cfg.get("align") or "center"
    c_justify = cfg.get("justify")
    c_wrap = cfg.get("wrap")
    if c_wrap is None:
        c_wrap = True

    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "d-flex",
            "flex-wrap" if c_wrap else "flex-nowrap",
            f"gap-{c_gap}",
            _align_class(c_align),
            _justify_class(c_justify),
            user_cls,
        )
    }
    attrs.update(convert_attrs(kwargs))
    return Div(*children, **attrs)


@register(category="layout")
@beta
def Center(
    *children: Any,
    min_height: str | None = UNSET,
    max_width: str | None = UNSET,
    text_center: bool | None = UNSET,
    **kwargs: Any,
) -> Div:
    """Render content centered on both axes."""
    cfg = resolve_defaults(
        "Center",
        min_height=min_height,
        max_width=max_width,
        text_center=text_center,
    )
    c_min_height = cfg.get("min_height")
    c_max_width = cfg.get("max_width")
    c_text_center = cfg.get("text_center")
    if c_text_center is None:
        c_text_center = True

    user_cls = kwargs.pop("cls", "")
    user_style = kwargs.pop("style", None)
    styles: list[str] = []
    if c_min_height:
        styles.append(f"min-height: {c_min_height};")
    if c_max_width:
        styles.append(f"max-width: {c_max_width}; margin-inline: auto;")

    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "d-flex align-items-center justify-content-center",
            "text-center" if c_text_center else "",
            user_cls,
        )
    }
    if styles or user_style:
        attrs["style"] = _merge_style(" ".join(styles), user_style)
    attrs.update(convert_attrs(kwargs))
    return Div(*children, **attrs)
