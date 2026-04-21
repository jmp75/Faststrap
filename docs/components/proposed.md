# Proposed Components

!!! warning "Planned Surface Only"
    Everything on this page is a proposal for future Faststrap releases. These components are **not implemented yet**. This page exists to document the intended direction clearly before code is written.

Faststrap now has enough real-world showcases to expose the next meaningful gap: frontend developers can build polished pages today, but they still repeat a lot of structural and product-UI patterns by hand.

The proposed components below are meant to close that gap without drifting away from Faststrap's core philosophy:

- Bootstrap-native structure
- FastHTML-first composition
- HTMX-first interaction
- minimal JavaScript
- custom CSS for visual identity, not framework replacement

---

## Layout Primitives

These are high-leverage building blocks that make polished layout composition faster and more consistent across apps.

### Stack

Vertical layout primitive with consistent spacing between children.

```python
Stack(
    H2("Team Metrics"),
    P("Track delivery, revenue, and support load."),
    DashboardGrid(*cards),
    gap=4,
)
```

Why it matters:

- removes repeated `d-flex flex-column gap-*`
- improves section rhythm
- helps AI builders avoid ad hoc spacing

### Cluster

Horizontal wrapping layout for actions, chips, badges, and filter controls.

```python
Cluster(
    Badge("Enterprise", variant="primary"),
    Badge("Priority", variant="warning"),
    Button("Export"),
    gap=2,
    justify="between",
)
```

Why it matters:

- cleaner than hand-written `d-flex flex-wrap align-items-center gap-*`
- ideal for headers, action bars, and metadata rows

### Center

Simple primitive for centering content with optional max width and text alignment.

```python
Center(
    Card(H3("No projects yet"), P("Create your first project to get started.")),
    max_width="32rem",
)
```

Why it matters:

- useful for auth, empty states, hero content, and completion screens
- keeps centering patterns consistent

### Switcher

Responsive layout primitive that switches from inline to stacked once items no longer fit comfortably.

```python
Switcher(
    Card("Monthly recurring revenue"),
    Card("Retention"),
    Card("Churn"),
    threshold="48rem",
    gap=3,
)
```

Why it matters:

- a better abstraction for “three across until they shouldn’t be”
- very useful in dashboards and marketing summaries

### Sidebar

Composable app-shell sidebar primitive distinct from navigation-only navbar variants.

```python
Sidebar(
    brand=Span("Northstar"),
    items=[...],
    footer=ThemeToggle(),
    collapsible=True,
)
```

Why it matters:

- simplifies dashboard shells
- avoids re-implementing structural sidebar scaffolding
- pairs naturally with `DashboardLayout`

### SplitPane

Two-pane layout for docs, productivity tools, builders, and master/detail screens.

```python
SplitPane(
    left=Markdown(doc_text),
    right=Card("Inspector"),
    ratio="2:1",
)
```

Why it matters:

- useful for documentation tools, editors, data inspectors, and admin workflows
- gives frontend developers a better default than ad hoc grid hacks

---

## Product Navigation & Discovery

These components target higher-level application patterns that modern frontend teams expect out of the box.

### SearchBar

Polished global search/header search component with optional HTMX suggestions.

```python
SearchBar(
    placeholder="Search users, invoices, and reports",
    endpoint="/search",
    target="#search-results",
)
```

Why it matters:

- very common app-shell need
- should feel more intentional than raw `Input(...)`

### ProfileDropdown

Opinionated authenticated-user menu for dashboards and portals.

```python
ProfileDropdown(
    name="Maya Yusuf",
    subtitle="Revenue Operations",
    avatar="/assets/maya.jpg",
    items=[
        ("Profile", "/profile"),
        ("Settings", "/settings"),
        ("Sign out", "/logout"),
    ],
)
```

Why it matters:

- avoids rebuilding the same account menu in every app
- stronger than generic dropdown composition

### MegaMenu

Expanded navigation surface for marketing sites, docs, and SaaS platforms.

```python
MegaMenu(
    label="Product",
    sections=[
        {"title": "Build", "links": [...]},
        {"title": "Deploy", "links": [...]},
    ],
)
```

