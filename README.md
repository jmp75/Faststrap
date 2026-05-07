# FastStrap

**Modern Bootstrap 5 components for FastHTML - Build beautiful web UIs in pure Python with zero JavaScript knowledge.**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastHTML](https://img.shields.io/badge/FastHTML-0.6+-green.svg)](https://fastht.ml/)
[![PyPI version](https://img.shields.io/pypi/v/faststrap.svg)](https://pypi.org/project/faststrap/)
[![Tests](https://github.com/Faststrap-org/Faststrap/workflows/Tests/badge.svg)](https://github.com/Faststrap-org/Faststrap/actions)

---

## Why FastStrap

FastHTML is amazing for building web apps in pure Python, but it lacks pre-built UI components. FastStrap fills that gap by providing:


 **145+ components, helpers, and presets** - 128 registered UI components plus HTMX, SEO, PWA, and optional integrations  
 **HTMX Presets Module** - 17 ready-to-use patterns for common interactions  
 **SEO Module** - Comprehensive meta tags, Open Graph, Twitter Cards, and structured data  
 **Zero JavaScript knowledge required** - Components just work  
 **No build steps** - Pure Python, no npm/webpack/vite  
 **Full HTMX integration** - Dynamic updates without page reloads  
 **Zero-JS animations by default** - Beautiful effects with pure CSS (`Fx`), with optional GSAP motion via `faststrap[gsap]`  
 **Dark mode built-in** - Automatic theme switching  
 **Type-safe** - Full type hints for better IDE support  
 **Pythonic API** - Intuitive kwargs style  
 **Enhanced customization** - Slot classes, CSS variables, themes, and more  
 **Docs and examples included** - Coverage is expanding

It also ships higher-level modules for HTMX presets, SEO metadata composition, and PWA setup so production concerns are covered alongside UI components.

---

## Quick Start

### Installation

```bash
pip install faststrap
```

### Hello World

```python
from fasthtml.common import FastHTML, serve
from faststrap import add_bootstrap, Card, Button, create_theme

app = FastHTML()

# Use built-in theme or create custom
theme = create_theme(primary="#7BA05B", secondary="#48C774")
add_bootstrap(app, theme=theme, mode="dark")

@app.route("/")
def home():
    return Card(
        "Welcome to FastStrap! Build beautiful UIs in pure Python.",
        header="Hello World!",
        footer=Button("Get Started", variant="primary")
    )

serve()
```

That's it! You now have a modern, responsive web app with zero JavaScript.

### Working with Static Files

Faststrap V0.5.1+ includes a helper to easily mount your own static files (images, CSS, etc.):

```python
from faststrap import mount_assets

# Mount your "assets" directory at "/assets" URL
mount_assets(app, "assets")

# Use in your app
Img(src="/assets/logo.png")
Div(style="background-image: url('/assets/hero.jpg')")
```

See [Static Files Guide](docs/STATIC_FILES.md) for more details.

---

## Enhanced Features

### 1. Enhanced Attribute Handling

Faststrap now supports advanced attribute handling:

```python
from faststrap import Button

# Style dict and CSS variables
Button(
    "Styled Button",
    style={"background-color": "#7BA05B", "border": "none"},
    css_vars={"--bs-btn-padding-y": "0.75rem", "--bs-btn-border-radius": "12px"},
    data={"id": "123", "type": "demo"},
    aria={"label": "Styled button"},
)

# Filter None/False values automatically
Button("Test", disabled=None, hidden=False)  # None/False values are dropped
```

### 2. CloseButton Helper

Reusable close button for alerts, modals, and drawers:

```python
from faststrap import CloseButton, Alert

# Use in alerts
Alert(
    "This alert uses CloseButton helper",
    variant="info",
    dismissible=True,
)

# Use in modals/drawers (automatically used)
```

### 3. Expanded Button Component

More control over button appearance and behavior:

```python
from faststrap import Button

# Render as link
Button("As Link", as_="a", href="/page", variant="secondary")

# Loading states with custom text
Button("Loading", loading=True, loading_text="Please wait...", spinner=True)

# Full width, pill, active states
Button("Full Width", full_width=True, variant="info")
Button("Pill", pill=True, variant="warning")
Button("Active", active=True, variant="success")

# Icon and spinner control
Button("Icon + Spinner", icon="check-circle", spinner=True, icon_pos="start")
```

### 4. Slot Class Overrides

Fine-grained control over component parts:

```python
from faststrap import Card, Modal, Drawer, Dropdown

# Card with custom slot classes
Card(
    "Content",
    header="Custom Header",
    footer="Custom Footer",
    header_cls="bg-primary text-white p-3",
    body_cls="p-4",
    footer_cls="text-muted",
)

# Modal with custom classes
Modal(
    "Modal content",
    title="Custom Modal",
    dialog_cls="shadow-lg",
    content_cls="border-0",
    header_cls="bg-primary text-white",
    body_cls="p-4",
)

# Drawer with custom classes
Drawer(
    "Drawer content",
    title="Custom Drawer",
    header_cls="bg-success text-white",
    body_cls="p-4",
)

# Dropdown with custom classes
Dropdown(
    "Option 1", "Option 2",
    label="Custom Dropdown",
    toggle_cls="custom-toggle",
    menu_cls="custom-menu",
    item_cls="custom-item",
)
```

### 5. Theme System

Create and apply custom themes:

```python
from faststrap import create_theme, add_bootstrap

# Create custom theme
my_theme = create_theme(
    primary="#7BA05B",
    secondary="#48C774",
    info="#36A3EB",
    warning="#FFC107",
    danger="#DC3545",
    success="#28A745",
    light="#F8F9FA",
    dark="#343A40",
)

# Use built-in themes
add_bootstrap(app, theme="green-nature")  # or "blue-ocean", "purple-magic", etc.

# Or use custom theme
add_bootstrap(app, theme=my_theme)
```

Available built-in themes:

- `green-nature`
- `blue-ocean`
- `purple-magic`
- `red-alert`
- `orange-sunset`
- `teal-oasis`
- `indigo-night`
- `pink-love`
- `cyan-sky`
- `gray-mist`

### 6. Registry Metadata And Discovery

Components include metadata about category, stability, and JavaScript requirements. The registry also helps developers and AI agents discover existing components before inventing new wrappers:

```python
from faststrap import (
    find_components,
    get_component,
    get_components_by_pattern,
    list_component_metadata,
    list_components,
)

components = list_components(category="display")
cards = find_components("card")
toast_components = get_components_by_pattern("toast")
metadata = list_component_metadata()

# Check if component requires JS
modal = get_component("Modal")
# Modal is registered with requires_js=True
```

---

## Available Components And Helpers (145+ Total)

Faststrap currently exposes **128 registered UI components** across forms, display, feedback, navigation, layout, and patterns, plus **17 HTMX presets**, SEO/PWA helpers, accessibility helpers, core utilities, and optional integrations. Components are typed, HTMX-friendly, and follow Bootstrap conventions. Stability markers (`@stable`, `@beta`, `@experimental`) indicate API maturity.

### Presets Module (17 Utilities)

- `ActiveSearch`
- `InfiniteScroll`
- `AutoRefresh`
- `LazyLoad`
- `LoadingButton`
- `OptimisticAction`
- `LocationAction`
- `hx_redirect`
- `hx_refresh`
- `hx_trigger`
- `hx_reswap`
- `hx_retarget`
- `toast_response`
- `SSEStream`
- `sse_event`
- `sse_comment`
- `@require_auth`

### Forms (33 Public Components / Helpers)

- `Button`
- `ButtonGroup`
- `ButtonToolbar`
- `CalendarDatePicker`
- `Checkbox`
- `CloseButton`
- `DateRangePicker`
- `ExportButton`
- `FileInput`
- `FilterBar`
- `FloatingLabel`
- `Form`
- `FormBuilder`
- `FormErrorSummary`
- `FormGroup`
- `FormGroupFromErrors`
- `FormWizard`
- `Input`
- `InputGroup`
- `InputGroupText`
- `InlineEditor`
- `LiveValidationField`
- `MultiSelect`
- `Radio`
- `Range`
- `RangeSlider`
- `SearchableSelect`
- `Select`
- `Switch`
- `ThemeToggle`
- `ToggleGroup`
- `ValidationMessage`
- `WizardStep`

### Display (34 Components + 5 table aliases)

- `Avatar`
- `AvatarGroup`
- `Badge`
- `BadgeGroup`
- `Card`
- `Carousel`
- `CarouselItem`
- `Chart`
- `DataTable`
- `EmptyState`
- `Figure`
- `Image`
- `KPICard`
- `MapView`
- `Markdown`
- `Mermaid`
- `MetricCard`
- `ResultCard`
- `Sheet`
- `SSETarget`
- `StatCard`
- `StatusBadge`
- `Stepper`
- `StepperStep`
- `Svg`
- `BsTable` / `BsTHead` / `BsTBody` / `BsTRow` / `BsTCell`
- `Table`
- `THead`
- `TBody`
- `TRow`
- `TCell`
- `TextClamp`
- `Timeline`
- `TimelineItem`
- `TrendCard`

### v0.6.1 Naming Notes

- `FormBuilder` is now the preferred name for the Pydantic form builder API. If you are on `v0.6.0` or earlier, keep using `Form.from_pydantic()`. In `v0.6.1+`, prefer `FormBuilder.from_pydantic()`. `Form` remains as a compatibility alias.
- `Table`, `THead`, `TBody`, `TRow`, and `TCell` remain the primary table API. `v0.6.1` adds optional aliases `BsTable`, `BsTHead`, `BsTBody`, `BsTRow`, and `BsTCell` for projects that import both FastHTML and Faststrap table primitives.

### Feedback (27 Components)

- `Alert`
- `ConfirmAction`
- `ConfirmDialog`
- `ErrorDialog`
- `ErrorPage`
- `ErrorToast`
- `InfoToast`
- `InstallPrompt`
- `Modal`
- `ModernToast`
- `ModernToastStack`
- `NoticeAlert`
- `NoticeToast`
- `NotificationCenter`
- `Placeholder`
- `PlaceholderButton`
- `PlaceholderCard`
- `Popover`
- `Progress`
- `ProgressBar`
- `SimpleToast`
- `Spinner`
- `SuccessToast`
- `Toast`
- `ToastContainer`
- `Tooltip`
- `WarningToast`

### Navigation (23 Components)

- `Accordion`
- `AccordionItem`
- `BottomNav`
- `BottomNavItem`
- `Breadcrumb`
- `Collapse`
- `CommandItem`
- `CommandPalette`
- `Drawer`
- `Dropdown`
- `DropdownDivider`
- `DropdownItem`
- `GlassNavbar`
- `GlassNavItem`
- `ListGroup`
- `ListGroupItem`
- `Navbar`
- `Pagination`
- `Scrollspy`
- `SidebarNavbar`
- `SidebarNavItem`
- `TabPane`
- `Tabs`

### Layout (5 Components)

- `Container`
- `Row`
- `Col`
- `Hero`
- `DashboardGrid`

### Patterns (8 Composed Components)

- `Feature`
- `FeatureGrid`
- `FooterModern`
- `NavbarModern`
- `PricingGroup`
- `PricingTier`
- `Testimonial`
- `TestimonialSection`

### Layouts (3 Composed Layouts)

- `DashboardLayout`
- `LandingLayout`
- `AuthLayout`

### Accessibility (4 Helpers)

- `SkipLink`
- `LiveRegion`
- `VisuallyHidden`
- `FocusTrap`

### Effects (1 Module)

- `Fx` - Zero-JS animations and visual effects

### Optional Integrations (3 Opt-In Systems)

- `ChartJS` - Optional Chart.js integration via `faststrap[chartjs]`
- `Gsap` / `Motion` / `GsapReveal` - Optional GSAP motion integration via `faststrap[gsap]`
- `ModernToast` - Opinionated modern toast surface that remains separate from the core Bootstrap toast API

### Core Discovery And Theme Utilities

- `list_components`
- `get_component`
- `find_components`
- `get_components_by_pattern`
- `list_component_metadata`
- `theme_variant_css`

## Documentation Coverage

Docs are actively being expanded to match the full API surface. See the docs site and `examples/` for current coverage and usage patterns.

**View docs**: [https://faststrap-org.github.io/Faststrap/](https://faststrap-org.github.io/Faststrap/)

## Showcase References

Faststrap now has a dedicated `showcase/` layer for polished, product-style references. These files are meant to show what the framework looks like beyond small demos:

- `showcase/novaflow_ai_saas.py`
- `showcase/fastcloud_generated_saas.py` (compact minimal-good example)
- `showcase/northstar_ops_dashboard.py`
- `showcase/agency_portfolio.py`
- `showcase/carenest_clinic.py`
- `showcase/ledgerleaf_finance.py`
- `showcase/learnloop_academy.py`
- `showcase/lexbridge_corporate.py`
- `showcase/forgedocs_platform.py`

Recommended screenshot folder for docs/README assets:

- `docs/assets/showcase/`

Recommended naming:

- `novaflow-ai-saas-light.png`
- `novaflow-ai-saas-dark.png`
- `northstar-ops-dashboard-light.png`
- `northstar-ops-dashboard-dark.png`

---

## Examples

Comprehensive examples organized by learning path:

### 01_getting_started/

- `hello_world.py` - Your first Faststrap app
- `first_card.py` - Working with components
- `simple_form.py` - Building forms
- `adding_htmx.py` - HTMX interactivity

### 03_real_world_apps/

- `blog/` - Complete blog with posts, comments, admin
- `calculator/` - HTMX-powered calculator
- `game/` - Tic-tac-toe with win detection
- `ecommerce/` - E-commerce store (existing)

### 04_advanced/

- `effects_showcase.py` - All Faststrap effects demo
- `custom_themes.py` - Theme customization
- `component_defaults.py` - Global configuration

### 05_new_components/

- `v100_component_wave.py` - Core v1.0 component wave demo
- `v100_workflow_patterns.py` - HTMX workflow and helper patterns
- `v100_optional_integrations.py` - ModernToast, ChartJS, and GSAP opt-in integrations

**See**: `examples/README.md` for complete guide

| **Dropdown** | Contextual menus with split buttons |  |
| **Input** | Text form controls with validation |  |
| **Select** | Dropdown selections (single/multiple) |  |
| **Breadcrumb** | Navigation trail with icons |  |
| **Pagination** | Page navigation with customization |  |
| **Spinner** | Loading indicators (border/grow) |  |
| **Progress** | Progress bars with animations |  |

###  Phase 4A (v0.4.0) - 10 Components

| Component | Description | Status |
|-----------|-------------|--------|
| **Table** | Responsive data tables |  |
| **Accordion** | Collapsible panels |  |
| **Checkbox** | Checkbox form controls |  |
| **Radio** | Radio button controls |  |
| **Switch** | Toggle switch variant |  |
| **Range** | Slider input control |  |
| **ListGroup** | Versatile lists |  |
| **Collapse** | Show/hide content |  |
| **InputGroup** | Prepend/append addons |  |
| **FloatingLabel** | Animated label inputs |  |

###  Phase 4B (v0.4.5) - 8 Components

| Component | Description | Status |
|-----------|-------------|--------|
| **FileInput** | File uploads with preview |  |
| **Tooltip** | Contextual hints |  |
| **Popover** | Rich overlays |  |
| **Figure** | Image + caption |  |
| **ConfirmDialog** | Modal confirmation preset |  |
| **EmptyState** | Placeholder component |  |
| **StatCard** | Metric display card |  |
| **Hero** | Landing page hero section |  |

###  Phase 5A (v0.5.0-v0.5.3) - 6 Components

| Component | Description | Status |
|-----------|-------------|--------|
| **Image** | Responsive images with utilities |  |
| **Carousel** | Image/content sliders |  |
| **Placeholder** | Skeleton loading states |  |
| **Scrollspy** | Auto-updating navigation |  |
| **SidebarNavbar** | Premium vertical sidebar |  |
| **GlassNavbar** | Glassmorphism navbar |  |

###  Phase 5B+ (v0.5.6-v0.6.0) - stabilization and foundations

**HTMX Presets Module (17 helpers):**

- `ActiveSearch`, `InfiniteScroll`, `AutoRefresh`, `LazyLoad`, `LoadingButton`
- `OptimisticAction`, `LocationAction`
- `hx_redirect`, `hx_refresh`, `hx_trigger`, `hx_reswap`, `hx_retarget`, `toast_response`
- `SSEStream`, `sse_event`, `sse_comment`
- `@require_auth` decorator

**SEO Module (3 helpers):**

- `SEO` - Meta tags, Open Graph, Twitter Cards, Article metadata
- `PageMeta` - Unified SEO + social + canonical + favicon composition
- `StructuredData` - JSON-LD for Article, Product, Breadcrumb, Organization, LocalBusiness

**UI Components (9):**

- `ErrorPage`, `ErrorDialog`, `FormGroup`, `ThemeToggle`, `SearchableSelect`
- `FooterModern`, `Testimonial`, `TestimonialSection`, `AuthLayout`

## Release Snapshot (current main - major release candidate)

The planned component roadmap is now complete on `main`. The next release should be treated as a major release candidate because the public API surface now includes the full planned component wave, optional integrations, and framework ergonomics.

### Data Foundations

- DataTable with search, sort, pagination, and export helper
- DataTable query helpers: `DataTable.query_params()` and `DataTable.page_url()`
- Chart wrapper for Matplotlib, Plotly, Altair, and raw SVG/HTML
- Optional Chart.js integration: `ChartJS`, `add_chartjs()`, and `faststrap[chartjs]`
- Metric cards: `MetricCard`, `TrendCard`, `KPICard`
- `StatCard` refinement with `delta` aliases and a theme hook
- Dashboard layout primitives: `DashboardGrid`
- Filter inputs: `FilterBar`, `DateRangePicker`, `MultiSelect`, `RangeSlider`, `ExportButton`
- Realtime helpers: `SSEStream`, `SSETarget`
- NotificationCenter dropdown hub
- Renderers: `Markdown`, `Svg`, `Mermaid`
- Form error summary: `FormErrorSummary`

### Completed Component Waves

- Wave 1: `ResultCard`, `Avatar`, `AvatarGroup`, `StatusBadge`, `BadgeGroup`, `InlineEditor`
- Wave 2: `Timeline`, `Stepper`, `CalendarDatePicker`
- Wave 3: `FormWizard`, `CommandPalette`, `ModernToast`, `ChartJS`, `GSAP Motion`
- Wave 4: `Pagination` improvements, `LiveValidationField`, `ValidationMessage`, `ConfirmAction`, DataTable query helpers, registry discovery, `theme_variant_css`

### Optional Integrations

- `faststrap[chartjs]` for Chart.js teams
- `faststrap[gsap]` for richer motion while keeping core `Fx` zero-JS by default
- `ModernToast` as an opinionated polished toast alternative beside the core Bootstrap toast components

### Remaining Before Major Release

- Add focused examples for all newly added components and optional integrations
- Add at least two showcase apps that exercise the new surfaces in realistic product contexts
- Finalize release notes/changelog and version metadata
- Run full CI locally and on GitHub Actions

**Status: v1.0 component scope reached.**

### Canonical Next-Component Plan

For the current merged source of truth on what we plan to build next, see the `Canonical Next Build Roadmap` section in [`ROADMAP.md`](ROADMAP.md). That section consolidates the audit follow-ups, implementation-first additions, and broader component suggestions into one prioritized wave plan.

See [ROADMAP.md](ROADMAP.md) for complete timeline.

---

## Core Concepts

### 1. Adding Bootstrap to Your App

```python
from fasthtml.common import FastHTML
from faststrap import add_bootstrap, create_theme

app = FastHTML()

# Basic setup (includes default FastStrap favicon)
add_bootstrap(app)

# With dark mode
add_bootstrap(app, mode="dark")

# Custom theme
theme = create_theme(primary="#7BA05B", secondary="#48C774")
add_bootstrap(app, theme=theme)

# Using CDN
# Note: this covers Faststrap-managed assets only.
# Your own app CSS/images still need to be served by your deployment setup.
add_bootstrap(app, use_cdn=True)
```

### 2. Using Components

All components follow Bootstrap's conventions with Pythonic names:

```python
from faststrap import Button, Badge, Alert, Input, Select, Tabs

# Button with HTMX
Button("Save", variant="primary", hx_post="/save", hx_target="#result")

# Form inputs
Input("email", input_type="email", label="Email Address", required=True)
Select("country", ("us", "USA"), ("uk", "UK"), label="Country")

# Navigation tabs
Tabs(
    ("home", "Home", True),
    ("profile", "Profile"),
    ("settings", "Settings")
)
```

### 3. HTMX Integration

All components support HTMX attributes:

```python
# Dynamic button
Button("Load More", hx_get="/api/items", hx_swap="beforeend")

# Live search input
Input("search", placeholder="Search...", hx_get="/search", hx_trigger="keyup changed delay:500ms")

# Dynamic dropdown
Select("category", ("a", "A"), ("b", "B"), hx_get="/filter", hx_trigger="change")
```

### 4. Responsive Grid System

```python
from faststrap import Container, Row, Col

Container(
    Row(
        Col("Left column", cols=12, md=6, lg=4),
        Col("Middle column", cols=12, md=6, lg=4),
        Col("Right column", cols=12, md=12, lg=4)
    )
)
```

---

## Examples

### Form with Validation

```python
from faststrap import Input, Select, Button, Card

Card(
    Input(
        "email",
        input_type="email",
        label="Email Address",
        placeholder="you@example.com",
        required=True,
        help_text="We'll never share your email"
    ),
    Input(
        "password",
        input_type="password",
        label="Password",
        required=True,
        size="lg"
    ),
    Select(
        "country",
        ("us", "United States"),
        ("uk", "United Kingdom"),
        ("ca", "Canada"),
        label="Country",
        required=True
    ),
    Button("Sign Up", variant="primary", type="submit", cls="w-100"),
    header="Create Account"
)
```

### Navigation with Tabs

```python
from faststrap import Tabs, TabPane, Card

Card(
    Tabs(
        ("profile", "Profile", True),
        ("settings", "Settings"),
        ("billing", "Billing")
    ),
    Div(
        TabPane("Profile content here", tab_id="profile", active=True),
        TabPane("Settings content here", tab_id="settings"),
        TabPane("Billing content here", tab_id="billing"),
        cls="tab-content p-3"
    )
)
```

### Loading States

```python
from faststrap import Spinner, Progress, Button

# Spinner in button
Button(
    Spinner(size="sm", label="Loading..."),
    " Processing...",
    variant="primary",
    disabled=True
)

# Progress bar
Progress(75, variant="success", striped=True, animated=True, label="75%")

# Stacked progress
Div(
    ProgressBar(30, variant="success"),
    ProgressBar(20, variant="warning"),
    ProgressBar(10, variant="danger"),
    cls="progress"
)
```

### Pagination

```python
from faststrap import Pagination, Breadcrumb

# Breadcrumb
Breadcrumb(
    (Icon("house"), "/"),
    ("Products", "/products"),
    ("Laptops", None)
)

# Page navigation
Pagination(
    current_page=5,
    total_pages=20,
    size="lg",
    align="center",
    show_first_last=True
)
```

---

## Project Structure

```
faststrap/
 src/faststrap/               # Library source
    components/              # 128 registered UI components
    core/                    # Assets, theme, registry, discovery, base primitives
    integrations/            # Optional ChartJS and GSAP integrations
    presets/                 # HTMX interaction/response helpers
    seo/                     # SEO + structured data helpers
    pwa/                     # PWA manifest and install helpers
    layouts/                 # Composed page layouts
    static/                  # Vendored Bootstrap/Faststrap assets + favicon
 tests/                       # 779 collected tests in CI
 examples/                    # Structured examples by learning path
    01_getting_started/
    02_ui_components/
    03_real_world_apps/
    04_advanced/
 docs/                        # MkDocs site + guides (incl. deployment)
 pyproject.toml               # Packaging, tooling, and quality gates
```

---

## Development

### Prerequisites

- Python 3.10+
- FastHTML 0.6+
- Git

### Setup

```bash
# Clone repository
git clone https://github.com/Faststrap-org/Faststrap.git
cd Faststrap

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install with dev dependencies
pip install -e ".[dev]"

# Run tests
pytest

# Run with coverage
pytest --cov=faststrap

# Type checking
mypy src/faststrap

# Format code
black src/faststrap tests
ruff check src/faststrap tests
```

---

## Troubleshooting

### Static Files Not Loading (404 Errors)

**Fixed in v0.4.6+!** If you're seeing 404 errors for Bootstrap CSS/JS files, update to the latest version:

```bash
pip install --upgrade faststrap
```

### Theme Not Applied with fast_app()

When using `fast_app()`, add `data_bs_theme` to your root element:

```python
app, rt = fast_app()
add_bootstrap(app, mode="light")

@rt("/")
def get():
    return Div(
        YourContent(),
        data_bs_theme="light",  #  Add this for proper theming
    )
```

### Styles Not Loading with Custom Html()

When manually creating `Html()` + `Head()`, include `*app.hdrs`:

```python
@app.route("/")
def get():
    return Html(
        Head(
            Title("My App"),
            *app.hdrs,  #  Required for Faststrap styles
        ),
        Body(YourContent())
    )
```

**For more help**, see [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md)

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Quick Contribution Guide

1. **Pick a component** from [ROADMAP.md](ROADMAP.md) active or planned sections
2. **Follow patterns** in [BUILDING_COMPONENTS.md](BUILDING_COMPONENTS.md)
3. **Write tests** - Aim for 100% coverage (8-15 tests per component)
4. **Submit PR** - We review within 48 hours

---

## Documentation

-  **Component Spec**: [COMPONENT_SPEC.md](COMPONENT_SPEC.md)
-  **Building Guide**: [BUILDING_COMPONENTS.md](BUILDING_COMPONENTS.md)
-  **Roadmap**: [ROADMAP.md](ROADMAP.md)
-  **Contributing**: [CONTRIBUTING.md](CONTRIBUTING.md)
-  **Changelog**: [CHANGELOG.md](CHANGELOG.md)

---

## Support

-  **Documentation**: [GitHub README](https://github.com/Faststrap-org/Faststrap#readme)
-  **Bug Reports**: [GitHub Issues](https://github.com/Faststrap-org/Faststrap/issues)
-  **Discussions**: [GitHub Discussions](https://github.com/Faststrap-org/Faststrap/discussions)
-  **Discord**: [FastHTML Community](https://discord.gg/qcXvcxMhdP)

---

## License

MIT License - see [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **FastHTML** - The amazing pure-Python web framework
- **Bootstrap** - Battle-tested UI components
- **HTMX** - Dynamic interactions without complexity
- **Contributors** - Thank you! 

---

**Built with  for the FastHTML community**

