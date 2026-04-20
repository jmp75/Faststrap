"""Flagship showcase — Aurelia Hotels Booking.

Production-grade luxury hotel landing for Faststrap:

- Cormorant Garamond display font + Inter body
- Gold accent (#C9A84C) on dark navy (#0A0F1E) palette
- Animated hero with floating "Award Winner" badge and live demand counter
- Amenities glassmorphism strip: WiFi, Breakfast, Parking, Pool, Spa
- Room cards with star ratings, amenity mini-badges, gold price highlight
- AutoRefresh live traveler count
- ActiveSearch room filtering
- LazyLoad testimonials and special offers
- LoadingButton availability check with toast alert
- FooterModern, PageMeta, Fx effects throughout
"""

from __future__ import annotations

import random
from datetime import datetime
from typing import Any

from fasthtml.common import (
    H1,
    H2,
    H4,
    H5,
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
    Alert,
    Badge,
    Card,
    Col,
    Container,
    FooterModern,
    FormGroup,
    Fx,
    Icon,
    Input,
    PageMeta,
    Row,
    Select,
    Testimonial,
    add_bootstrap,
    create_theme,
)
from faststrap.presets import ActiveSearch, AutoRefresh, LazyLoad, LoadingButton, toast_response

# ── Theme ──────────────────────────────────────────────────────────────────────
AURELIA_THEME = create_theme(
    primary="#C9A84C",  # antique gold
    secondary="#8B7355",  # warm stone
    success="#4CAF50",
    danger="#E53935",
    warning="#F59E0B",
    dark="#0A0F1E",
    light="#F8F5EF",
)

app = FastHTML()
add_bootstrap(app, theme=AURELIA_THEME, font_family="Inter")

# ── Data ───────────────────────────────────────────────────────────────────────
ROOMS = [
    {
        "name": "Classic Twin",
        "price": "$92",
        "image": "https://images.unsplash.com/photo-1566665797739-1674de7a421a?w=1200",
        "desc": "Comfortable room with twin beds, ideal for quick city escapes.",
        "size": "26 m²",
        "beds": "2 Twin",
        "amenities": ["wifi", "cup-hot", "snow"],
    },
    {
        "name": "Deluxe King",
        "price": "$129",
        "image": "https://images.unsplash.com/photo-1591088398332-8a7791972843?w=1200",
        "desc": "Elegant king suite with premium linens and city views.",
        "size": "38 m²",
        "beds": "1 King",
        "amenities": ["wifi", "cup-hot", "snow", "tv"],
    },
    {
        "name": "Family Suite",
        "price": "$189",
        "image": "https://images.unsplash.com/photo-1578683010236-d716f9a3f461?w=1200",
        "desc": "Spacious multi-room suite for families and extended stays.",
        "size": "60 m²",
        "beds": "1 King + 2 Twin",
        "amenities": ["wifi", "cup-hot", "snow", "tv", "water"],
    },
    {
        "name": "Presidential",
        "price": "$420",
        "image": "https://images.unsplash.com/photo-1618773928121-c32242e63f39?w=1200",
        "desc": "Top-floor suite with panoramic skyline views and a private lounge.",
        "size": "120 m²",
        "beds": "1 Super King",
        "amenities": ["wifi", "cup-hot", "snow", "tv", "water", "gem"],
    },
]

OFFERS = [
    (
        "Weekend Getaway Package",
        "20% Off",
        "https://images.unsplash.com/photo-1522708323590-d24dbb6b0267?w=1200",
    ),
    (
        "Family Vacation Deal",
        "35% Off",
        "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?w=1200",
    ),
    (
        "Spa & Wellness Retreat",
        "15% Off",
        "https://images.unsplash.com/photo-1544161515-4ab6ce6db874?w=1200",
    ),
]

TEAM = [
    (
        "Michael Drew",
        "General Manager",
        "https://images.unsplash.com/photo-1560250097-0b93528c311a?w=400",
    ),
    (
        "Frank Jones",
        "Guest Relations",
        "https://images.unsplash.com/photo-1488426862026-3ee34a7d66df?w=400",
    ),
    (
        "Mya Mullins",
        "Head of Reception",
        "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=400",
    ),
    (
        "Ruby Nguyen",
        "Wellness Director",
        "https://images.unsplash.com/photo-1487412720507-e7ab37603c6f?w=400",
    ),
]

