"""Flagship showcase — SEA Furniture Store.

Production-grade furniture e-commerce landing for Faststrap:

- Playfair Display display font + Inter body
- Warm cream palette (#FAF7F2) with walnut brown accents
- Product cards: image zoom on hover, heart wishlist Icon, quick-view overlay
- Why Choose Us: Icon() components (patch-check, tree, house-heart, truck)
- Stats banner: Orders / Homes / Cities / Years
- TestimonialSection with star ratings
- Brands strip and News grid
- FooterModern, PageMeta, Fx animations throughout
"""

from __future__ import annotations

from typing import Any

from fasthtml.common import (
    H1,
    H2,
    H3,
    H4,
    A,
    Br,
    Button,
    Div,
    FastHTML,
    Img,
    Nav,
    P,
    Span,
    Strong,
    Style,
    serve,
)

from faststrap import (
    Badge,
    Card,
    Col,
    Container,
    FooterModern,
    Fx,
    Icon,
    PageMeta,
    Row,
    Testimonial,
    TestimonialSection,
    add_bootstrap,
    create_theme,
)

# ── Theme ──────────────────────────────────────────────────────────────────────
FURNITURE_THEME = create_theme(
    primary="#5C4033",  # walnut brown
    secondary="#8D6E63",  # warm tan
    success="#4CAF50",
    warning="#F6A33B",
    danger="#E53935",
    light="#FAF7F2",  # warm cream
    dark="#1A1210",
)

app = FastHTML()
add_bootstrap(app, theme=FURNITURE_THEME, font_family="Inter", mode="light")

# ── Data ───────────────────────────────────────────────────────────────────────
PRODUCTS = [
    (
        "Accent Lounge Chair",
        "$249",
        "https://images.unsplash.com/photo-1596162954151-cdcb4c0f70a8?w=800",
    ),
    (
        "Pastel Occasional Chair",
        "$189",
        "https://images.unsplash.com/photo-1505693416388-ac5ce068fe85?w=800",
    ),
    (
        "Round Walnut Table",
        "$320",
        "https://images.unsplash.com/photo-1505691938895-1758d7feb511?w=800",
    ),
    ("Soft Fabric Sofa", "$640", "https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=800"),
    (
        "Velvet Reading Chair",
        "$279",
        "https://images.unsplash.com/photo-1549187774-b4e9b0445b41?w=800",
    ),
    (
        "Minimal Daybed",
        "$520",
        "https://images.unsplash.com/photo-1583847268964-b28dc8f51f92?w=800",
    ),
]

FEATURED = [
    (
        "Industrial Side Table",
        "$120",
        "https://images.unsplash.com/photo-1616594039964-3b1c0801c4e7?w=800",
    ),
    (
        "Nordic TV Console",
        "$480",
        "https://images.unsplash.com/photo-1600210492486-724fe5c67fb0?w=800",
    ),
    (
        "Floating Wall Shelf",
        "$80",
        "https://images.unsplash.com/photo-1556228453-efd6c1ff04f6?w=800",
    ),
    (
        "Compact Work Desk",
        "$260",
        "https://images.unsplash.com/photo-1519710164239-da123dc03ef4?w=800",
    ),
    (
        "Lounge Grey Armchair",
        "$350",
        "https://images.unsplash.com/photo-1615874959474-d609969a20ed?w=800",
    ),
]

STATS = [
    ("74,353", "Orders Delivered", "box-seam-fill"),
    ("6,333", "Happy Homes", "house-heart-fill"),
    ("20+", "Cities Served", "geo-alt-fill"),
    ("20+", "Years Experience", "award-fill"),
]

BRANDS = ["WoodNature", "Golden Gallery", "Modern Living", "HighLight Home", "Nordic Scale"]

NEWS = [
    (
        "The Art of Choosing Furniture That Complements Your Space",
        "https://images.unsplash.com/photo-1586023492125-27b2c045efd7?w=1200",
    ),
    (
        "Sustainable Materials: The Future of Modern Furniture",
        "https://images.unsplash.com/photo-1615529182904-14819c35db37?w=1200",
    ),
    (
        "How Minimalist Decor Creates Calm Living Rooms",
        "https://images.unsplash.com/photo-1493663284031-b7e3aefcae8e?w=1200",
    ),
]

