# Faststrap Showcase Program Plan

This document defines the new flagship showcase strategy for Faststrap.

The goal is to make Faststrap look as capable as it actually is.

Right now, the framework's examples are stronger at teaching features than at selling aspiration. The next showcase wave should fix that by creating a set of polished, high-fidelity reference apps that demonstrate:

- premium visual quality
- production-style composition
- broad component coverage
- strong HTMX and preset usage
- distinctive design directions across categories

## Why This Matters

Faststrap already has a large public surface area with data, layout, form, feedback, navigation, SEO, PWA, and preset utilities. However, the current public sample layer undersells that capability.

Current problems:

- no clear flagship tier distinct from learning demos
- too many examples that feel like internal demos instead of real products
- stale references and outdated version strings in some showcase files
- under-demonstration of newer or more advanced components
- inconsistent visual fidelity across showcase files
- old examples still occupying "gold standard" reference status in practice

## Audit Summary

### Current strengths

These are the current strongest visual references:

- `showcase/hotel_booking_showcase.py`
- `showcase/furniture_store_showcase.py`
- `showcase/agency_portfolio.py`
- external benchmark: `C:/Users/Meshell/Desktop/FastHTML/mmercyj_beddings`

### Current weaknesses

These should not remain primary flagship references without major rebuilds:

- `showcase/saas_landing.py`
- `showcase/admin_dashboard.py`
- `examples/landing_demo.py`
- `examples/patterns_demo.py`
- `examples/phase5_demo.py`
- `examples/05_examples/portfolio_demo.py`
- `examples/05_examples/portfolio_demo2.py`
- `examples/showcase/portfolio_standard.py`
- `examples/showcase/portfolio_premium.py`

### Public-surface demo gap

Several exported Faststrap features are still absent or barely represented in examples/showcases. High-priority under-demonstrated surfaces include:

- `DashboardGrid`
- `DateRangePicker`
- `FormBuilder`
- `FormErrorSummary`
- `Mermaid`
- `Svg`
- `NotificationCenter`
- `ExportButton`
- `MultiSelect`
- `RangeSlider`
- `BottomNav`
- `Sheet`
- `Figure`
- `AuthLayout`

## Strategy

Split the sample ecosystem into two deliberate tiers:

### 1. Learning examples

Location:

- `examples/`

Purpose:

- explain components
- teach patterns
- provide focused, small examples

Allowed to be:

- simpler
- narrower
- less visually ambitious

### 2. Flagship showcases

Location:

- `showcase/`

Purpose:

- attract developers
- prove the framework can ship premium UIs
- act as the primary design reference set
- feed docs, README, skills, and marketing assets

Required to be:

- visually polished
- product-like
- mobile-first
- intentionally themed
- component-rich without feeling like a demo grid

## Showcase Quality Standard

Every flagship showcase must meet all of the following:

1. Use a deliberate visual system
- custom `font_family`
- explicit theme choice or `create_theme(...)`
- custom CSS layer for atmosphere and brand polish

2. Feel like a real product
- believable copy
- realistic CTA hierarchy
- no placeholder sections
- no "chart goes here" messaging
- no "inspired by uploaded design" comments

3. Be mobile-first
- mobile stack defined intentionally first
- responsive breakpoints explicit
- dense secondary content hidden or simplified on smaller screens where needed

4. Demonstrate Faststrap meaningfully
- at least 8 relevant components used in context
- at least 1 preset or advanced interaction
- HTMX-first where appropriate
- `Fx` classes used deliberately

5. Be reference-grade code
- no wildcard imports
- no stale version strings
- no dead demo artifacts
- readable file structure
- clear data/setup organization

## The 10 Flagship Showcases

### Wave 1

These three become the first new gold-standard references and should be built first.

1. `showcase/novaflow_ai_saas.py`
- category: AI SaaS / B2B product marketing
- role: replaces weak/default SaaS references
- target components:
  - `NavbarModern`
  - `Hero`
  - `FeatureGrid`
  - `PricingGroup`
  - `TestimonialSection`
  - `ThemeToggle`
  - `LoadingButton`
  - `ActiveSearch`
  - `ToastContainer`
  - `FooterModern`

2. `showcase/northstar_ops_dashboard.py`
- category: analytics / admin webapp
- role: primary dashboard reference
- target components:
  - `DashboardLayout`
  - `DashboardGrid`
  - `MetricCard`
  - `TrendCard`
  - `KPICard`
  - `Chart`
  - `DataTable`
  - `FilterBar`
  - `DateRangePicker`
  - `MultiSelect`
  - `RangeSlider`
  - `ExportButton`
  - `NotificationCenter`

3. `showcase/atelier_studio_portfolio.py`
- category: creative agency / premium portfolio
- role: primary portfolio reference
- target components:
  - `GlassNavbar`
  - `Carousel`
  - `Figure`
  - `TestimonialSection`
  - `LoadingButton`
  - `InfiniteScroll`
  - `ToastContainer`
  - `Badge`
  - `Card`
  - `Fx.glass`

### Wave 2

4. `showcase/haven_resort_booking.py`
- category: hospitality / travel / booking
- target components:
  - `Hero`
  - `FormGroup`
  - `SearchableSelect`
  - `DateRangePicker`
  - `LoadingButton`
  - `LazyLoad`
  - `AutoRefresh`
  - `Testimonial`
  - `Alert`
  - `FooterModern`