TESTIMONIALS = [
    (
        "The booking flow was effortless and the room exceeded every expectation. Truly five-star.",
        "Melissa Adam",
        "Via, London",
    ),
    (
        "Outstanding hospitality and the smoothest check-in I've ever experienced.",
        "Ricky Smith",
        "NYC, USA",
    ),
    (
        "Family-friendly service, clean rooms, and the breakfast was absolutely delightful.",
        "Leslie May",
        "LA, USA",
    ),
]

AMENITIES = [
    ("wifi", "Free WiFi", "High-speed throughout"),
    ("cup-hot-fill", "Breakfast", "Included daily"),
    ("car-front-fill", "Parking", "Secure valet"),
    ("water", "Infinity Pool", "Rooftop access"),
    ("heart-pulse-fill", "Spa & Wellness", "World-class"),
]

AMENITY_ICON_LABELS = {
    "wifi": "WiFi",
    "cup-hot": "Breakfast",
    "snow": "A/C",
    "tv": "Smart TV",
    "water": "Pool",
    "gem": "Butler",
}

# ── CSS ────────────────────────────────────────────────────────────────────────
CSS = """
/* ════════════════════════════════════════════════════════════
   Aurelia Hotels · Luxury Landing CSS
   Cormorant Garamond display, Inter body, gold on dark navy.
   Atmospheric only — Bootstrap/Faststrap own layout.
   ════════════════════════════════════════════════════════════ */

@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;0,700;1,400;1,600&family=Inter:wght@300;400;500;600;700&display=swap');

body {
  font-family: 'Inter', system-ui, sans-serif;
  background: #F8F5EF;
  color: #1A1410;
}

/* ── Display font ───────────────────────────────────────────── */
h1, h2, h3, h4 {
  font-family: 'Cormorant Garamond', Georgia, serif;
  letter-spacing: -0.01em;
}

/* ── Navbar ─────────────────────────────────────────────────── */
.au-nav {
  background: rgba(10,15,30,0.92) !important;
  backdrop-filter: blur(16px);
  border-bottom: 1px solid rgba(201,168,76,0.15) !important;
}

.au-brand {
  font-family: 'Cormorant Garamond', serif;
  font-size: 1.5rem;
  font-weight: 700;
  color: #C9A84C !important;
  letter-spacing: 0.05em;
}

/* ── Hero ───────────────────────────────────────────────────── */
.au-hero {
  position: relative;
  background:
    linear-gradient(180deg, rgba(10,15,30,0.65) 0%, rgba(10,15,30,0.45) 50%, rgba(10,15,30,0.85) 100%),
    url('https://images.unsplash.com/photo-1455587734955-081b22074882?w=1400') center/cover no-repeat;
  border-radius: 20px;
  overflow: hidden;
  min-height: 580px;
  display: flex;
  align-items: center;
}

/* Floating award badge animation */
@keyframes au-float {
  0%, 100% { transform: translateY(0); }
  50%       { transform: translateY(-8px); }
}

.au-float-badge {
  animation: au-float 3s ease-in-out infinite;
}

/* Gold divider line */
.au-gold-divider {
  width: 60px;
  height: 2px;
  background: linear-gradient(90deg, #C9A84C, #E8C97A);
  border-radius: 2px;
  margin: 1rem 0 1.25rem;
}

/* ── Amenities strip ────────────────────────────────────────── */
.au-amenities-strip {
  background: rgba(10,15,30,0.85);
  backdrop-filter: blur(20px);
  border-radius: 0 0 16px 16px;
  padding: 1.5rem;
  margin-top: -1px;
}

.au-amenity-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.35rem;
  padding: 0 1rem;
  border-right: 1px solid rgba(201,168,76,0.15);
  text-align: center;
}

.au-amenity-item:last-child { border-right: none; }

.au-amenity-icon {
  width: 2.5rem;
  height: 2.5rem;
  border-radius: 50%;
  background: rgba(201,168,76,0.12);
  color: #C9A84C;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1rem;
}

.au-amenity-label   { font-size: 0.78rem; color: #fff; font-weight: 600; }
.au-amenity-sublabel { font-size: 0.65rem; color: rgba(255,255,255,0.45); }

/* ── Booking card ───────────────────────────────────────────── */
.au-booking-card {
  background: rgba(255,255,255,0.96);
  backdrop-filter: blur(12px);
  border-radius: 16px;
  box-shadow: 0 20px 60px rgba(0,0,0,0.25);
  border: 1px solid rgba(201,168,76,0.15);
}

/* ── Room cards ─────────────────────────────────────────────── */
.au-room-card {
  background: #fff;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 4px 20px rgba(0,0,0,0.06);
  border: 1px solid rgba(0,0,0,0.05);
  height: 100%;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.au-room-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 16px 48px rgba(0,0,0,0.12);
}

.au-room-image-wrap { position: relative; overflow: hidden; }

.au-room-image-wrap img {
  width: 100%;
  height: 220px;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.au-room-card:hover .au-room-image-wrap img { transform: scale(1.06); }

.au-price-tag {
  position: absolute;
  bottom: 0.75rem;
  right: 0.75rem;
  background: rgba(10,15,30,0.85);
  backdrop-filter: blur(8px);
  color: #C9A84C;
  font-weight: 700;
  font-size: 1rem;
  padding: 0.3rem 0.8rem;
  border-radius: 50px;
  font-family: 'Cormorant Garamond', serif;
}

.au-room-body { padding: 1.25rem 1.5rem 1.5rem; }

.au-stars { color: #C9A84C; font-size: 0.8rem; gap: 1px; }

.au-amenity-badge {
  display: inline-flex;
  align-items: center;
  gap: 0.3rem;
  background: rgba(201,168,76,0.08);
  color: #8B7355;
  border-radius: 50px;
  padding: 0.2rem 0.6rem;
  font-size: 0.7rem;
  font-weight: 600;
}

/* ── Section helpers ────────────────────────────────────────── */
.au-section-overline {
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #C9A84C;
  display: block;
  margin-bottom: 0.5rem;
}

/* ── Story section ──────────────────────────────────────────── */
.au-story-section {
  background: #F0EBE1;
  border-radius: 20px;
  padding: 3rem 2.5rem;
}

/* ── CTA section ────────────────────────────────────────────── */
.au-cta {
  background: linear-gradient(135deg, #0A0F1E 0%, #1A2040 100%);
  border-radius: 20px;
  padding: 3rem 2.5rem;
  position: relative;
  overflow: hidden;
}

.au-cta::before {
  content: "";
  position: absolute;
  top: -50%;
  right: -10%;
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(201,168,76,0.08) 0%, transparent 70%);
  border-radius: 50%;
}
"""


