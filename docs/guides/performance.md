# Performance Considerations

Faststrap is intentionally lightweight, but performance still depends on how much HTML you render, which assets you load, and whether interactive features are server-side or client-side.

## DataTable Size

Client-side `DataTable` is best for small and medium datasets. For large datasets, use server-side pagination and filtering.

Recommended rule of thumb:

| Rows | Recommendation |
| --- | --- |
| `0-500` | Client-side rendering is usually fine. |
| `500-1,000` | Client-side is acceptable if columns are few and pages are simple. |
| `1,000+` | Prefer server-side pagination/search/sort. |

The paginator renders a bounded window, but the table body itself still costs HTML size, serialization time, and browser layout work.

## Reuse External Assets

Some optional components can inject third-party assets:

| Component | Asset note |
| --- | --- |
| `MapView` | Leaflet CSS/JS can be injected once, then reuse with `include_assets=False`. |
| `Chart` | Plotly can include JS with `include_js=True`; avoid repeating this when already loaded. |
| `Markdown` / `Svg` | Sanitization imports optional Python dependencies. |
| `Mermaid` | Requires Mermaid.js on the page. |
| `GSAP` | Optional integration; not needed for core animations. |

## CDN vs Local Assets

Use CDN assets for serverless deployments where local static mounting may be awkward.

Use local assets when:

- You want offline-friendly behavior.
- You need tighter control of asset versions.
- You are deploying a long-running ASGI app with static file support.

## Bootstrap Icons

Bootstrap Icons CSS and fonts add extra network weight. Keep it enabled for icon-heavy apps, but consider disabling or replacing it if your app uses very few icons.

## HTMX Patterns

HTMX can reduce initial page weight by loading expensive content on demand:

- Use `LazyLoad` for below-the-fold widgets.
- Use `ActiveSearch` for server-side search instead of shipping large option lists.
- Use server-side `DataTable` mode for large tabular data.
- Use `SSETarget` only where live updates are genuinely needed.

## PWA Precaching

PWA setup can precache core assets. This improves repeat visits but increases first service-worker install work. Keep optional assets out of the precache list unless they are needed on most visits.

## Custom CSS

Premium pages often need custom CSS, but keep the architecture deliberate:

- Prefer reusable class hooks over large inline style blocks.
- Use `theme_variant_css()` for paired light/dark variants.
- Avoid repeating large `Style()` blocks across every route.

## Measuring

When a page feels slow, inspect:

- HTML response size.
- Number and size of CSS/JS assets.
- Server render time for large tables or charts.
- Browser layout cost for huge DOM trees.
- Repeated third-party scripts included by optional components.
