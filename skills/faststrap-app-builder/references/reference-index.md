# Faststrap Reference Index

Use this file as the first-stop reference map before building a Faststrap app.

The goal is simple:

- pick one primary reference before coding
- pick one secondary reference only if it adds something specific
- prefer flagship references over legacy/simple ones unless the user explicitly wants a smaller or plainer build

Do not combine three or four unrelated visual directions into one app.

---

## Selection Workflow

1. Identify the page/app type.
2. Pick the strongest matching flagship reference below.
3. Add one secondary reference only if you need a specific pattern:
   - auth flow
   - mobile-first company-site simplification
   - dashboard shell wiring
   - PWA/browser API behavior
4. Reuse structure and quality bar, not literal copy.

---

## By Page Type

### SaaS Landing / Product Marketing

Primary choices:

- `Faststrap/showcase/novaflow_ai_saas.py`
  - flagship SaaS/product reference
  - strongest choice for premium hierarchy, polished surfaces, and HTMX-enhanced product marketing
- `Faststrap/showcase/hotel_booking_showcase.py`
  - use when the brief needs a more editorial, premium, or luxury landing-page tone
- `Faststrap/showcase/generated_saas.py`
  - use as a smaller polished SaaS reference when the user does not need the full flagship scale
- `Faststrap/showcase/fastcloud_generated_saas.py`
  - compact showcase reference
  - useful as a simpler teaching/example surface, not the premium benchmark
- `Faststrap/showcase/saas_landing.py`
  - legacy/simple reference only
  - use when a lighter starting point is genuinely needed, not as the visual quality target

Pattern add-ons:

- `C:\Users\Meshell\Desktop\FastHTML\mmercyj_beddings\components.py`
- `C:\Users\Meshell\Desktop\FastHTML\mmercyj_beddings\routes.py`
- `Faststrap/skills/faststrap-app-builder/references/mmercyj-patterns.md`

Use the MMERCYJ references when you need:

- stronger company-site architecture
- clearer mobile-first hero simplification
- a polished small-business/site composition pattern

### Dashboard / Admin / Internal Tools

Primary choices:

- `Faststrap/showcase/northstar_ops_dashboard.py`
  - flagship dashboard/admin reference
  - strongest choice for KPI cards, filters, panels, and premium operational UI
- `Faststrap/showcase/analytics_dashboard.py`
  - compact analytics/dashboard reference with strong visual polish
- `Faststrap/showcase/admin_dashboard.py`
  - legacy/simple dashboard reference
  - use only when the user wants a lower-complexity starting point

Pattern add-ons:

- `C:\Users\Meshell\Desktop\FastHTML\NIS\app\presentation\components\ui\layout.py`
- `C:\Users\Meshell\Desktop\FastHTML\NIS\app\presentation\routes\hq\dashboard.py`
- `C:\Users\Meshell\Desktop\FastHTML\Final-Year\main.py`

Use these when you need:

- production-style shell wiring
- route-area separation
- theme/defaults modules in real apps

### Auth / Onboarding / Registration

Primary choices:

- `C:\Users\Meshell\Desktop\FastHTML\NIS\app\presentation\routes\auth.py`
- `C:\Users\Meshell\Desktop\FastHTML\NIS\app\presentation\routes\register.py`

Use these when the app needs:

- branded login/register flows
- multi-step onboarding
- non-generic form presentation
- custom background or auth-shell treatment

### Finance / FinTech / Mobile-First Product Flows

Primary choices:

- `Faststrap/showcase/ledgerleaf_finance.py`
  - best mobile-first financial/product reference
  - strong for bottom-nav patterns, sheets, account panels, and practical transactional UI

### Education / SaaS Platform

Primary choices:

- `Faststrap/showcase/learnloop_academy.py`
  - best learning/product platform reference
  - strong for dashboard-layout reuse, progress UI, tabs, and structured content surfaces

### E-commerce / Product Catalog / Brand Commerce

Primary choices:

- `Faststrap/showcase/furniture_store_showcase.py`
  - best warm e-commerce/product storytelling reference
  - strong for product cards, editorial merchandising, testimonials, and trust sections

