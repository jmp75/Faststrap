# MMERCYJ patterns

Use `mmercyj_beddings` as a direct reference for polished company-site work built with FastHTML + Faststrap.

Primary local files:

- `C:\Users\Meshell\Desktop\FastHTML\mmercyj_beddings\app.py`
- `C:\Users\Meshell\Desktop\FastHTML\mmercyj_beddings\components.py`
- `C:\Users\Meshell\Desktop\FastHTML\mmercyj_beddings\routes.py`
- `C:\Users\Meshell\Desktop\FastHTML\mmercyj_beddings\content.py`

## What to copy from it

### App bootstrap

From `app.py`:

- keep the app entrypoint lean
- wire `add_bootstrap(app, theme=..., mode=...)`
- mount local assets with `mount_assets(...)`
- append project CSS after Faststrap
- separate route registration into a dedicated setup function

### Project organization

From the file split:

- keep reusable view pieces in `components.py`
- keep page/route assembly in `routes.py`
- keep editable site content/constants in a separate content module
- keep app startup/theme wiring separate from page composition

This is a strong pattern for small business sites, brand sites, and marketing-heavy multi-page apps.

### Hero composition

From `components.py`:

- build a strong hero around a primary message column and a secondary support/highlight card
- use Faststrap components such as `Carousel`, `Card`, `Badge`, `Button`, `Navbar`, `Container`, `Row`, and `Col` before inventing raw structures
- use layered composition: carousel/image layer, overlay layer, and content layer
- keep CTA hierarchy obvious and immediate

### Mobile-first responsive rule

This project is an important reference for one recurring Faststrap app-building lesson:

- when two cards or columns are horizontal on desktop, explicitly define the mobile stack first
- use patterns like `Row(..., cols=1, cols_lg=2)` or `Row(..., cols=1, cols_md=2)` rather than assuming desktop composition will collapse correctly
- if a support card is useful on desktop but too dense for small screens, hide it intentionally with Bootstrap display utilities such as `d-none d-lg-block`
- preserve the primary content column for all breakpoints and treat secondary dense cards as optional on mobile/tablet

This should be solved with Bootstrap/Faststrap layout utilities first, not with heavy custom responsive CSS.

### Visual tone

This app is a good reference for:

- polished small-business/company-site presentation
- modern but practical CTA-driven layouts
- custom CSS layered on top of Bootstrap rather than replacing Bootstrap
- realistic route/page structure instead of a single-file landing page

### What not to lose in future builds

When using this reference:

- do not flatten the architecture into one route file
- do not keep every desktop support card visible on mobile by default
- do not replace Bootstrap row/column/display behavior with unnecessary custom CSS
- do not drop back to generic hero-card-grid-footer composition without the stronger hierarchy and spacing shown here