5. `showcase/oak_and_linen_store.py`
- category: ecommerce / home decor
- target components:
  - `Navbar`
  - `Card`
  - `Badge`
  - `Carousel`
  - `Tabs`
  - `Drawer`
  - `Dropdown`
  - `Pagination`
  - `Toast`
  - `ButtonGroup`

6. `showcase/lexbridge_corporate.py`
- category: consulting / law / corporate
- target components:
  - `NavbarModern`
  - `Breadcrumb`
  - `Accordion`
  - `FooterModern`
  - `PageMeta`
  - `StructuredData`
  - `Card`
  - `EmptyState`
  - `Button`
  - `Hero`

### Wave 3

7. `showcase/ledgerleaf_finance.py`
- category: fintech / finance portal
- target components:
  - `Chart`
  - `DataTable`
  - `KPICard`
  - `MetricCard`
  - `NotificationCenter`
  - `ExportButton`
  - `FilterBar`
  - `RangeSlider`
  - `BottomNav`
  - `Sheet`

8. `showcase/carenest_clinic.py`
- category: healthcare / appointment / trust-heavy site
- target components:
  - `AuthLayout`
  - `FormBuilder`
  - `FormErrorSummary`
  - `DateRangePicker`
  - `InputGroup`
  - `Select`
  - `NoticeAlert`
  - `Modal`
  - `Button`
  - `Card`

9. `showcase/learnloop_academy.py`
- category: edtech / learning platform
- target components:
  - `DashboardLayout`
  - `Progress`
  - `Tabs`
  - `Accordion`
  - `MetricCard`
  - `Chart`
  - `FilterBar`
  - `NotificationCenter`
  - `BottomNav`
  - `Badge`

10. `showcase/forgedocs_platform.py`
- category: developer docs / platform site
- target components:
  - `Markdown`
  - `Mermaid`
  - `Svg`
  - `Table`
  - `Tabs`
  - `ThemeToggle`
  - `SearchableSelect`
  - `PageMeta`
  - `Toast`
  - `Navbar`

## Design Direction Per Showcase

Each flagship should have a distinct visual personality so Faststrap does not look one-note.

- `novaflow_ai_saas.py`
  - crisp editorial SaaS
  - cool neutrals + electric accent
  - premium product-marketing clarity

- `northstar_ops_dashboard.py`
  - dark command-center analytics
  - high-density clarity
  - strong dashboard information hierarchy

- `atelier_studio_portfolio.py`
  - moody cinematic creative studio
  - glass and glow accents
  - typography-led composition

- `haven_resort_booking.py`
  - warm hospitality
  - light, premium, photo-led
  - calm trust-oriented conversion

- `oak_and_linen_store.py`
  - tactile luxury retail
  - cream, walnut, charcoal
  - product-forward composition

- `lexbridge_corporate.py`
  - restrained premium enterprise
  - high-trust visual language
  - clean section rhythm

- `ledgerleaf_finance.py`
  - precision fintech
  - clear, dense, controlled
  - serious data-first tone

- `carenest_clinic.py`
  - bright, reassuring healthcare
  - accessible form flows
  - trust and clarity over spectacle

- `learnloop_academy.py`
  - energetic but structured
  - progress-focused and learner-friendly

- `forgedocs_platform.py`
  - technical sharpness
  - code, docs, diagrams, and clarity

## Recommended Execution Order

### Phase A - Foundation

1. Create `showcase/README.md`
2. Define flagship quality standards
3. List current showcase status and planned replacements
4. Add a simple component-coverage matrix per flagship

### Phase B - Build Wave 1

1. `showcase/novaflow_ai_saas.py`
2. `showcase/northstar_ops_dashboard.py`
3. `showcase/atelier_studio_portfolio.py`

These become the new skill references first.

### Phase C - Replace reference anchors

Update these after Wave 1 lands:

- `skills/faststrap-app-builder/references/reference-apps.md`
- any README showcase references
- docs/index showcase highlights if needed

### Phase D - Build Wave 2

1. `showcase/haven_resort_booking.py`
2. `showcase/oak_and_linen_store.py`
3. `showcase/lexbridge_corporate.py`

### Phase E - Build Wave 3

1. `showcase/ledgerleaf_finance.py`
2. `showcase/carenest_clinic.py`
3. `showcase/learnloop_academy.py`
4. `showcase/forgedocs_platform.py`

## Deliverables Per Showcase

Each showcase should ship with:

- runnable Python file in `showcase/`
- polished inline `Style(...)` or mounted local CSS
- component usage notes
- screenshot-ready home route
- mobile and desktop validation

Optional later additions:

- `showcase/assets/...`
- screenshots for README/docs
- a showcase gallery page in docs

## Acceptance Criteria

The showcase program is successful when:

1. Faststrap has at least 10 premium internal showcase apps
2. the skill reference set prefers those showcase files over weaker demos
3. major newer components are demonstrated in believable product contexts
4. the README and docs point to polished references first
5. a new user can look at the showcase layer and immediately see that Faststrap can build premium products

## Immediate Next Step

Start with:

1. `showcase/novaflow_ai_saas.py`

Why:

- SaaS landing pages are a common first evaluation path
- this is the fastest high-visibility win
- it can immediately replace weaker landing/marketing references in the skill layer

