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

## Audit Triage Notes

Recent external audits surfaced a mix of real gaps and already-covered ideas. We keep this page focused by separating proposals from duplicates.

Already implemented today:

- `StatCard`
- `EmptyState`
- `Breadcrumb`
- `ConfirmDialog`
- `FilterBar`
- `SearchableSelect`
- `DataTable` with sorting, search, and pagination

Better handled as docs, recipes, or examples rather than new components:

- HTMX field validation patterns built on `FormGroup`
- responsive breadcrumb composition
- loading overlays built from `Spinner`
- skeleton states built from `Placeholder` / `PlaceholderCard`
- richer usage guidance for `FilterBar`, `SearchableSelect`, and `EmptyState`

Retained below as real future-component candidates:

- `ResultCard`
- `InlineEditor`
- `Avatar`
- `PaginationControls`

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
- encourages consistent spacing across pages and sections

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

- captures the common multi-card summary layout that collapses cleanly as space tightens
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

Two-pane layout for docs, productivity tools, editors, and master/detail screens.

```python
SplitPane(
    left=Markdown(doc_text),
    right=Card("Inspector"),
    ratio="2:1",
)
```

Why it matters:

- useful for documentation tools, editors, data inspectors, and admin workflows
- provides a stronger default than ad hoc grid composition

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
- provides a more complete header-search pattern than raw `Input(...)`

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

### InlineEditor

Edit-in-place primitive for HTMX-first dashboards, admin tools, and profile surfaces.

```python
InlineEditor(
    value="Revenue Operations",
    field_name="team_name",
    endpoint="/settings/team-name",
    input_type="text",
)
```

Why it matters:

- repeated pattern in tables, profile settings, and admin views
- should reduce ad hoc "click to edit" markup
- fits Faststrap well when implemented as server-driven swap targets

### PaginationControls

Composable pagination helper for list and search pages outside the full `DataTable` surface.

```python
PaginationControls(
    current_page=2,
    total_pages=10,
    endpoint="/orders",
    page_param="page",
)
```

Why it matters:

- `DataTable` already handles pagination well, but non-table views still repeat pager markup
- useful for card grids, search result pages, docs indexes, and gallery views
- keeps paging behavior consistent without forcing a full table abstraction

### Avatar

Identity primitive with image fallback, initials fallback, and optional presence indicator.

```python
Avatar(
    name="Maya Yusuf",
    src="/assets/maya.jpg",
    size="md",
    status="online",
)
```

Why it matters:

- repeated in dashboards, comments, account menus, and messaging UIs
- stronger than raw `Image(...)` when apps need initials fallback and status treatment
- pairs naturally with `ProfileDropdown` and team/member lists

---

## Feedback & Visualization Proposals

These proposals involve richer interaction and rendering concerns than the layout and flow primitives above.

### ResultCard

Structured success/error/warning feedback card for form submissions, setup flows, and post-action states.

```python
ResultCard(
    status="success",
    title="Profile updated",
    message="Your account changes were saved successfully.",
    action=("View profile", "/profile"),
)
```

Why it matters:

- repeated pattern after saves, onboarding completion, billing actions, and empty-success handoffs
- stronger and more consistent than ad hoc `Alert(...)` + `Button(...)` composition
- complements `EmptyState` instead of replacing it

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

Implementation notes:

- extends the existing toast surfaces with a more polished presentation option
- minimal JavaScript is acceptable when used only for progressive enhancement and not required for core rendering
- advanced behavior such as the following can remain optional:
  - animated stack coordination
  - pause on hover
  - progress timers
  - swipe or advanced dismiss gestures

Recommended behavior:

- server-rendered first
- usable without JavaScript
- advanced animation or timer behavior only when Faststrap JavaScript is present
- no client-side state store

### ChartJS

Proposal for an optional Chart.js integration alongside the current generic `Chart` wrapper.

```python
ChartJS(
    type="line",
    data=chart_data,
    options={"plugins": {"legend": {"display": False}}},
)
```

Implementation notes:

- adds an optional integration alongside the generic chart surface
- should remain optional, similar to `MapView`, Markdown sanitization, or Mermaid-style extras
- a packaging shape such as the following fits that model well:
  - `faststrap[chartjs]`

Design notes:

- keep the current `Chart` component as the generic abstraction
- add `ChartJS` as a more specialized integration path
- bundle no chart assets by default
- allow:
  - CDN mode
  - local vendored asset mode later if needed
- expose theme helpers so charts adapt to light/dark surfaces cleanly

Why it matters:

- Chart.js provides a familiar charting option for product and dashboard interfaces
- it complements Python charting workflows when teams need a charting surface aligned with modern dashboard styling

Security / correctness notes:

- serialize config safely from Python
- document CSP implications
- avoid unsafe raw HTML patterns for chart bootstrapping

---

## Suggested Build Order

If implemented soon, this order provides the highest immediate frontend value:

1. `Stack`
2. `Cluster`
3. `Center`
4. `Switcher`
5. `ProfileDropdown`
6. `ResultCard`
7. `Timeline`
8. `InlineEditor`
9. `SearchBar`
10. `Sidebar`
11. `Stepper`
12. `Avatar`
13. `FormWizard`
14. `PaginationControls`
15. `ModernToast`
16. `SplitPane`
17. `MegaMenu`
18. `CommandPalette`
19. `ChartJS`

Build-order rationale:

- low-JS layout leverage first
- common product UI next
- richer interaction/integration components after that
