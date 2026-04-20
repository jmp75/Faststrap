# Faststrap Showcase

This directory is the flagship reference layer for Faststrap.

Unlike the smaller examples in `examples/`, the files here are intended to show what Faststrap looks like when used for polished, production-style work.

## Purpose

Showcase apps should:

- attract new users to the framework
- prove Faststrap can build premium interfaces
- serve as the primary design references for docs, skills, and future sample work

## Current Reference Status

### Current flagship references

These are the strongest internal showcase files and should be treated as the first stop for visual inspiration, AI reference work, and docs screenshots:

- `novaflow_ai_saas.py`
- `northstar_ops_dashboard.py`
- `agency_portfolio.py`
- `hotel_booking_showcase.py`
- `furniture_store_showcase.py`
- `carenest_clinic.py`
- `ledgerleaf_finance.py`
- `learnloop_academy.py`
- `lexbridge_corporate.py`
- `forgedocs_platform.py`

Compact reference:

- `fastcloud_generated_saas.py` - minimal good example; smaller than the flagship SaaS files but still polished enough to copy from

External benchmark:

- `C:/Users/Meshell/Desktop/FastHTML/mmercyj_beddings`

### Legacy but still useful

These are still worth keeping around, but they should not be the primary references for new work:

- `saas_landing.py`
- `admin_dashboard.py`

See `SHOWCASE_PROGRAM_PLAN.md` for the full roadmap, gap analysis, and component coverage plan.

## Showcase Standards

Every flagship showcase should:

- use a strong visual direction
- use custom typography
- use a real Faststrap theme or `create_theme(...)`
- include a polished custom CSS layer
- feel mobile-first and production-ready
- demonstrate meaningful Faststrap component usage
- avoid placeholder content and stale version strings
- use readable, copyable reference-grade code

## Screenshot Convention

When adding showcase screenshots for docs/README, place them in:

- `docs/assets/showcase/`

Recommended filenames:

- `novaflow-ai-saas-light.png`
- `novaflow-ai-saas-dark.png`
- `northstar-ops-dashboard-light.png`
- `northstar-ops-dashboard-dark.png`

Use lowercase kebab-case so docs pages and README references stay predictable.

## Separation Of Concerns

Use:

- `examples/` for learning and focused component demos
- `showcase/` for aspirational, polished, flagship references

If an app is useful for teaching but not visually exceptional, it belongs in `examples/`, not here.
