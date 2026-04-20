# App Repo AGENTS Template

Place a file like this in the root of any new FastHTML + Faststrap app repository.

```md
# App Build Guide

This repository is a real FastHTML application built with Faststrap.

## Required first reads

Before making UI changes, inspect:

1. `main.py` or the app entrypoint
2. the shared theme/defaults module
3. the main layout shell
4. the app CSS file
5. the closest route/page module for the task
6. the relevant Faststrap component docs/examples for the page features you need

## Framework reference

The Faststrap framework repo lives at:

- `C:/path/to/Faststrap`

Before building, inspect these framework references:

- `C:/path/to/Faststrap/AGENTS.md`
- `C:/path/to/Faststrap/showcase/novaflow_ai_saas.py`
- `C:/path/to/Faststrap/showcase/northstar_ops_dashboard.py`
- `C:/path/to/Faststrap/showcase/hotel_booking_showcase.py`

## Local gold-standard reference apps

Use these projects as the visual and architectural bar:

- `C:/path/to/NIS`
- `C:/path/to/another/reference-app`

Inspect the closest matching files before writing code.

## UI quality bar

- The result must feel production-grade, branded, and intentional.
- Avoid generic Bootstrap-looking pages.
- Use Faststrap components plus custom CSS for polish.
- Respect responsive layout, spacing rhythm, typography hierarchy, and section contrast.
- Do not ship a plain hero-card-grid-footer layout unless the brief explicitly calls for it.
- Build mobile-first: if two cards or columns sit side by side on desktop, explicitly define the stacked mobile state first with Bootstrap/Faststrap row controls like `cols=1, cols_md=2` or `cols=1, cols_lg=2`.
- If a secondary/highlight card is too dense for mobile or tablet, hide it with Bootstrap display utilities like `d-none d-lg-block` rather than forcing it into a cramped small-screen layout.
- Before finishing, do a dedicated "Bootstrap smell" pass: remove pill-heavy defaults, weak shadows, over-rounded controls, and generic untouched sections.

## Accessibility and state rules

- Keep headings semantic and ordered.
- Preserve visible focus states.
- Ensure icon-only controls have accessible labels.
- Check empty, loading, success, and error states for key interactions before calling the page done.
- Do not rely on color alone to carry important meaning.

## Implementation priority

- Use Faststrap and Bootstrap capabilities first for layout, spacing, responsiveness, visibility control, and component behavior.
- Before inventing a new section or widget, inspect whether Faststrap already has a component or pattern that can cover most of the need.
- Use HTMX first for interaction and partial updates.
- Use custom CSS mainly for brand feel, modern visuals, and refinements Bootstrap does not already solve well.
- Use JavaScript only when HTMX/Bootstrap cannot do the job cleanly or when browser/PWA APIs are required.
- Do not add external CSS CDNs for styling.
- In single-file showcases, inline `Style(...)` is acceptable. In multi-route apps, move custom CSS into local assets rather than scattering large inline style blocks across route files.

## Architecture rules

- Keep theme tokens and component defaults centralized.
- Keep layout shells separate from page business logic.
- Split routes/modules by area when the app is multi-page.
- Prefer existing Faststrap components and patterns before inventing raw HTML structures.

## Completion checklist

- Mobile and desktop both checked
- Shared theme/defaults applied consistently
- Custom CSS added where needed for polish
- Empty/loading/error states considered
- Accessibility labels and focus states checked
- Typography scale and spacing rhythm reviewed
- Relevant tests run
```