def stars(count: int = 5) -> Any:
    return Div(
        *[Icon("star-fill") for _ in range(count)],
        cls="au-stars d-flex",
    )


def amenity_badges(amenity_keys: list[str]) -> Any:
    return Div(
        *[
            Span(
                Icon(k, style="font-size:0.7rem;"),
                AMENITY_ICON_LABELS.get(k, k),
                cls="au-amenity-badge me-1 mb-1",
            )
            for k in amenity_keys
        ],
        cls="d-flex flex-wrap mt-2 mb-3",
    )


def room_card(room: dict, idx: int = 0) -> Any:
    return Div(
        # Image
        Div(
            Img(src=room["image"], alt=room["name"]),
            Span(f"{room['price']} / night", cls="au-price-tag"),
            cls="au-room-image-wrap",
        ),
        # Body
        Div(
            stars(),
            H5(room["name"], cls="fw-700 mt-2 mb-1"),
            P(room["desc"], cls="text-muted small mb-0", style="line-height:1.5;"),
            amenity_badges(room["amenities"]),
            Div(
                Div(
                    Icon("rulers", cls="me-1 text-muted"),
                    Span(room["size"], cls="small text-muted"),
                    cls="d-flex align-items-center me-3",
                ),
                Div(
                    Icon("moon-stars", cls="me-1 text-muted"),
                    Span(room["beds"], cls="small text-muted"),
                    cls="d-flex align-items-center",
                ),
                cls="d-flex mb-3",
            ),
            Button(
                Icon("calendar2-check-fill", cls="me-2"),
                "Check Availability",
                cls="btn btn-sm fw-600 w-100",
                style="background:#C9A84C;color:#fff;border-radius:50px;",
            ),
            cls="au-room-body",
        ),
        cls=f"au-room-card {Fx.fade_in}",
        style=f"animation-delay:{idx*80}ms;",
    )


