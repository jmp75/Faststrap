"""Structured display primitives for data, code, and records."""

from __future__ import annotations

import json
from collections.abc import Mapping, Sequence
from typing import Any

from fasthtml.common import H3, Code, Div, P, Pre, Span, ft

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs
from .card import Card

KeyValueItems = Mapping[str, Any] | Sequence[tuple[str, Any]] | Sequence[Mapping[str, Any]]


def _normalize_items(items: KeyValueItems) -> list[tuple[str, Any]]:
    if isinstance(items, Mapping):
        return [(str(key), value) for key, value in items.items()]

    normalized: list[tuple[str, Any]] = []
    for item in items:
        if isinstance(item, Mapping):
            label = item.get("label", item.get("key", ""))
            value = item.get("value", "")
            normalized.append((str(label), value))
        else:
            label, value = item
            normalized.append((str(label), value))
    return normalized


@register(category="display")
@beta
def KeyValueList(
    items: KeyValueItems,
    *,
    striped: bool = False,
    compact: bool = False,
    **kwargs: Any,
) -> Div:
    """Render label/value metadata rows."""
    user_cls = kwargs.pop("cls", "")
    row_cls = "py-1" if compact else "py-2"
    rows = []
    for index, (label, value) in enumerate(_normalize_items(items)):
        rows.append(
            Div(
                Div(label, cls="fw-semibold text-muted"),
                Div(value, cls="text-body"),
                cls=merge_classes(
                    "d-grid gap-1 gap-sm-3 border-bottom",
                    row_cls,
                    "bg-body-tertiary px-2" if striped and index % 2 else "",
                ),
                style="grid-template-columns: minmax(9rem, 0.35fr) 1fr;",
            )
        )

    attrs: dict[str, Any] = {"cls": merge_classes("faststrap-key-value-list", user_cls)}
    attrs.update(convert_attrs(kwargs))
    return Div(*rows, **attrs)


@register(category="display")
@beta
def RecordDetail(
    items: KeyValueItems,
    *,
    title: str | None = None,
    subtitle: str | None = None,
    actions: Any | list[Any] | tuple[Any, ...] | None = None,
    **kwargs: Any,
) -> Div:
    """Render a card-style detail view for one record."""
    user_cls = kwargs.pop("cls", "")

    header_children: list[Any] = []
    if title:
        header_children.append(H3(title, cls="h5 mb-1"))
    if subtitle:
        header_children.append(P(subtitle, cls="text-muted mb-0"))

    header: Any | None = None
    if header_children or actions is not None:
        action_children: list[Any] = []
        if actions is not None:
            action_children = list(actions) if isinstance(actions, (list, tuple)) else [actions]
        header = Div(
            Div(*header_children),
            Div(*action_children, cls="d-flex flex-wrap gap-2") if action_children else "",
            cls="d-flex flex-column flex-sm-row justify-content-between gap-3",
        )

    attrs: dict[str, Any] = {"cls": merge_classes("faststrap-record-detail", user_cls)}
    attrs.update(convert_attrs(kwargs))
    return Card(KeyValueList(items), header=header, **attrs)


@register(category="display")
@beta
def CodeBlock(
    code: str,
    *,
    language: str | None = None,
    filename: str | None = None,
    copy: bool = False,
    wrap: bool = False,
    **kwargs: Any,
) -> Div:
    """Render escaped source code in a Bootstrap-styled block."""
    user_cls = kwargs.pop("cls", "")
    code_cls = f"language-{language}" if language else ""

    header = None
    if filename or copy:
        header = Div(
            Span(filename or "Code", cls="fw-semibold small text-muted"),
            Span("Copy", cls="badge text-bg-secondary") if copy else "",
            cls="d-flex align-items-center justify-content-between border-bottom px-3 py-2",
        )

    pre_cls = merge_classes("mb-0 p-3", "text-wrap" if wrap else "overflow-auto")
    attrs: dict[str, Any] = {
        "cls": merge_classes("faststrap-code-block border rounded bg-body-tertiary", user_cls)
    }
    attrs.update(convert_attrs(kwargs))
    return Div(header or "", Pre(Code(code, cls=code_cls), cls=pre_cls), **attrs)


@register(category="display")
@beta
def JsonViewer(
    data: Any,
    *,
    title: str | None = None,
    expanded: bool = True,
    **kwargs: Any,
) -> Any:
    """Render JSON-like data as an escaped, readable details block."""
    rendered = json.dumps(data, indent=2, sort_keys=True, default=str)
    block = CodeBlock(rendered, language="json")
    if title is None:
        user_cls = kwargs.pop("cls", "")
        attrs: dict[str, Any] = {"cls": merge_classes("faststrap-json-viewer", user_cls)}
        attrs.update(convert_attrs(kwargs))
        return Div(block, **attrs)

    user_cls = kwargs.pop("cls", "")
    attrs = {"cls": merge_classes("faststrap-json-viewer", user_cls)}
    if expanded:
        attrs["open"] = True
    attrs.update(convert_attrs(kwargs))
    return ft("details", ft("summary", title, cls="fw-semibold mb-2"), block, **attrs)
