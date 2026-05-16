"""Additional CSS-only loading indicators."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import Div, Span, Svg, ft

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import UNSET, resolve_defaults
from ...utils.attrs import convert_attrs

LoaderSize = Literal["sm", "md", "lg"]


def _variant_style(variant: str | None) -> str | None:
    if not variant or variant == "primary":
        return None
    return f"--faststrap-loader-color: var(--bs-{variant});"


@register(category="feedback")
@beta
def DotsLoader(
    *,
    variant: str | None = UNSET,
    label: str | None = UNSET,
    **kwargs: Any,
) -> Div:
    """Render a three-dot loading animation."""
    cfg = resolve_defaults("DotsLoader", variant=variant, label=label)
    c_variant = cfg.get("variant") or "primary"
    c_label = cfg.get("label") or "Loading..."

    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-dots-loader", user_cls),
        "role": "status",
        "aria_label": c_label,
    }
    style = _variant_style(c_variant)
    if style:
        attrs["style"] = style
    attrs.update(convert_attrs(kwargs))

    return Div(Div(), Div(), Div(), Span(c_label, cls="visually-hidden"), **attrs)


@register(category="feedback")
@beta
def RingLoader(
    *,
    variant: str | None = UNSET,
    size: str | None = UNSET,
    label: str | None = UNSET,
    **kwargs: Any,
) -> Div:
    """Render a spinning ring loading animation."""
    cfg = resolve_defaults("RingLoader", variant=variant, size=size, label=label)
    c_variant = cfg.get("variant") or "primary"
    c_size = cfg.get("size") or "64px"
    c_label = cfg.get("label") or "Loading..."

    user_cls = kwargs.pop("cls", "")
    user_style = kwargs.pop("style", "")
    styles = [f"width: {c_size}; height: {c_size};"]
    variant_style = _variant_style(c_variant)
    if variant_style:
        styles.append(variant_style)
    if isinstance(user_style, str) and user_style.strip():
        styles.append(user_style.strip())

    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-ring-loader", user_cls),
        "style": " ".join(styles),
        "role": "status",
        "aria_label": c_label,
    }
    attrs.update(convert_attrs(kwargs))

    return Div(Div(), Div(), Div(), Div(), Span(c_label, cls="visually-hidden"), **attrs)


@register(category="feedback")
@beta
def WaveLoader(
    *,
    variant: str | None = UNSET,
    label: str | None = UNSET,
    **kwargs: Any,
) -> Div:
    """Render a vertical wave loading animation."""
    cfg = resolve_defaults("WaveLoader", variant=variant, label=label)
    c_variant = cfg.get("variant") or "primary"
    c_label = cfg.get("label") or "Loading..."

    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-wave-loader", user_cls),
        "role": "status",
        "aria_label": c_label,
    }
    style = _variant_style(c_variant)
    if style:
        attrs["style"] = style
    attrs.update(convert_attrs(kwargs))

    bars = [
        Div(cls="faststrap-wave-bar", style=f"animation-delay: {index * 0.1}s;")
        for index in range(5)
    ]
    return Div(*bars, Span(c_label, cls="visually-hidden"), **attrs)


@register(category="feedback")
@beta
def PulseLoader(
    *,
    variant: str | None = UNSET,
    size: LoaderSize | None = UNSET,
    label: str | None = UNSET,
    **kwargs: Any,
) -> Div:
    """Render a pulsing circle loading animation."""
    cfg = resolve_defaults("PulseLoader", variant=variant, size=size, label=label)
    c_variant = cfg.get("variant") or "primary"
    c_size = cfg.get("size") or "md"
    c_label = cfg.get("label") or "Loading..."

    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-pulse-loader", f"pulse-{c_size}", user_cls),
        "role": "status",
        "aria_label": c_label,
    }
    style = _variant_style(c_variant)
    if style:
        attrs["style"] = style
    attrs.update(convert_attrs(kwargs))
    return Div(Div(cls="faststrap-pulse-circle"), Span(c_label, cls="visually-hidden"), **attrs)


@register(category="feedback")
@beta
def PolygonLoader(*, label: str | None = UNSET, **kwargs: Any) -> Div:
    """Render a shape-shifting polygon loading animation."""
    cfg = resolve_defaults("PolygonLoader", label=label)
    c_label = cfg.get("label") or "Loading..."

    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-polygon-loader", user_cls),
        "role": "status",
        "aria_label": c_label,
    }
    attrs.update(convert_attrs(kwargs))
    return Div(Span(c_label, cls="visually-hidden"), **attrs)


@register(category="feedback")
@beta
def TypewriterLoader(text: str = "Loading...", **kwargs: Any) -> Div:
    """Render a typewriter-style text loading animation."""
    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-typewriter-loader", user_cls),
        "data_text": text,
        "role": "status",
        "aria_label": text,
    }
    attrs.update(convert_attrs(kwargs))
    return Div(**attrs)


@register(category="feedback")
@beta
def ShadowLoader(text: str = "Loading...", **kwargs: Any) -> Div:
    """Render a bouncing shadow text loading animation."""
    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-shadow-loader", user_cls),
        "data_text": text,
        "role": "status",
        "aria_label": text,
    }
    attrs.update(convert_attrs(kwargs))
    return Div(**attrs)


@register(category="feedback")
@beta
def ProgressRing(
    value: int | float,
    *,
    max_value: int | float = 100,
    size: str | None = UNSET,
    variant: str | None = UNSET,
    show_text: bool | None = UNSET,
    label: str | None = UNSET,
    **kwargs: Any,
) -> Div:
    """Render a circular SVG progress indicator."""
    cfg = resolve_defaults(
        "ProgressRing",
        size=size,
        variant=variant,
        show_text=show_text,
        label=label,
    )
    c_size = cfg.get("size") or "4rem"
    c_variant = cfg.get("variant") or "primary"
    c_show_text = cfg.get("show_text", True)

    safe_max = max(float(max_value), 1.0)
    percentage = min(100.0, max(0.0, (float(value) / safe_max) * 100.0))
    radius = 45
    circumference = 2 * 3.14159 * radius
    stroke_offset = circumference - (percentage / 100.0) * circumference
    accessible_label = cfg.get("label") or f"{int(percentage)}% complete"

    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-progress-ring", user_cls),
        "role": "progressbar",
        "aria_label": accessible_label,
        "aria_valuemin": "0",
        "aria_valuemax": str(max_value),
        "aria_valuenow": str(value),
    }
    attrs.update(convert_attrs(kwargs))

    svg = Svg(
        ft(
            "circle",
            cx="50",
            cy="50",
            r=str(radius),
            fill="none",
            stroke="var(--bs-border-color)",
            stroke_width="8",
        ),
        ft(
            "circle",
            cx="50",
            cy="50",
            r=str(radius),
            fill="none",
            stroke=f"var(--bs-{c_variant})",
            stroke_width="8",
            stroke_dasharray=str(circumference),
            stroke_dashoffset=str(stroke_offset),
            stroke_linecap="round",
            transform="rotate(-90 50 50)",
            cls="faststrap-progress-ring-value",
        ),
        viewBox="0 0 100 100",
        style=f"width: {c_size}; height: {c_size};",
        aria_hidden="true",
    )

    children: list[Any] = [svg]
    if c_show_text:
        children.append(
            Div(
                f"{int(percentage)}%",
                cls="position-absolute top-50 start-50 translate-middle fw-bold",
                style="font-size: 0.875rem;",
            )
        )

    return Div(*children, **attrs)
