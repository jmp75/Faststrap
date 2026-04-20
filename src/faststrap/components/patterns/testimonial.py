"""Testimonial Pattern Components.

Customer testimonial cards and sections for social proof.
"""

from typing import Any

from fasthtml.common import Blockquote, Div, Img, P, Span

from ...core._stability import beta
from ...core.base import merge_classes
from ...core.registry import register
from ...utils.attrs import convert_attrs
from ..display.card import Card


@register(category="patterns")
@beta
def Testimonial(
    quote: str,
    author: str,
    role: str | None = None,
    avatar: str | None = None,
    rating: int | None = None,
    **kwargs: Any,
) -> Any:
    """Single testimonial card with quote, author, and optional avatar/rating.

    Args:
        quote: Testimonial quote text
        author: Author name
        role: Author's role/title (optional)
        avatar: URL to author's avatar image (optional)
        rating: Star rating out of 5 (optional)
        **kwargs: Additional HTML attributes

    Returns:
        Card component with testimonial content

    Example:
        Basic testimonial:
        >>> Testimonial(
        ...     quote="This product changed my life!",
        ...     author="John Doe",
        ...     role="CEO, Acme Corp"
        ... )

        With avatar and rating:
        >>> Testimonial(
        ...     quote="Absolutely amazing experience.",
        ...     author="Jane Smith",
        ...     role="Designer",
        ...     avatar="/static/avatars/jane.jpg",
        ...     rating=5
        ... )

    Note:
        Marked as @beta - API may change in future releases.
    """
    from ...utils.icons import Icon

    # Build avatar section
    avatar_section = None
    if avatar:
        avatar_section = Img(
            src=avatar,
            alt=author,
            cls="rounded-circle me-3",
            style="width: 48px; height: 48px; object-fit: cover;",
        )

    # Build rating stars
    rating_section = None
    if rating is not None:
        stars = []
        for i in range(5):
            star_icon = "star-fill" if i < rating else "star"
            stars.append(Icon(star_icon, cls="text-warning"))

        rating_section = Div(
            *stars,
            cls="mb-3",
        )

    # Build author info
    author_info = []
    author_info.append(Span(author, cls="fw-bold d-block"))
    if role:
        author_info.append(Span(role, cls="text-muted small"))

    author_section = Div(
        Div(
            avatar_section,
            Div(*author_info),
            cls="d-flex align-items-center",
        ),
        cls="mt-3",
    )

    # Build quote
    quote_section = Blockquote(
        P(f'"{quote}"', cls="mb-0 fst-italic"),
        cls="mb-3",
    )

    # Build card content
    card_content = []
    if rating_section:
        card_content.append(rating_section)
    card_content.append(quote_section)
    card_content.append(author_section)

    # Build classes
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes("h-100", user_cls)

    return Card(
        *card_content,
        cls=all_classes,
        **kwargs,
    )


@register(category="patterns")
@beta
def TestimonialSection(
    *testimonials: Any,
    title: str = "What Our Customers Say",
    subtitle: str | None = None,
    columns: int = 3,
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
    """Section displaying multiple testimonials in a grid.

    Args:
        *testimonials: Testimonial components to display
        title: Section title
        subtitle: Optional subtitle
        columns: Number of columns in grid (default: 3)
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
        **kwargs: Additional HTML attributes

    Returns:
        Div with testimonials in responsive grid

    Example:
        Basic testimonial section:
        >>> TestimonialSection(
        ...     Testimonial(
        ...         quote="Great product!",
        ...         author="Alice",
        ...         role="Developer"
        ...     ),
        ...     Testimonial(
        ...         quote="Highly recommend!",
        ...         author="Bob",
        ...         role="Designer"
        ...     ),
        ...     Testimonial(
        ...         quote="Best decision ever!",
        ...         author="Carol",
        ...         role="Manager"
        ...     )
        ... )

        Custom title and 2 columns:
        >>> TestimonialSection(
        ...     *testimonials,
        ...     title="Success Stories",
        ...     subtitle="Hear from our happy customers",
        ...     columns=2
        ... )

    Note:
        Marked as @beta - API may change in future releases.
    """
    from ..layout.grid import Col, Container, Row

    header_attrs = convert_attrs(dict(header_attrs or {}))
    title_attrs = convert_attrs(dict(title_attrs or {}))
    subtitle_attrs = convert_attrs(dict(subtitle_attrs or {}))
    row_attrs = convert_attrs(dict(row_attrs or {}))
    col_attrs = convert_attrs(dict(col_attrs or {}))

    # Build header
    header_content = [
        Div(
            title,
            cls=merge_classes("h2 text-center mb-2", title_cls, title_attrs.pop("cls", "")),
            **title_attrs,
        )
    ]
    if subtitle:
        header_content.append(
            P(
                subtitle,
                cls=merge_classes(
                    "text-center text-muted mb-5",
                    subtitle_cls,
                    subtitle_attrs.pop("cls", ""),
                ),
                **subtitle_attrs,
            )
        )

    header = Div(
        *header_content,
        cls=merge_classes(header_cls, header_attrs.pop("cls", "")),
        **header_attrs,
    )

    # Build testimonial grid
    col_size = 12 // columns
    testimonial_cols = []
    for testimonial in testimonials:
        current_col_attrs = dict(col_attrs)
        testimonial_cols.append(
            Col(
                testimonial,
                md=col_size,
                cls=merge_classes("mb-4", col_cls, current_col_attrs.pop("cls", "")),
                **current_col_attrs,
            )
        )

    testimonial_grid = Row(
        *testimonial_cols,
        cls=merge_classes(row_cls, row_attrs.pop("cls", "")),
        **row_attrs,
    )

    # Build classes
    base_classes = ["py-5"]
    user_cls = kwargs.pop("cls", "")
    all_classes = merge_classes(" ".join(base_classes), user_cls)

    # Build attributes
    attrs: dict[str, Any] = {"cls": all_classes}
    attrs.update(convert_attrs(kwargs))

    return Div(
        Container(
            header,
            testimonial_grid,
        ),
        **attrs,
    )