@app.get("/")
def home() -> Any:
    return Div(
        Style(CSS),
        PageMeta(
            title="Aurelia Hotels — Luxury Hospitality Redefined",
            description="Experience premium hospitality at Aurelia Hotels. Book your stay with fast, easy room reservations and world-class service.",
        ),
        Container(
            # ── Navigation ─────────────────────────────────────────
            Nav(
                Div(
                    A(Span("AURELIA", cls="au-brand"), cls="navbar-brand", href="#"),
                    Button(
                        Span(cls="navbar-toggler-icon"),
                        cls="navbar-toggler border-0",
                        type="button",
                        data_bs_toggle="collapse",
                        data_bs_target="#auNavCollapse",
                        aria_controls="auNavCollapse",
                        aria_expanded="false",
                        aria_label="Toggle navigation",
                    ),
                    Div(
                        Div(
                            A("Home", href="#home", cls="nav-link text-white-50 fw-500"),
                            A("Rooms", href="#rooms", cls="nav-link text-white-50 fw-500"),
                            A("Deals", href="#deals", cls="nav-link text-white-50 fw-500"),
                            A("Contact", href="#contact", cls="nav-link text-white-50 fw-500"),
                            cls="navbar-nav ms-auto align-items-center gap-3",
                        ),
                        cls="collapse navbar-collapse",
                        id="auNavCollapse",
                    ),
                    cls="container",
                ),
                cls="navbar navbar-expand-lg navbar-dark au-nav position-sticky top-0 z-3",
            ),
            # ── Hero ───────────────────────────────────────────────
            Div(
                Row(
                    Col(
                        Div(
                            # Floating award badge
                            Div(
                                Badge(
                                    Icon("award-fill", cls="me-1 text-warning"),
                                    "Forbes Five-Star · 2026",
                                    variant="light",
                                    cls="au-float-badge",
                                    style="background:rgba(255,255,255,0.12)!important;color:#fff;border:1px solid rgba(201,168,76,0.35);",
                                ),
                                cls="mb-3",
                            ),
                            H1(
                                "Your Trusted Partner",
                                Br(),
                                "for Memorable Stays.",
                                cls=f"display-4 text-white fw-700 {Fx.slide_up}",
                            ),
                            Div(cls="au-gold-divider"),
                            P(
                                "Experience unmatched hospitality in rooms designed for comfort, "
                                "elegance, and unforgettable moments. From city breaks to extended escapes.",
                                cls=f"text-light mb-4 fs-5 {Fx.fade_in} {Fx.delay_sm}",
                            ),
                            # Live demand badge
                            AutoRefresh(
                                endpoint="/api/live-demand",
                                target="this",
                                interval=8000,
                                content=Div("Checking live demand…", cls="text-light small"),
                                cls="mb-3",
                            ),
                            cls="p-5",
                        ),
                        lg=7,
                    ),
                    Col(
                        Div(
                            # Booking form
                            Div(
                                H4(
                                    "Find Your Stay",
                                    cls="mb-3 fw-700",
                                    style="font-family:'Cormorant Garamond',serif;",
                                ),
                                FormGroup(
                                    Input("checkin", input_type="date"),
                                    label="Check In",
                                ),
                                FormGroup(
                                    Input("checkout", input_type="date"),
                                    label="Check Out",
                                ),
                                FormGroup(
                                    Select(
                                        "guests",
                                        ("1", "1 Guest"),
                                        ("2", "2 Guests", True),
                                        ("3", "3 Guests"),
                                        ("4", "4+ Guests"),
                                    ),
                                    label="Guests",
                                ),
                                LoadingButton(
                                    Icon("search", cls="me-2"),
                                    "Search Rooms",
                                    endpoint="/api/check-availability",
                                    target="#booking-result",
                                    variant="primary",
                                    cls="w-100 fw-600",
                                    style="background:#C9A84C;border-color:#C9A84C;border-radius:50px;",
                                ),
                                Div(id="booking-result", cls="mt-3"),
                                cls="au-booking-card p-4",
                            ),
                            cls="p-3",
                        ),
                        lg=5,
                    ),
                    cls="",
                    cols=1,
                    cols_lg=2,
                ),
                id="home",
                cls="au-hero mt-3",
            ),
            # ── Amenities Strip ────────────────────────────────────
            Div(
                Div(
                    *[
                        Div(
                            Div(Icon(icon), cls="au-amenity-icon"),
                            Div(label, cls="au-amenity-label"),
                            Div(sub, cls="au-amenity-sublabel"),
                            cls="au-amenity-item",
                        )
                        for icon, label, sub in AMENITIES
                    ],
                    cls="d-flex justify-content-center flex-wrap gap-0",
                ),
                cls="au-amenities-strip",
            ),
            # ── Room Search + Listing ──────────────────────────────
            Div(
                H2("Our Rooms & Suites", cls="fw-700 text-center mb-1"),
                Span(
                    "handcrafted for every kind of traveller",
                    cls="au-section-overline text-center d-block mb-4",
                ),
                Div(
                    ActiveSearch(
                        endpoint="/api/search-rooms",
                        target="#room-search-results",
                        placeholder="Search rooms (e.g. suite, twin, family)…",
                        debounce=250,
                    ),
                    cls="mb-3",
                ),
                Div(id="room-search-results"),
                Row(
                    *[Col(room_card(r, i), cls="mb-4") for i, r in enumerate(ROOMS)],
                    cls="g-3",
                    cols=1,
                    cols_md=2,
                    cols_lg=4,
                ),
                id="rooms",
                cls="mt-5",
            ),
            # ── Story + Team ───────────────────────────────────────
            Div(
                H2("Every Stay Has a Story", cls="fw-700 mb-3"),
                LazyLoad(
                    endpoint="/api/lazy-testimonials",
                    placeholder=Div(
                        Icon("three-dots", cls="me-2 text-muted"),
                        "Loading guest stories…",
                        cls="text-muted small",
                    ),
                ),
                H2("The Heart of Every Great Stay", cls="fw-700 mt-5 mb-3"),
                Row(
                    *[
                        Col(
                            Card(
                                Img(
                                    src=img,
                                    cls="w-100 rounded-top object-fit-cover",
                                    style="height:220px;",
                                ),
                                Div(
                                    Strong(name, cls="d-block"),
                                    P(role, cls="small text-muted mb-0"),
                                    cls="p-3 text-center",
                                ),
                                cls=f"border-0 shadow-sm h-100 {Fx.fade_in} {Fx.hover_lift}",
                                style="border-radius:16px;overflow:hidden;",
                            ),
                            cls="mb-3",
                        )
                        for name, role, img in TEAM
                    ],
                    cls="g-3",
                    cols=1,
                    cols_md=2,
                    cols_lg=4,
                ),
                cls="au-story-section mt-5",
            ),
            # ── Offers ─────────────────────────────────────────────
            Div(
                H2("Indulge in Luxury for Less", cls="fw-700 mb-1"),
                Span("limited-time exclusive packages", cls="au-section-overline d-block mb-4"),
                LazyLoad(
                    endpoint="/api/lazy-offers",
                    placeholder=Div("Loading offers…", cls="text-muted small"),
                ),
                id="deals",
                cls="mt-5",
            ),
            # ── CTA ───────────────────────────────────────────────
            Div(
                Row(
                    Col(
                        Div(
                            Span("reserve your stay", cls="au-section-overline"),
                            H2(
                                "Make your reservation today\nand create lasting memories.",
                                cls="text-white fw-700",
                            ),
                            P(
                                "Fast booking, trusted support, and premium room experiences.",
                                cls="text-white-50 mt-2",
                            ),
                            cls="p-4",
                        ),
                        lg=7,
                    ),
                    Col(
                        Card(
                            H4(
                                "Get in Touch",
                                cls="fw-700 mb-3",
                                style="font-family:'Cormorant Garamond',serif;",
                            ),
                            FormGroup(Input("full_name", placeholder="Full Name"), label="Name"),
                            FormGroup(
                                Input("email", input_type="email", placeholder="Email"),
                                label="Email",
                            ),
                            FormGroup(Input("phone", placeholder="Phone"), label="Phone"),
                            Button(
                                Icon("send-fill", cls="me-2"),
                                "Send Message",
                                cls="btn w-100 fw-600",
                                style="background:#C9A84C;color:#fff;border-radius:50px;",
                            ),
                            cls="border-0 shadow",
                            style="border-radius:16px;",
                        ),
                        lg=5,
                    ),
                    cls="g-3 align-items-center",
                    cols=1,
                    cols_lg=2,
                ),
                id="contact",
                cls="au-cta mt-5",
            ),
            # ── Footer ────────────────────────────────────────────
            FooterModern(
                brand="AURELIA",
                tagline="From business retreats to family vacations — we make every stay remarkable.",
                columns=[
                    {
                        "title": "Services",
                        "links": [
                            {"text": "Room Booking", "href": "#rooms"},
                            {"text": "Special Offers", "href": "#deals"},
                            {"text": "Contact", "href": "#contact"},
                        ],
                    },
                    {
                        "title": "Company",
                        "links": [
                            {"text": "About Us", "href": "#"},
                            {"text": "Careers", "href": "#"},
                            {"text": "Terms", "href": "#"},
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
                cls="rounded-4 mt-4",
                copyright_text="© 2026 Aurelia Hotels. All rights reserved.",
            ),
            cls="py-4",
        ),
        cls="container-xl",
    )


# ── API ─────────────────────────────────────────────────────────────────────────


@app.get("/api/live-demand")
def live_demand() -> Any:
    count = random.randint(24, 89)
    now = datetime.now().strftime("%H:%M")
    return Div(
        Icon("circle-fill", cls="me-1 text-danger", style="font-size:0.5rem;"),
        Badge(f"{count} travelers viewing now", variant="danger", cls="me-2"),
        Span(f"updated {now}", cls="small text-light opacity-75"),
        cls="d-flex align-items-center",
    )


@app.post("/api/check-availability")
def check_availability() -> Any:
    return toast_response(
        content=Alert(
            Icon("check-circle-fill", cls="me-2"),
            "Rooms available! Scroll down to choose your preferred stay.",
            variant="success",
        ),
        message="Availability confirmed.",
        variant="success",
    )


@app.get("/api/search-rooms")
def search_rooms(q: str = "") -> Any:
    query = q.strip().lower()
    if len(query) < 2:
        return ""
    matches = [r for r in ROOMS if query in r["name"].lower() or query in r["desc"].lower()]
    if not matches:
        return Div(
            Icon("info-circle", cls="me-2"),
            "No matching rooms found — try 'suite', 'twin', or 'deluxe'.",
            cls="alert alert-warning",
        )
    return Row(
        *[Col(room_card(r, i), md=6, cols=12, cls="mb-3") for i, r in enumerate(matches)],
        cls="g-3 mb-3",
    )


@app.get("/api/lazy-testimonials")
def lazy_testimonials() -> Any:
    return Row(
        *[
            Col(
                Testimonial(
                    quote=q,
                    author=a,
                    role=city,
                    rating=5,
                    cls=f"{Fx.fade_in}",
                ),
                lg=4,
                cols=12,
                cls="mb-3",
            )
            for q, a, city in TESTIMONIALS
        ],
        cls="g-3",
    )


@app.get("/api/lazy-offers")
def lazy_offers() -> Any:
    return Row(
        *[
            Col(
                Card(
                    Div(
                        Img(
                            src=img, cls="w-100 rounded-top object-fit-cover", style="height:180px;"
                        ),
                        style="overflow:hidden;",
                    ),
                    Div(
                        Badge(
                            Icon("tag-fill", cls="me-1"),
                            badge,
                            variant="warning",
                            cls="text-dark fw-700 mb-2",
                        ),
                        Strong(title, cls="d-block mb-2"),
                        Button(
                            Icon("calendar-check-fill", cls="me-1"),
                            "Book Offer",
                            cls="btn btn-sm fw-600",
                            style="background:#C9A84C;color:#fff;border-radius:50px;",
                        ),
                        cls="p-3",
                    ),
                    cls=f"border-0 shadow-sm h-100 {Fx.fade_in} {Fx.hover_lift}",
                    style="border-radius:14px;overflow:hidden;",
                ),
                lg=4,
                cols=12,
                cls="mb-3",
            )
            for title, badge, img in OFFERS
        ],
        cls="g-3",
    )


if __name__ == "__main__":
    serve(port=5015)
