"""Bootstrap Navbar component for site navigation."""

from __future__ import annotations

from typing import Any

from fasthtml.common import A, Button, Div, Nav, Span

from ...core._ids import next_sequential_id
from ...core._stability import stable
from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import UNSET, resolve_defaults
from ...core.types import ExpandType
from ...utils.attrs import convert_attrs


def _get_next_navbar_id() -> str:
    """Generate deterministic navbar ID for collapse toggler.

    Returns:
        Unique navbar ID string (e.g., 'navbar1', 'navbar2', etc.)
    """
    return next_sequential_id("navbar")


def _normalize_nav_item(item: Any) -> Any:
    """Normalize simple navbar items into Bootstrap nav-item/nav-link markup."""
    if isinstance(item, str):
        return Div(A(item, href="#", cls="nav-link"), cls="nav-item")

    if isinstance(item, tuple):
        text = item[0] if len(item) > 0 else ""
        href = item[1] if len(item) > 1 else "#"
        active = bool(item[2]) if len(item) > 2 else False
        link_cls = "nav-link active" if active else "nav-link"
        tuple_link_attrs: dict[str, Any] = {"href": href, "cls": link_cls}
        if active:
            tuple_link_attrs["aria_current"] = "page"
        return Div(A(text, **tuple_link_attrs), cls="nav-item")

    if isinstance(item, dict):
        text = item.get("text", "")
        href = item.get("href", "#")
        active = bool(item.get("active", False))
        disabled = bool(item.get("disabled", False))
        nav_item_cls = merge_classes("nav-item", item.get("item_cls", ""))
        link_cls = merge_classes("nav-link", item.get("cls", ""))
        if active:
            link_cls = merge_classes(link_cls, "active")
        if disabled:
            link_cls = merge_classes(link_cls, "disabled")

        dict_link_attrs: dict[str, Any] = {"href": href, "cls": link_cls}
        if active:
            dict_link_attrs["aria_current"] = "page"
        if disabled:
            dict_link_attrs["aria_disabled"] = "true"
            dict_link_attrs["tabindex"] = "-1"

        return Div(A(text, **dict_link_attrs), cls=nav_item_cls)

    if getattr(item, "tag", None) == "a":
        classes = str(
            getattr(item, "attrs", {}).get("class") or getattr(item, "attrs", {}).get("cls") or ""
        )
        if "nav-link" not in classes:
            classes = merge_classes(classes, "nav-link")
            item.attrs["cls"] = classes
        return Div(item, cls="nav-item")

    return item


def _is_simple_nav_item(item: Any) -> bool:
    """Return True when the item can be normalized into standard navbar navigation markup."""
    return isinstance(item, (str, tuple, dict)) or getattr(item, "tag", None) == "a"


def _group_nav_items(items: list[Any]) -> list[Any]:
    """Group simple items into a navbar-nav wrapper while preserving custom content."""
    grouped: list[Any] = []
    simple_buffer: list[Any] = []

    def flush_simple_items() -> None:
        if not simple_buffer:
            return
        grouped.append(Div(*simple_buffer, cls="navbar-nav"))
        simple_buffer.clear()

    for item in items:
        normalized = _normalize_nav_item(item)
        if _is_simple_nav_item(item):
            simple_buffer.append(normalized)
        else:
            flush_simple_items()
            grouped.append(normalized)

    flush_simple_items()
    return grouped


