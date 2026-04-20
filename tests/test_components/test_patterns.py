"""Tests for pattern components (FooterModern, TestimonialSection)."""

from fasthtml.common import to_xml

from faststrap.components.patterns import (
    Feature,
    FeatureGrid,
    FooterModern,
    PricingGroup,
    PricingTier,
    Testimonial,
    TestimonialSection,
)


def test_feature_supports_child_class_customization():
    """Feature supports styling hooks for title, description, and icon wrapper."""
    feature = Feature(
        "Fast build loops",
        "Use Python and HTMX without reimplementing card markup.",
        icon="lightning-charge",
        icon_wrapper_cls="rounded-4 shadow-sm",
        title_cls="display-6",
        description_cls="lead",
    )
    html = to_xml(feature)

    assert "feature-item" in html
    assert "feature-icon bg-primary text-white rounded-4 shadow-sm" in html
    assert "display-6" in html
    assert "lead" in html


def test_feature_supports_child_attrs():
    """Feature exposes attribute escape hatches for nested elements."""
    feature = Feature(
        "Design control",
        "Add production-grade hooks without rewriting the pattern.",
        icon="palette",
        icon_wrapper_attrs={"data_role": "feature-icon"},
        title_attrs={"id": "feature-title"},
        description_attrs={"data_testid": "feature-description"},
    )
    html = to_xml(feature)

    assert 'data-role="feature-icon"' in html
    assert 'id="feature-title"' in html
    assert 'data-testid="feature-description"' in html


def test_feature_grid_supports_row_and_column_customization():
    """FeatureGrid exposes row and column customization hooks."""
    grid = FeatureGrid(
        Feature("A", "Alpha"),
        Feature("B", "Beta"),
        columns=2,
        row_cls="align-items-stretch gx-5",
        row_attrs={"data_role": "feature-row"},
        col_cls="h-100",
        col_attrs={"data_layout": "feature-col"},
    )
    html = to_xml(grid)

    assert "feature-grid" in html
    assert "align-items-stretch gx-5" in html
    assert 'data-role="feature-row"' in html
    assert 'data-layout="feature-col"' in html
    assert "col-md-6 mb-4 h-100" in html


def test_pricing_group_supports_header_and_grid_customization():
    """PricingGroup exposes consistent header, row, and column hooks."""
    group = PricingGroup(
        PricingTier("Starter", 19),
        PricingTier("Pro", 49, highlighted=True),
        title="Clear pricing",
        subtitle="Built for teams that ship often.",
        header_cls="mx-auto",
        title_cls="display-5",
        subtitle_cls="lead",
        row_cls="align-items-stretch gx-5",
        col_cls="h-100",
        header_attrs={"data_role": "pricing-header"},
        row_attrs={"data_grid": "pricing-row"},
        col_attrs={"data_col": "pricing-tier"},
    )
    html = to_xml(group)

    assert "pricing-group py-5" in html
    assert "display-5" in html
    assert "lead" in html
    assert "align-items-stretch gx-5" in html
    assert "col-md-6 mb-4 h-100" in html
    assert 'data-role="pricing-header"' in html
    assert 'data-grid="pricing-row"' in html
    assert 'data-col="pricing-tier"' in html


# FooterModern Tests
def test_footer_modern_basic():
    """FooterModern renders with basic content."""
    footer = FooterModern(brand="MyApp")
    html = to_xml(footer)

    assert "MyApp" in html
    assert "footer" in html.lower()


def test_footer_modern_with_tagline():
    """FooterModern displays tagline."""
    footer = FooterModern(brand="MyApp", tagline="Building the future")
    html = to_xml(footer)

    assert "MyApp" in html
    assert "Building the future" in html


def test_footer_modern_with_columns():
    """FooterModern displays link columns."""
    footer = FooterModern(
        columns=[
            {
                "title": "Product",
                "links": [
                    {"text": "Features", "href": "/features"},
                    {"text": "Pricing", "href": "/pricing"},
                ],
            }
        ]
    )
    html = to_xml(footer)

    assert "Product" in html
    assert "Features" in html
    assert "/features" in html