CATEGORIES = [
    ("moon-stars-fill", "Bedroom", "#5C4033"),
    ("cup-hot-fill", "Kitchen", "#8D6E63"),
    ("lamp-fill", "Living Room", "#A0785A"),
    ("laptop", "Office", "#6D4C41"),
]

WHY_CHOOSE = [
    (
        "patch-check-fill",
        "Crafted with Precision",
        "Quality-first construction with artisan attention to every joint and finish.",
        "#5C4033",
    ),
    (
        "tree-fill",
        "Sustainable Materials",
        "Eco-conscious sourcing from verified sustainable forests and recycled materials.",
        "#4CAF50",
    ),
    (
        "house-heart-fill",
        "Designed for Every Space",
        "From compact studio apartments to sprawling family homes — we fit your life.",
        "#F6A33B",
    ),
    (
        "truck",
        "Reliable Delivery",
        "White-glove nationwide shipping with real-time tracking and room-of-choice drop.",
        "#0EA5E9",
    ),
]

# ── CSS ────────────────────────────────────────────────────────────────────────
CSS = """
/* ════════════════════════════════════════════════════════════
   SEA Furniture · Premium E-Commerce CSS
   Warm cream palette, Playfair Display headings,
   product card hover zoom, wishlist animations.
   Atmospheric only — Bootstrap/Faststrap own layout.
   ════════════════════════════════════════════════════════════ */

@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;800&family=Inter:wght@300;400;500;600;700&display=swap');

body {
  background: #FAF7F2;
  font-family: 'Inter', system-ui, sans-serif;
}

/* ── Typography ─────────────────────────────────────────────── */
h1, h2, h3, h4 {
  font-family: 'Playfair Display', Georgia, serif;
}

/* ── Sticky nav ─────────────────────────────────────────────── */
.fs-nav {
  background: rgba(250,247,242,0.92);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid rgba(92,64,51,0.08);
}

.fs-brand-text {
  font-family: 'Playfair Display', serif;
  font-size: 1.5rem;
  font-weight: 700;
  color: #1A1210;
  letter-spacing: -0.01em;
}

/* ── Hero ───────────────────────────────────────────────────── */
.fs-hero {
  background: linear-gradient(135deg, #1A1210 0%, #2C1810 50%, #1A1210 100%);
  border-radius: 20px;
  overflow: hidden;
  position: relative;
}

.fs-hero::after {
  content: "";
  position: absolute;
  top: -30%;
  right: -10%;
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(246,163,59,0.12) 0%, transparent 70%);
  border-radius: 50%;
  pointer-events: none;
}

/* ── Product Cards ──────────────────────────────────────────── */
.fs-product-card {
  background: #fff;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(92,64,51,0.06);
  border: 1px solid rgba(92,64,51,0.06);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  position: relative;
  height: 100%;
}

.fs-product-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 16px 40px rgba(92,64,51,0.14);
}

.fs-product-image-wrap {
  position: relative;
  overflow: hidden;
  height: 200px;
}

.fs-product-image-wrap img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.fs-product-card:hover .fs-product-image-wrap img {
  transform: scale(1.08);
}

/* Wishlist button */
.fs-wishlist-btn {
  position: absolute;
  top: 0.75rem;
  right: 0.75rem;
  width: 2.2rem;
  height: 2.2rem;
  border-radius: 50%;
  background: rgba(255,255,255,0.9);
  backdrop-filter: blur(4px);
  border: none;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #9CA3AF;
  cursor: pointer;
  transition: color 0.2s ease, transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1);
  z-index: 2;
}

.fs-wishlist-btn:hover { color: #E53935; transform: scale(1.2); }

/* Quick view overlay */
.fs-quick-view {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  background: rgba(92,64,51,0.85);
  color: #fff;
  text-align: center;
  padding: 0.6rem;
  font-size: 0.8rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  transform: translateY(100%);
  transition: transform 0.25s ease;
  cursor: pointer;
}

.fs-product-card:hover .fs-quick-view { transform: translateY(0); }

/* ── Category pills ─────────────────────────────────────────── */
.fs-category-pill {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.5rem;
  padding: 1.25rem 1rem;
  border-radius: 14px;
  border: 1.5px solid rgba(92,64,51,0.1);
  background: #fff;
  cursor: pointer;
  transition: border-color 0.2s ease, transform 0.2s ease;
  text-align: center;
}

.fs-category-pill:hover {
  border-color: #5C4033;
  transform: translateY(-3px);
}

.fs-category-icon {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.1rem;
}

/* ── Why Choose Us ──────────────────────────────────────────── */
.fs-why-card {
  background: #fff;
  border-radius: 14px;
  padding: 1.5rem;
  box-shadow: 0 2px 12px rgba(92,64,51,0.06);
  border: 1px solid rgba(92,64,51,0.06);
  height: 100%;
  transition: transform 0.2s ease;
}

.fs-why-card:hover { transform: translateY(-4px); }

.fs-why-icon {
  width: 3rem;
  height: 3rem;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.25rem;
  margin-bottom: 1rem;
}

/* ── Stats Banner ───────────────────────────────────────────── */
.fs-stats-banner {
  background: linear-gradient(135deg, #1A1210, #2C1810);
  border-radius: 20px;
  padding: 3rem 2rem;
}

.fs-stat-val {
  font-size: 2.2rem;
  font-weight: 800;
  color: #F6A33B;
  font-family: 'Playfair Display', serif;
  letter-spacing: -0.02em;
  line-height: 1;
}

.fs-stat-lbl {
  font-size: 0.8rem;
  color: rgba(255,255,255,0.55);
  font-weight: 500;
  margin-top: 0.3rem;
}

/* ── Brand cards ────────────────────────────────────────────── */
.fs-brand-card {
  background: #fff;
  border-radius: 10px;
  padding: 1rem 1.25rem;
  border: 1px solid rgba(92,64,51,0.08);
  text-align: center;
  transition: box-shadow 0.2s ease;
}

.fs-brand-card:hover { box-shadow: 0 6px 20px rgba(92,64,51,0.1); }

/* ── News cards ─────────────────────────────────────────────── */
.fs-news-card {
  background: #fff;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 2px 12px rgba(92,64,51,0.06);
  border: 1px solid rgba(92,64,51,0.06);
  height: 100%;
  transition: transform 0.2s ease;
}

.fs-news-card:hover { transform: translateY(-4px); }

/* ── Dark section ───────────────────────────────────────────── */
.fs-dark-section {
  background: linear-gradient(135deg, #1A1210, #2C1810);
  border-radius: 20px;
  color: #fff;
}
"""


