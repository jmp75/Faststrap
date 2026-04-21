# Showcase Gallery

Faststrap now keeps a dedicated `showcase/` layer for polished, production-style references.

These apps are not tiny component demos. They are intentionally built to prove that Faststrap can carry:

- premium landing pages
- dense internal dashboards
- vertical product sites
- polished client-facing web apps

## Why This Matters

The small examples in `examples/` are still useful for learning, but they do not fully communicate the ceiling of the framework.

The showcase layer exists to do three things:

1. give adopters real, aspirational references
2. give AI builders better composition examples
3. help docs and README communicate visual confidence, not just API breadth

## Current Flagship Set

### Product and SaaS

- `showcase/novaflow_ai_saas.py`
- `showcase/fastcloud_generated_saas.py` (compact minimal-good reference)
- `showcase/saas_landing.py` (legacy reference, no longer the primary SaaS bar)

### Dashboards and Data

- `showcase/northstar_ops_dashboard.py`
- `showcase/admin_dashboard.py` (legacy reference)
- `showcase/ledgerleaf_finance.py`

### Portfolio and Brand Sites

- `showcase/agency_portfolio.py`
- `showcase/lexbridge_corporate.py`

### Commerce and Hospitality

- `showcase/furniture_store_showcase.py`
- `showcase/hotel_booking_showcase.py`

### Vertical Product Apps

- `showcase/carenest_clinic.py`
- `showcase/learnloop_academy.py`
- `showcase/forgedocs_platform.py`

## Screenshot Folder

To keep screenshot usage consistent across docs and README, place showcase screenshots in:

- `docs/assets/showcase/`

Recommended naming:

- `novaflow-ai-saas-light.png`
- `novaflow-ai-saas-dark.png`
- `northstar-ops-dashboard-light.png`
- `northstar-ops-dashboard-dark.png`

When screenshots are added, the individual showcase pages should reference those files directly.

## What These Pages Should Demonstrate

Each flagship showcase should prove a few things clearly:

- strong Bootstrap-first structure with Faststrap components
- minimal JavaScript and HTMX-first interactions where possible
- custom CSS polish without looking like raw Bootstrap defaults
- real mobile responsiveness
- real product surfaces instead of one-off component dumps

See `showcase/README.md` and `SHOWCASE_PROGRAM_PLAN.md` for the internal standards and rollout plan.