def test_footer_modern_with_social():
    """FooterModern displays social links."""
    footer = FooterModern(
        social_links=[
            {"icon": "twitter", "href": "https://twitter.com/app"},
            {"icon": "github", "href": "https://github.com/app"},
        ]
    )
    html = to_xml(footer)

    assert "twitter" in html
    assert "github" in html


def test_footer_modern_copyright():
    """FooterModern displays copyright text."""
    footer = FooterModern(copyright_text="© 2026 MyCompany Inc.")
    html = to_xml(footer)

    assert "© 2026 MyCompany Inc." in html


def test_footer_modern_variants():
    """FooterModern supports background variants."""
    footer = FooterModern(brand="Test", bg_variant="light", text_variant="dark")
    html = to_xml(footer)

    assert "bg-light" in html
    assert "text-dark" in html


# Testimonial Tests
def test_testimonial_basic():
    """Testimonial renders with quote and author."""
    testimonial = Testimonial(quote="Great product!", author="John Doe")
    html = to_xml(testimonial)

    assert "Great product!" in html
    assert "John Doe" in html


def test_testimonial_with_role():
    """Testimonial displays author role."""
    testimonial = Testimonial(quote="Amazing!", author="Jane Smith", role="CEO, Acme Corp")
    html = to_xml(testimonial)

    assert "Jane Smith" in html
    assert "CEO, Acme Corp" in html


def test_testimonial_with_avatar():
    """Testimonial displays avatar image."""
    testimonial = Testimonial(quote="Test", author="Test User", avatar="/static/avatar.jpg")
    html = to_xml(testimonial)

    assert "/static/avatar.jpg" in html
    assert "rounded-circle" in html


def test_testimonial_with_rating():
    """Testimonial displays star rating."""
    testimonial = Testimonial(quote="Excellent!", author="User", rating=5)
    html = to_xml(testimonial)

    assert "star" in html  # Star icons


# TestimonialSection Tests
def test_testimonial_section_basic():
    """TestimonialSection renders with testimonials."""
    section = TestimonialSection(
        Testimonial(quote="Great!", author="User 1"),
        Testimonial(quote="Amazing!", author="User 2"),
    )
    html = to_xml(section)

    assert "Great!" in html
    assert "Amazing!" in html


def test_testimonial_section_title():
    """TestimonialSection displays custom title."""
    section = TestimonialSection(Testimonial(quote="Test", author="User"), title="Customer Reviews")
    html = to_xml(section)

    assert "Customer Reviews" in html


def test_testimonial_section_subtitle():
    """TestimonialSection displays subtitle."""
    section = TestimonialSection(
        Testimonial(quote="Test", author="User"), subtitle="Hear from our happy customers"
    )
    html = to_xml(section)

    assert "Hear from our happy customers" in html


def test_testimonial_section_columns():
    """TestimonialSection supports custom column count."""
    section = TestimonialSection(
        Testimonial(quote="1", author="A"), Testimonial(quote="2", author="B"), columns=2
    )
    html = to_xml(section)

    # Should have grid layout
    assert "row" in html.lower() or "col" in html.lower()


def test_testimonial_section_supports_header_and_grid_customization():
    """TestimonialSection exposes consistent header, row, and column hooks."""
    section = TestimonialSection(
        Testimonial(quote="Great product!", author="User A"),
        Testimonial(quote="Still great!", author="User B"),
        columns=2,
        header_cls="mx-auto",
        title_cls="display-6",
        subtitle="What teams noticed after launch",
        subtitle_cls="lead",
        row_cls="align-items-stretch gx-5",
        col_cls="h-100",
        header_attrs={"data_role": "testimonials-header"},
        row_attrs={"data_grid": "testimonials-row"},
        col_attrs={"data_col": "testimonial-item"},
    )
    html = to_xml(section)

    assert "display-6" in html
    assert "lead" in html
    assert "align-items-stretch gx-5" in html
    assert "col-md-6 mb-4 h-100" in html
    assert 'data-role="testimonials-header"' in html
    assert 'data-grid="testimonials-row"' in html
    assert 'data-col="testimonial-item"' in html