def product_card(name: str, price: str, image: str, index: int = 0) -> Any:
    return Div(
        # Image with zoom + wishlist + quick view
        Div(
            Img(src=image, alt=name),
            Button(
                Icon("heart"),
                cls="fs-wishlist-btn",
                title="Add to wishlist",
            ),
            Div("Quick View", cls="fs-quick-view"),
            cls="fs-product-image-wrap",
        ),
        # Card body
        Div(
            Div(
                Strong(name, cls="d-block mb-0", style="font-size:0.92rem;"),
                Span(price, cls="fw-700", style="color:#5C4033;"),
                cls="d-flex justify-content-between align-items-center mb-2",
            ),
            Button(
                Icon("cart-plus", cls="me-1"),
                "Add to Cart",
                cls="btn btn-sm w-100 fw-600",
                style="background:#5C4033;color:#fff;border-radius:50px;",
            ),
            cls="p-3",
        ),
        cls=f"fs-product-card {Fx.fade_in}",
        style=f"animation-delay:{index*60}ms;",
    )


@app.get("/")
def home() -> Any:
    return Div(
        Style(CSS),
        PageMeta(
            title="SEA Furniture — Premium Furniture for Elegant Living",
            description="Discover elegant, durable furniture built for modern living spaces. Handcrafted chairs, sofas, tables, and more.",
        ),
        Container(
            # ── Navigation ─────────────────────────────────────────
            Nav(
                Div(
                    A(Span("sea.", cls="fs-brand-text"), cls="navbar-brand", href="#"),
                    Button(
                        Span(cls="navbar-toggler-icon"),
                        cls="navbar-toggler",
                        type="button",
                        data_bs_toggle="collapse",
                        data_bs_target="#fsNavCollapse",
                        aria_controls="fsNavCollapse",
                        aria_expanded="false",
                        aria_label="Toggle navigation",
                    ),
                    Div(
                        Div(
                            A("Home", href="#", cls="nav-link fw-500"),
                            A("Products", href="#products", cls="nav-link fw-500"),
                            A("About", href="#about", cls="nav-link fw-500"),
                            A("Featured", href="#featured", cls="nav-link fw-500"),
                            A("Contact", href="#footer", cls="nav-link fw-500"),
                            cls="navbar-nav ms-auto align-items-center gap-1",
                        ),
                        cls="collapse navbar-collapse",
                        id="fsNavCollapse",
                    ),
                    cls="container",
                ),
                cls="navbar navbar-expand-lg navbar-light fs-nav shadow-none px-2 position-sticky top-0 z-3",
            ),
            # ── Hero ───────────────────────────────────────────────
            Div(
                Row(
                    Col(
                        Div(
                            Badge(
                                Icon("stars", cls="me-1"),
                                "New Collection 2026",
                                variant="warning",
                                cls="text-dark fw-600 mb-3",
                            ),
                            H1(
                                Span("Furniture ", style="color:#F6A33B;"),
                                "Solutions.",
                                Br(),
                                "Affordable Prices.",
                                cls=f"display-4 fw-bold text-white {Fx.slide_up}",
                            ),
                            P(
                                "Discover elegant, durable furniture crafted for modern living. "
                                "From curated chairs to premium cabinets — furnished beautifully.",
                                cls=f"text-light mt-3 fs-5 {Fx.fade_in} {Fx.delay_sm}",
                            ),
                            Div(
                                Button(
                                    Icon("arrow-right-circle", cls="me-2"),
                                    "View Products",
                                    variant="warning",
                                    cls="text-dark fw-700 me-2",
                                    style="border-radius:50px;",
                                ),
                                Button(
                                    "Request Quote",
                                    variant="light",
                                    outline=True,
                                    style="border-radius:50px;",
                                ),
                                cls="mt-4",
                            ),
                            cls="p-5",
                        ),
                        lg=7,
                    ),
                    Col(
                        Div(
                            Img(
                                src="https://images.unsplash.com/photo-1484101403633-562f891dc89a?w=1200",
                                cls="w-100 rounded-3 object-fit-cover",
                                style="height:100%;min-height:420px;",
                            ),
                            cls="h-100 p-3",
                        ),
                        lg=5,
                    ),
                    cls="g-0",
                    cols=1,
                    cols_lg=2,
                ),
                cls="fs-hero mt-3",
            ),
            # ── Category Pills ─────────────────────────────────────
            Div(
                H2("Shop by Space", cls="fw-bold text-center mb-1"),
                P(
                    "Browse furniture for every room in your home.",
                    cls="text-center text-muted mb-4",
                ),
                Row(
                    *[
                        Col(
                            Div(
                                Div(
                                    Icon(ic),
                                    cls="fs-category-icon",
                                    style=f"background:{color}18;color:{color};",
                                ),
                                Strong(label, cls="small"),
                                cls="fs-category-pill",
                            ),
                            cls=f"mb-3 {Fx.fade_in}",
                        )
                        for ic, label, color in CATEGORIES
                    ],
                    cls="g-2",
                    cols=2,
                    cols_md=4,
                ),
                cls="mt-5",
            ),
            # ── Products ───────────────────────────────────────────
            Div(
                H2("Our Products", cls="fw-bold text-center"),
                P(
                    "Carefully selected pieces to elevate comfort and style.",
                    cls="text-center text-muted mb-4",
                ),
                Row(
                    *[
                        Col(product_card(n, p, img, i), cls="mb-4")
                        for i, (n, p, img) in enumerate(PRODUCTS)
                    ],
                    cls="g-3",
                    cols=1,
                    cols_md=2,
                    cols_lg=3,
                ),
                Div(
                    Button(
                        Icon("grid-3x3-gap-fill", cls="me-2"),
                        "View All Products",
                        variant="outline-secondary",
                        cls="fw-600",
                        style="border-radius:50px;",
                    ),
                    cls="text-center mt-2",
                ),
                id="products",
                cls="mt-5",
            ),
            # ── Stats Banner ───────────────────────────────────────
            Div(
                Row(
                    *[
                        Col(
                            Div(
                                Div(
                                    Icon(
                                        icon,
                                        cls="me-3",
                                        style="font-size:1.8rem;opacity:0.5;color:#F6A33B;",
                                    ),
                                    Div(
                                        Div(val, cls="fs-stat-val"),
                                        Div(label, cls="fs-stat-lbl"),
                                    ),
                                    cls="d-flex align-items-center",
                                ),
                                cls="text-center text-md-start",
                            ),
                            cls=f"mb-3 {Fx.fade_in}",
                        )
                        for val, label, icon in STATS
                    ],
                    cls="g-3 align-items-center",
                    cols=2,
                    cols_md=4,
                ),
                cls="fs-stats-banner mt-5",
            ),
            # ── Featured + Deal Card ───────────────────────────────
            Div(
                Row(
                    Col(
                        H3("Featured Products", cls="fw-bold mb-3"),
                        Row(
                            *[
                                Col(
                                    Card(
                                        Img(
                                            src=img,
                                            cls="w-100 object-fit-cover rounded-top",
                                            style="height:120px;",
                                        ),
                                        Div(
                                            Strong(name, cls="small d-block"),
                                            Span(price, cls="small fw-700", style="color:#5C4033;"),
                                            cls="p-2",
                                        ),
                                        cls="border-0 shadow-sm h-100 fs-news-card",
                                    ),
                                    cls="mb-3",
                                )
                                for name, price, img in FEATURED
                            ],
                            cls="g-2",
                            cols=2,
                            cols_md=3,
                        ),
                        lg=8,
                        id="featured",
                    ),
                    Col(
                        Card(
                            Img(
                                src="https://images.unsplash.com/photo-1555041469-a586c61ea9bc?w=1200",
                                cls="w-100 object-fit-cover rounded-top",
                                style="height:220px;",
                            ),
                            Div(
                                Badge(
                                    Icon("tag-fill", cls="me-1"),
                                    "UP TO 35% OFF",
                                    variant="warning",
                                    cls="text-dark fw-700 mb-2",
                                ),
                                H4(
                                    "Perfect Cabinets For Your Living Room!",
                                    style="font-family:'Playfair Display',serif;",
                                ),
                                P(
                                    "Limited-time pricing on handcrafted storage essentials.",
                                    cls="text-muted",
                                ),
                                Button(
                                    Icon("bag-fill", cls="me-2"),
                                    "Shop Now",
                                    variant="warning",
                                    cls="text-dark fw-700",
                                    style="border-radius:50px;",
                                ),
                                cls="p-3",
                            ),
                            cls="border-0 shadow-sm",
                        ),
                        lg=4,
                    ),
                    cls=" ",
                    cols=1,
                    cols_lg=2,
                ),
                cls="mt-5",
            ),
            # ── Why Choose Us ──────────────────────────────────────
            Div(
                Row(
                    Col(
                        H2("Why Choose SEA", cls="fw-bold mb-4", id="about"),
                        Row(
                            *[
                                Col(
                                    Div(
                                        Div(
                                            Icon(icon),
                                            cls="fs-why-icon",
                                            style=f"background:{color}18;color:{color};",
                                        ),
                                        Strong(title, cls="d-block mb-1"),
                                        P(desc, cls="small text-muted mb-0"),
                                        cls=f"fs-why-card {Fx.fade_in}",
                                        style=f"animation-delay:{i*80}ms;",
                                    ),
                                    cls="mb-3",
                                )
                                for i, (icon, title, desc, color) in enumerate(WHY_CHOOSE)
                            ],
                            cls="g-3",
                            cols=1,
                            cols_md=2,
                        ),
                        lg=8,
                    ),
                    Col(
                        Card(
                            Div(
                                Icon("quote", cls="display-4", style="color:#F6A33B;opacity:0.8;"),
                                P(
                                    '"I absolutely love our new living room set. '
                                    'The craftsmanship is outstanding and delivery was seamless."',
                                    cls="mb-3",
                                    style="font-style:italic;",
                                ),
                                Div(
                                    Icon("star-fill", cls="text-warning"),
                                    Icon("star-fill", cls="text-warning"),
                                    Icon("star-fill", cls="text-warning"),
                                    Icon("star-fill", cls="text-warning"),
                                    Icon("star-fill", cls="text-warning"),
                                    cls="d-flex gap-1 mb-2",
                                ),
                                Strong("John Doe", style="color:#F6A33B;"),
                                P("Verified Buyer · Nigeria", cls="small text-muted mb-0"),
                                cls="p-4",
                            ),
                            cls="border-0 h-100",
                            style="background:linear-gradient(135deg,#1A1210,#2C1810);color:#fff;border-radius:16px;",
                        ),
                        lg=4,
                    ),
                    cls="",
                    cols=1,
                    cols_lg=2,
                ),
                cls="mt-5",
            ),
            # ── Testimonials ───────────────────────────────────────
            Div(
                H2("What Our Customers Say", cls="fw-bold text-center mb-5"),
                TestimonialSection(
                    Testimonial(
                        quote="The quality exceeded my expectations. The walnut table is a centrepiece in our dining room.",
                        author="Amaka Osei",
                        role="Interior Designer, Abuja",
                        rating=5,
                    ),
                    Testimonial(
                        quote="Delivery was spot on and assembly was a breeze. Will definitely order again.",
                        author="Tunde Bakare",
                        role="Architect, Lagos",
                        rating=5,
                    ),
                    columns=2,
                ),
                cls="mt-5",
            ),
            # ── Brands ────────────────────────────────────────────
            Div(
                H3("Top Featured Brands", cls="fw-bold mb-3"),
                Row(
                    *[
                        Col(
                            Div(
                                Strong(b, cls="d-block mb-0"),
                                Span("Quality partner", cls="small text-muted"),
                                cls="fs-brand-card",
                            ),
                            cls="mb-3",
                        )
                        for b in BRANDS
                    ],
                    cls="g-2",
                    cols=2,
                    cols_md=3,
                    cols_lg=5,
                ),
                cls="mt-5",
            ),
            # ── News ──────────────────────────────────────────────
            Div(
                H3("News & Updates", cls="fw-bold mb-3"),
                Row(
                    *[
                        Col(
                            Div(
                                Img(src=img, cls="w-100 object-fit-cover", style="height:180px;"),
                                Div(
                                    Strong(title),
                                    Div(
                                        Icon("arrow-right-circle", cls="me-1"),
                                        "Read more",
                                        cls="small mt-1",
                                        style="color:#5C4033;cursor:pointer;",
                                    ),
                                    cls="p-3",
                                ),
                                cls="fs-news-card",
                            ),
                            cls=f"mb-3 {Fx.fade_in}",
                        )
                        for title, img in NEWS
                    ],
                    cls="g-3",
                    cols=1,
                    cols_lg=3,
                ),
                cls="mt-3 mb-5",
            ),
            # ── Footer ────────────────────────────────────────────
            FooterModern(
                brand="sea.",
                tagline="Premium furniture solutions for elegant living.",
                columns=[
                    {
                        "title": "Company",
                        "links": [
                            {"text": "About", "href": "#about"},
                            {"text": "Products", "href": "#products"},
                            {"text": "Contact", "href": "#footer"},
                        ],
                    },
                    {
                        "title": "Support",
                        "links": [
                            {"text": "Shipping", "href": "#"},
                            {"text": "Returns", "href": "#"},
                            {"text": "Help", "href": "#"},
                        ],
                    },
                ],
                social_links=[
                    {"icon": "instagram", "href": "#"},
                    {"icon": "facebook", "href": "#"},
                    {"icon": "twitter-x", "href": "#"},
                ],
                bg_variant="dark",
                text_variant="light",
                copyright_text="© 2026 SEA Furniture. All rights reserved.",
                id="footer",
                cls="rounded-4 mt-4",
            ),
            cls="py-4",
        ),
        cls="container-xl",
    )


if __name__ == "__main__":
    serve(port=5014)