### Agency / Portfolio / Corporate

Primary choices:

- `Faststrap/showcase/agency_portfolio.py`
- `Faststrap/showcase/lexbridge_corporate.py`

Use when the brief is:

- portfolio-forward
- corporate/professional
- service-business presentation

### Documentation / Developer Platform

Primary choice:

- `Faststrap/showcase/forgedocs_platform.py`

Use when the brief needs:

- technical documentation structure
- search/navigation-heavy docs UI
- reference sections and developer portal composition

### PWA / Browser-API-Heavy Work

Primary choices:

- `C:\Users\Meshell\Desktop\FastHTML\siwes-logbook-automation\main.py`
- `C:\Users\Meshell\Desktop\FastHTML\siwes-logbook-automation\app\presentation\components\shared\theme.py`
- `C:\Users\Meshell\Desktop\FastHTML\siwes-logbook-automation\app\presentation\assets\custom.css`

Use these when the app needs:

- PWA installability
- offline-first patterns
- service worker behavior
- browser APIs HTMX alone cannot cover

Do not use these as permission to default to JavaScript in ordinary Faststrap work.

---

## Reference Quality Matrix

Use this when several files look relevant and you need to choose fast.

| Reference | Best For | Quality Bar | Notes |
|---|---|---|---|
| `Faststrap/showcase/novaflow_ai_saas.py` | Premium SaaS landing | Flagship | strongest SaaS visual benchmark |
| `Faststrap/showcase/northstar_ops_dashboard.py` | Premium dashboard/admin | Flagship | strongest internal-tools benchmark |
| `Faststrap/showcase/hotel_booking_showcase.py` | Luxury/editorial landing | Premium | use for richer visual direction |
| `Faststrap/showcase/generated_saas.py` | Smaller polished SaaS | Good | simpler than Novaflow while still intentional |
| `Faststrap/showcase/analytics_dashboard.py` | Compact analytics UI | Good | smaller dashboard reference with polish |
| `Faststrap/showcase/ledgerleaf_finance.py` | FinTech/mobile-first flows | Good | strong transactional/mobile patterns |
| `Faststrap/showcase/learnloop_academy.py` | Education/platform UI | Good | progress, tabs, structured content |
| `Faststrap/showcase/furniture_store_showcase.py` | E-commerce/brand commerce | Good | warm product storytelling |
| `Faststrap/showcase/agency_portfolio.py` | Agency/portfolio | Good | presentation-led structure |
| `Faststrap/showcase/admin_dashboard.py` | Simpler dashboard | Legacy | lower bar than Northstar |
| `Faststrap/showcase/saas_landing.py` | Simpler SaaS starter | Legacy | lower bar than Novaflow |
| `Faststrap/showcase/fastcloud_generated_saas.py` | Compact/simple SaaS example | Secondary | useful as a small example, not flagship bar |

---

## Reference Rules

- Prefer the flagship reference when both flagship and legacy options exist.
- Use legacy/simple references only when the user explicitly wants lower complexity, faster iteration, or a plainer starting point.
- If the user asks for "premium", "flagship", "modern", or "production-grade", do not anchor on a legacy example.
- For dashboards, do not treat `admin_dashboard.py` as equal to `northstar_ops_dashboard.py`.
- For SaaS marketing, do not treat `saas_landing.py` or `fastcloud_generated_saas.py` as equal to `novaflow_ai_saas.py`.

---

## Supporting References

These are not the first visual pick, but they are often the right second reference.

- `Faststrap/skills/faststrap-app-builder/references/nis-patterns.md`
  - production app wiring, theme modules, route composition, and layout structure
- `Faststrap/skills/faststrap-app-builder/references/mmercyj-patterns.md`
  - company-site composition and mobile-first hero simplification
- `Faststrap/skills/faststrap-app-builder/references/reference-apps.md`
  - detailed file list and supporting notes
- `Faststrap/skills/faststrap-app-builder/references/project-agents-template.md`
  - template instructions for fresh app repos

Start here, then open the specific follow-up reference only when needed.
