"""Server-rendered command palette components."""

from __future__ import annotations

from typing import Any, Literal

from fasthtml.common import A, Div, Kbd, Span
from fasthtml.common import Form as FTForm
from fasthtml.common import Input as FTInput

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs
from ...utils.icons import Icon

CommandPaletteMethod = Literal["get", "post"]


@register(category="navigation")
@beta
def CommandItem(
    label: str,
    *,
    href: str | None = None,
    description: str | None = None,
    icon: str | None = None,
    shortcut: str | None = None,
    active: bool = False,
    **kwargs: Any,
) -> Div | A:
    """Render one command in a command palette."""
    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes(
            "faststrap-command-item d-flex align-items-center gap-3 px-3 py-2 rounded",
            "active" if active else "",
            user_cls,
        ),
        "data_fs_command_item": "true",
    }
    attrs.update(convert_attrs(kwargs))

    content = [
        Icon(icon, cls="text-muted", aria_hidden="true") if icon else "",
        Div(
            Span(label, cls="fw-semibold d-block"),
            Span(description, cls="small text-muted") if description else "",
            cls="flex-grow-1 min-w-0",
        ),
        Kbd(shortcut, cls="small") if shortcut else "",
    ]
    if href:
        return A(*content, href=href, **attrs)
    return Div(*content, **attrs)


@register(category="navigation")
@beta
def CommandPalette(
    *commands: Any,
    name: str = "q",
    placeholder: str = "Search commands...",
    endpoint: str | None = None,
    method: CommandPaletteMethod = "get",
    title: str | None = "Command palette",
    empty: Any | None = None,
    hx_target: str | None = None,
    hx_swap: str = "innerHTML",
    **kwargs: Any,
) -> Div:
    """Render a command/search palette with an HTMX-friendly search form."""
    if method not in {"get", "post"}:
        msg = f"method must be 'get' or 'post', got {method!r}"
        raise ValueError(msg)

    user_cls = kwargs.pop("cls", "")
    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-command-palette card shadow-sm", user_cls),
        "data_fs_command_palette": "true",
    }
    attrs.update(convert_attrs(kwargs))

    results_id = attrs.get("id", "command-palette")
    target = hx_target or f"#{results_id}-results"
    form_attrs: dict[str, Any] = {
        "method": method,
        "cls": "faststrap-command-palette-form border-bottom p-3",
        "role": "search",
    }
    if endpoint:
        form_attrs["action"] = endpoint
        form_attrs[f"hx_{method}"] = endpoint
        form_attrs["hx_target"] = target
        form_attrs["hx_swap"] = hx_swap
        form_attrs["hx_trigger"] = "input changed delay:200ms, search"

    query_input = FTInput(
        type="search",
        name=name,
        placeholder=placeholder,
        cls="form-control",
        autocomplete="off",
        aria_label=placeholder,
    )
    results = Div(
        *(commands or ([empty] if empty is not None else [])),
        id=f"{results_id}-results",
        cls="faststrap-command-palette-results d-grid gap-1 p-2",
    )

    body = [
        Div(title, cls="card-header fw-semibold") if title else "",
        FTForm(query_input, **convert_attrs(form_attrs)),
        results,
    ]
    return Div(*body, **attrs)
