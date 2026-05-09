"""Bootstrap Pagination component for page navigation."""

from __future__ import annotations

from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

from fasthtml.common import A, Li, Nav, Span, Ul

from ...core.base import merge_classes
from ...core.registry import register
from ...core.theme import UNSET, resolve_defaults
from ...core.types import AlignType, SizeType
from ...utils.attrs import convert_attrs


def _page_href(
    base_url: str,
    page: int,
    *,
    page_param: str,
    query_params: dict[str, Any] | None,
) -> str:
    split = urlsplit(base_url)
    params = dict(parse_qsl(split.query, keep_blank_values=True))
    if query_params:
        params.update({key: value for key, value in query_params.items() if value is not None})
    params[page_param] = str(page)
    query = urlencode(params, doseq=True)
    return urlunsplit((split.scheme, split.netloc, split.path, query, split.fragment))


def _htmx_attrs(
    href: str,
    *,
    htmx: bool,
    hx_target: str | None,
    hx_swap: str | None,
    hx_push_url: bool,
) -> dict[str, Any]:
    if not htmx:
        return {}

    attrs: dict[str, Any] = {"hx_get": href}
    if hx_target:
        attrs["hx_target"] = hx_target
    if hx_swap:
        attrs["hx_swap"] = hx_swap
    if hx_push_url:
        attrs["hx_push_url"] = "true"
    return attrs


@register(category="navigation")
def Pagination(
    current_page: int,
    total_pages: int,
    size: SizeType | None = UNSET,
    align: AlignType | None = UNSET,
    max_pages: int | None = UNSET,
    base_url: str | None = UNSET,
    show_first_last: bool | None = UNSET,
    show_prev_next: bool | None = UNSET,
    page_param: str = "page",
    query_params: dict[str, Any] | None = None,
    htmx: bool = False,
    hx_target: str | None = None,
    hx_swap: str | None = "outerHTML",
    hx_push_url: bool = False,
    **kwargs: Any,
) -> Nav:
    """Bootstrap Pagination component for page navigation.

    Args:
        current_page: Current active page (1-indexed)
        total_pages: Total number of pages
        size: Pagination size (sm, lg)
        align: Alignment (start, center, end)
        max_pages: Maximum page numbers to show
        base_url: Base URL for page links
        show_first_last: Show first/last page buttons
        show_prev_next: Show previous/next buttons
        page_param: Query-string parameter used for page links
        query_params: Extra query parameters to preserve
        htmx: Add hx-get attributes to generated page links
        hx_target: Optional HTMX target for nav and generated links
        hx_swap: Optional HTMX swap mode for generated links
        hx_push_url: Push generated URLs when HTMX links are clicked
        **kwargs: Additional HTML attributes
    """
    cfg = resolve_defaults(
        "Pagination",
        size=size,
        align=align,
        max_pages=max_pages,
        base_url=base_url,
        show_first_last=show_first_last,
        show_prev_next=show_prev_next,
    )

    c_size = cfg.get("size")
    c_align = cfg.get("align", "start")
    c_max_pages = cfg.get("max_pages", 5)
    c_base_url = cfg.get("base_url", "#")
    c_show_first_last = cfg.get("show_first_last", False)
    c_show_prev_next = cfg.get("show_prev_next", True)

    classes = ["pagination"]
    if c_size:
        classes.append(f"pagination-{c_size}")

    justify_class = {
        "center": "justify-content-center",
        "end": "justify-content-end",
    }.get(c_align)

    user_cls = kwargs.pop("cls", "")
    ul_cls = merge_classes(" ".join(classes), user_cls)

    safe_total = max(1, total_pages)
    safe_current = max(1, min(current_page, safe_total))
    safe_max_pages = max(1, c_max_pages)

    half = safe_max_pages // 2
    start = max(1, safe_current - half)
    end = min(safe_total, start + safe_max_pages - 1)
    if end == safe_total:
        start = max(1, end - safe_max_pages + 1)

    def href_for(page: int) -> str:
        return _page_href(
            c_base_url,
            page,
            page_param=page_param,
            query_params=query_params,
        )

    def link_attrs(href: str) -> dict[str, Any]:
        return _htmx_attrs(
            href,
            htmx=htmx,
            hx_target=hx_target,
            hx_swap=hx_swap,
            hx_push_url=hx_push_url,
        )

    links: list[Any] = []

    if c_show_first_last and safe_current > 1:
        href = href_for(1)
        links.append(
            Li(
                A("<<", href=href, cls="page-link", aria_label="First", **link_attrs(href)),
                cls="page-item",
            )
        )

    if c_show_prev_next:
        prev_disabled = safe_current == 1
        prev_page = max(1, safe_current - 1)
        href = href_for(prev_page)
        links.append(
            Li(
                (
                    A(
                        "<",
                        href=href,
                        cls="page-link",
                        aria_label="Previous",
                        **link_attrs(href),
                    )
                    if not prev_disabled
                    else Span("<", cls="page-link", aria_hidden="true")
                ),
                cls="page-item" + (" disabled" if prev_disabled else ""),
            )
        )

    for page in range(start, end + 1):
        active = page == safe_current
        href = href_for(page)
        links.append(
            Li(
                (
                    A(str(page), href=href, cls="page-link", **link_attrs(href))
                    if not active
                    else Span(str(page), cls="page-link")
                ),
                cls="page-item" + (" active" if active else ""),
                aria_current="page" if active else None,
            )
        )

    if c_show_prev_next:
        next_disabled = safe_current == safe_total
        next_page = min(safe_total, safe_current + 1)
        href = href_for(next_page)
        links.append(
            Li(
                (
                    A(">", href=href, cls="page-link", aria_label="Next", **link_attrs(href))
                    if not next_disabled
                    else Span(">", cls="page-link", aria_hidden="true")
                ),
                cls="page-item" + (" disabled" if next_disabled else ""),
            )
        )

    if c_show_first_last and safe_current < safe_total:
        href = href_for(safe_total)
        links.append(
            Li(
                A(">>", href=href, cls="page-link", aria_label="Last", **link_attrs(href)),
                cls="page-item",
            )
        )

    ul = Ul(*links, cls=ul_cls)

    nav_attrs: dict[str, Any] = {"aria_label": "Page navigation"}
    if hx_target:
        nav_attrs["hx_target"] = hx_target
    nav_attrs.update(convert_attrs(kwargs))

    return Nav(ul, cls=justify_class, **nav_attrs)