Why it matters:

- useful for premium landing sites and docs nav
- bridges the gap between simple nav links and fully custom dropdown markup

### CommandPalette

Keyboard-driven command/search launcher with server-driven results.

```python
CommandPalette(
    endpoint="/commands",
    shortcut="mod+k",
    target="#command-results",
)
```

Why it matters:

- strong fit for dashboards, admin tools, and internal platforms
- should be implemented as progressive enhancement, not JS-heavy client state

---

## Flows & Information Patterns

These components make common multi-step and history-heavy UI easier to ship.

### Timeline

Chronological activity stream for order history, audits, roadmap updates, and release logs.

```python
Timeline(
    ("09:30", "Booking confirmed"),
    ("10:15", "Payment captured"),
    ("11:05", "Welcome email sent"),
)
```

Why it matters:

- repeated in SaaS, ops, healthcare, finance, and booking products
- easier than rebuilding custom event stacks

### Stepper

Progress indicator for multi-step flows.

```python
Stepper(
    ("Account", True),
    ("Workspace", True),
    ("Billing", False),
)
```

Why it matters:

- core primitive for onboarding and setup flows
- should work well with server-driven forms

### FormWizard

Multi-step form helper built on `Stepper`, `FormGroup`, and server-driven progression.

```python
FormWizard(
    steps=[account_step(), workspace_step(), billing_step()],
    current_step=2,
    endpoint="/signup/step",
)
```

Why it matters:

- a high-value abstraction for onboarding, checkout, and application flows
- should remain server-first and HTMX-friendly

---

## Feedback & Visualization Proposals

These proposals are slightly more opinionated because they touch richer interaction and rendering concerns.

### ModernToast

Proposal for a more visually polished toast surface than the existing `Toast` / `SimpleToast`.

```python
ModernToast(
    "Deployment succeeded",
    title="Project published",
    variant="success",
    action=("View dashboard", "/dashboard"),
)
```

**My take on JS here:**

- a modern toast is still worth adding
- **minimal JavaScript is acceptable** if it is progressive enhancement, tiny in scope, and not required for core rendering
- if we want features like:
  - animated stack coordination
  - pause on hover
  - progress timers
  - swipe or advanced dismiss gestures
  then some JS becomes reasonable

Recommended contract:

- server-rendered first
- usable without JS
- advanced animation/timer behavior only when Faststrap JS is present
- no client-side state store

That keeps it aligned with Faststrap instead of turning it into a mini frontend framework.

### ChartJS

Proposal for an optional Chart.js integration alongside the current generic `Chart` wrapper.

```python
ChartJS(
    type="line",
    data=chart_data,
    options={"plugins": {"legend": {"display": False}}},
)
```

**My take on Chart.js:**

- yes, this is worth doing
- it should be **optional**, just like `MapView`, Markdown sanitization, or Mermaid-style extras
- the right packaging shape is something like:
  - `faststrap[chartjs]`

Recommended design:

- keep the current `Chart` component as the generic abstraction
- add `ChartJS` as an opinionated, modern-chart path
- bundle no chart assets by default
- allow:
  - CDN mode
  - local vendored asset mode later if needed
- expose theme helpers so charts adapt to light/dark surfaces cleanly

Why it matters:

- Chart.js gives frontend developers a more familiar modern charting feel
- it helps close the gap where Matplotlib/Altair/Plotly are powerful but not always visually aligned with modern SaaS dashboards by default

Security / correctness notes:

- serialize config safely from Python
- document CSP implications
- avoid unsafe raw HTML patterns for chart bootstrapping

---

## Suggested Build Order

If implemented soon, this is the order that gives the biggest frontend value fastest:

1. `Stack`
2. `Cluster`
3. `Center`
4. `Switcher`
5. `ProfileDropdown`
6. `Timeline`
7. `SearchBar`
8. `Sidebar`
9. `Stepper`
10. `FormWizard`
11. `ModernToast`
12. `SplitPane`
13. `MegaMenu`
14. `CommandPalette`
15. `ChartJS`

This order intentionally prioritizes:

- low-JS layout leverage first
- common product UI next
- richer interaction/integration components after that
