"""Feature Pattern Components."""

from typing import Any

from fasthtml.common import H3, Div, I, P

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs
from ..layout.grid import Col, Row


@register(category="patterns")
@beta
def Feature(
    title: str,
    description: str,
    icon: str | Any | None = None,
    icon_cls: str = "bg-primary text-white",
    icon_wrapper_cls: str | None = None,
    title_cls: str = "fs-4 fw-bold",
    description_cls: str = "text-muted",
    icon_wrapper_attrs: dict[str, Any] | None = None,
    title_attrs: dict[str, Any] | None = None,
    description_attrs: dict[str, Any] | None = None,
    **kwargs: Any,
) -> Div:
    """A single feature item with icon, title, and description.

    Args:
        title: Feature title
        description: Feature description
        icon: Bootstrap icon name or custom element
        icon_cls: CSS classes for icon container
        icon_wrapper_cls: Additional classes for the icon wrapper
        title_cls: Additional classes for the title element
        description_cls: Additional classes for the description element
        icon_wrapper_attrs: Extra attributes for the icon wrapper
        title_attrs: Extra attributes for the title element
        description_attrs: Extra attributes for the description element
        **kwargs: Additional attributes

    Returns:
        Div with feature content

    Note:
        Marked as @beta - API may change in future releases.
    """
    icon_wrapper_attrs = convert_attrs(dict(icon_wrapper_attrs or {}))
    title_attrs = convert_attrs(dict(title_attrs or {}))
    description_attrs = convert_attrs(dict(description_attrs or {}))

    icon_el = None
    if isinstance(icon, str):
        icon_el = Div(
            I(cls=f"bi bi-{icon}"),
            cls=merge_classes(
                "feature-icon", icon_cls, icon_wrapper_cls, icon_wrapper_attrs.pop("cls", "")
            ),
            **icon_wrapper_attrs,
        )
    elif icon:
        icon_el = Div(
            icon,
            cls=merge_classes(
                "feature-icon", icon_cls, icon_wrapper_cls, icon_wrapper_attrs.pop("cls", "")
            ),
            **icon_wrapper_attrs,
        )

    return Div(
        icon_el,
        H3(title, cls=merge_classes(title_cls, title_attrs.pop("cls", "")), **title_attrs),
        P(
            description,
            cls=merge_classes(description_cls, description_attrs.pop("cls", "")),
            **description_attrs,
        ),
        cls=merge_classes("feature-item", kwargs.pop("cls", "")),
        **kwargs,
    )


@register(category="patterns")
@beta
def FeatureGrid(
    *features: Any,
    columns: int = 3,
    row_cls: str | None = None,
    col_cls: str | None = None,
    row_attrs: dict[str, Any] | None = None,
    col_attrs: dict[str, Any] | None = None,
    **kwargs: Any,
) -> Div:
    """Grid layout for multiple feature items.

    Args:
        *features: Feature components
        columns: Number of columns (default: 3)
        row_cls: Additional classes for the row wrapper
        col_cls: Additional classes for each column wrapper
        row_attrs: Extra attributes for the row wrapper
        col_attrs: Extra attributes for each column wrapper
        **kwargs: Additional attributes

    Returns:
        Div with responsive feature grid

    Note:
        Marked as @beta - API may change in future releases.
    """
    row_attrs = convert_attrs(dict(row_attrs or {}))
    col_attrs = convert_attrs(dict(col_attrs or {}))

    col_size = 12 // columns
    cols = []
    for feat in features:
        current_col_attrs = dict(col_attrs)
        cols.append(
            Col(
                feat,
                md=col_size,
                cls=merge_classes("mb-4", col_cls, current_col_attrs.pop("cls", "")),
                **current_col_attrs,
            )
        )

    return Div(
        Row(*cols, cls=merge_classes(row_cls, row_attrs.pop("cls", "")), **row_attrs),
        cls=merge_classes("feature-grid", kwargs.pop("cls", "")),
        **kwargs,
    )