@stable
@register(category="navigation", requires_js=True)
def Navbar(
    *children: Any,
    items: list[Any] | None = None,
    brand: Any | None = None,
    brand_href: str = "/",
    variant: str | None = UNSET,
    color_scheme: str | None = UNSET,
    bg: str | None = UNSET,
    expand: ExpandType | None = UNSET,
    sticky: str | None = UNSET,
    fixed: str | None = UNSET,
    container: bool | str | None = UNSET,
    **kwargs: Any,
) -> Nav:
    """Bootstrap Navbar component for responsive site navigation.

    Args:
        *children: Navbar content
        items: Navbar items list (links, buttons, etc.)
        brand: Brand text or logo
        brand_href: Brand link URL (default: "/")
        variant: Color scheme alias (light or dark text)
        color_scheme: Color scheme (light or dark text)
        bg: Background color class
        expand: Breakpoint where navbar expands
        sticky: Stick to top or bottom
        fixed: Fix to top or bottom
        container: Wrap in container
        **kwargs: Additional HTML attributes
    """
    # Resolve API defaults
    cfg = resolve_defaults(
        "Navbar",
        variant=variant,
        color_scheme=color_scheme,
        bg=bg,
        expand=expand,
        sticky=sticky,
        fixed=fixed,
        container=container,
    )

    # Use color_scheme (with variant as fallback)
    # Priority: 1. explicit color_scheme, 2. explicit variant, 3. global default
    if color_scheme is not UNSET:
        c_scheme = color_scheme
    elif variant is not UNSET:
        c_scheme = variant
    else:
        c_scheme = cfg.get("color_scheme") or cfg.get("variant", "light")

    c_bg = cfg.get("bg")
    c_expand = cfg.get("expand", "lg")
    c_sticky = cfg.get("sticky")
    c_fixed = cfg.get("fixed")
    c_container = cfg.get("container", True)

    # Build navbar classes
    classes = ["navbar"]

    # Add expand class
    if c_expand is True:
        classes.append("navbar-expand")
    elif isinstance(c_expand, str) and c_expand not in ("never", "false"):
        if c_expand == "always":
            classes.append("navbar-expand")
        else:
            classes.append(f"navbar-expand-{c_expand}")

    # Add variant/color-scheme
    if c_scheme:
        classes.append(f"navbar-{c_scheme}")

    # Add background
    if c_bg:
        classes.append(f"bg-{c_bg}")

    # Add sticky/fixed positioning
    if c_sticky:
        classes.append(f"sticky-{c_sticky}")
    elif c_fixed:
        classes.append(f"fixed-{c_fixed}")

    # Merge with user classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(classes), user_cls)

    # Build attributes
    root_id = kwargs.pop("id", None)
    attrs: dict[str, Any] = {"cls": all_classes}
    if root_id:
        attrs["id"] = root_id
    attrs.update(convert_attrs(kwargs))

    # Build navbar content
    parts = []

    # Merge *children and items
    nav_content = list(children)
    if items:
        nav_content.extend(_group_nav_items(items))

    # Wrap in container if requested
    if c_container:
        container_cls = "container" if c_container is True else f"container-{c_container}"

        # Build container content
        container_parts = []

        # Brand
        if brand:
            brand_elem = A(brand, cls="navbar-brand", href=brand_href)
            container_parts.append(brand_elem)

        # Toggler for mobile (collapse button)
        if c_expand:
            suffix = _get_next_navbar_id()
            toggler_id = f"{root_id}-{suffix}-collapse" if root_id else suffix

            toggler = Button(
                Span(cls="navbar-toggler-icon"),
                cls="navbar-toggler",
                type="button",
                data_bs_toggle="collapse",
                data_bs_target=f"#{toggler_id}",
                aria_controls=toggler_id,
                aria_expanded="false",
                aria_label="Toggle navigation",
            )
            container_parts.append(toggler)

            # Collapsible content
            collapse = Div(*nav_content, cls="collapse navbar-collapse", id=toggler_id)
            container_parts.append(collapse)
        else:
            # No collapse, just add children directly
            container_parts.extend(nav_content)

        parts.append(Div(*container_parts, cls=container_cls))
    else:
        # No container wrapper
        if brand:
            parts.append(A(brand, cls="navbar-brand", href=brand_href))

        if c_expand:
            # Still need collapse for mobile
            suffix = _get_next_navbar_id()
            toggler_id = f"{root_id}-{suffix}-collapse" if root_id else suffix

            toggler = Button(
                Span(cls="navbar-toggler-icon"),
                cls="navbar-toggler",
                type="button",
                data_bs_toggle="collapse",
                data_bs_target=f"#{toggler_id}",
                aria_controls=toggler_id,
                aria_expanded="false",
                aria_label="Toggle navigation",
            )
            parts.append(toggler)

            collapse = Div(*nav_content, cls="collapse navbar-collapse", id=toggler_id)
            parts.append(collapse)
        else:
            parts.extend(nav_content)

    return Nav(*parts, **attrs)
