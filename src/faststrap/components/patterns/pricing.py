"""Pricing Pattern Components."""

from typing import Any

from fasthtml.common import H2, H3, Div, Li, P, Span, Ul

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs
from ..display.card import Card
from ..forms.button import Button
from ..layout.grid import Col, Row


@register(category="patterns")
@beta
def PricingTier(
    name: str,
    price: str | int,
    period: str = "month",
    features: list[str] | None = None,
    button_text: str = "Get Started",
    button_href: str = "#",
    highlighted: bool = False,
    **kwargs: Any,
) -> Any:
    """A single pricing tier card.

    Args:
        name: Tier name (e.g., "Pro", "Enterprise")
        price: Price amount
        period: Billing period (e.g., "month", "year")
        features: List of feature strings
        button_text: CTA button text
        button_href: CTA button link
        highlighted: Whether to highlight this tier
        **kwargs: Additional attributes

    Returns:
        Card component with pricing content

    Note:
        Marked as @beta - API may change in future releases.
    """
    if features is None:
        features = []

    # Build feature list
    feature_items = [Li(feat) for feat in features]
    feature_list = Ul(*feature_items, cls="list-unstyled")

    # Build price display
    price_display = Div(
        Span("$", cls="fs-4"),
        Span(str(price), cls="display-4 fw-bold"),
        Span(f"/{period}", cls="text-muted"),
        cls="mb-4",
    )

    # Build CTA button
    cta_button = Button(
        button_text,
        href=button_href,
        variant="primary",
        outline=not highlighted,
        size="lg",
        cls="w-100",
    )

    # Build card
    card_cls = "h-100 text-center"
    if highlighted:
        card_cls += " border-primary shadow-lg"

    return Card(
        H3(name, cls="card-title"),
        price_display,
        feature_list,
        cta_button,
        cls=card_cls,
        **kwargs,
    )


@register(category="patterns")
@beta
def PricingGroup(
    *tiers: Any,
    title: str = "Choose Your Plan",
    subtitle: str | None = None,
    header_cls: str | None = None,
    title_cls: str | None = None,
    subtitle_cls: str | None = None,
    row_cls: str | None = None,
    col_cls: str | None = None,
    header_attrs: dict[str, Any] | None = None,
    title_attrs: dict[str, Any] | None = None,
    subtitle_attrs: dict[str, Any] | None = None,
    row_attrs: dict[str, Any] | None = None,
    col_attrs: dict[str, Any] | None = None,
    **kwargs: Any,
) -> Div:
    """Group of pricing tiers in a responsive grid.

    Args:
        *tiers: PricingTier components
        title: Section title
        subtitle: Optional subtitle
        header_cls: Additional classes for the section header
        title_cls: Additional classes for the title element
        subtitle_cls: Additional classes for the subtitle element
        row_cls: Additional classes for the row wrapper
        col_cls: Additional classes for each column wrapper
        header_attrs: Extra attributes for the section header
        title_attrs: Extra attributes for the title element
        subtitle_attrs: Extra attributes for the subtitle element
        row_attrs: Extra attributes for the row wrapper
        col_attrs: Extra attributes for each column wrapper
        **kwargs: Additional attributes

    Returns:
        Div with pricing tiers in grid

    Note:
        Marked as @beta - API may change in future releases.
    """
    header_attrs = convert_attrs(dict(header_attrs or {}))
    title_attrs = convert_attrs(dict(title_attrs or {}))
    subtitle_attrs = convert_attrs(dict(subtitle_attrs or {}))
    row_attrs = convert_attrs(dict(row_attrs or {}))
    col_attrs = convert_attrs(dict(col_attrs or {}))

    # Build header
    header = Div(
        H2(
            title,
            cls=merge_classes("text-center mb-2", title_cls, title_attrs.pop("cls", "")),
            **title_attrs,
        ),
        (
            P(
                subtitle,
                cls=merge_classes(
                    "text-center text-muted mb-5",
                    subtitle_cls,
                    subtitle_attrs.pop("cls", ""),
                ),
                **subtitle_attrs,
            )
            if subtitle
            else None
        ),
        cls=merge_classes(header_cls, header_attrs.pop("cls", "")),
        **header_attrs,
    )

    # Build tier grid
    col_size = 12 // len(tiers) if tiers else 12
    cols = []
    for tier in tiers:
        current_col_attrs = dict(col_attrs)
        cols.append(
            Col(
                tier,
                md=col_size,
                cls=merge_classes("mb-4", col_cls, current_col_attrs.pop("cls", "")),
                **current_col_attrs,
            )
        )

    return Div(
        header,
        Row(*cols, cls=merge_classes(row_cls, row_attrs.pop("cls", "")), **row_attrs),
        cls=merge_classes("pricing-group py-5", kwargs.pop("cls", "")),
        **kwargs,
    )
