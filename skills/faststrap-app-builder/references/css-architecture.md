# CSS Architecture

Use this guide when a Faststrap project is larger than a single-file showcase and needs a clear CSS structure.

The goal is to keep:

- Bootstrap and Faststrap responsible for layout and component structure
- local CSS responsible for brand identity, surface treatment, depth, and refinement
- app styles organized enough that future edits do not collapse into one large `custom.css`

---

## Recommended Structure

```text
assets/
├── css/
│   ├── _brand.css
│   ├── _typography.css
│   ├── _layout.css
│   ├── _surfaces.css
│   ├── _interactions.css
│   └── custom.css
```

Recommended responsibility split:

- `_brand.css`
  - theme tokens, brand colors, radius tokens, semantic colors
- `_typography.css`
  - headings, body, labels, helper text, rhythm for text
- `_layout.css`
  - section spacing, wrappers, stacks, shell-level layout adjustments
- `_surfaces.css`
  - cards, panels, shells, overlays, glass, borders, shadows
- `_interactions.css`
  - buttons, links, hover states, focus polish, transitions
- `custom.css`
  - imports or aggregates the above files

---

## Example: `_brand.css`

```css
:root {
  --brand-primary: #5b6cff;
  --brand-secondary: #182033;
  --brand-accent: #10b981;
  --brand-danger: #ef4444;

  --radius-sm: 0.5rem;
  --radius-md: 0.75rem;
  --radius-lg: 1rem;

  --space-xs: 0.5rem;
  --space-sm: 0.75rem;
  --space-md: 1.5rem;
  --space-lg: 2.25rem;
  --space-xl: 3rem;
}

[data-bs-theme="light"] {
  --brand-shell: #f6f8fc;
  --brand-surface: rgba(255, 255, 255, 0.82);
  --brand-border: rgba(15, 23, 42, 0.08);
  --brand-text: rgba(15, 23, 42, 0.94);
  --brand-muted: rgba(15, 23, 42, 0.68);
}

[data-bs-theme="dark"] {
  --brand-shell: #09111f;
  --brand-surface: rgba(12, 20, 36, 0.72);
  --brand-border: rgba(148, 163, 184, 0.16);
  --brand-text: rgba(226, 232, 240, 0.94);
  --brand-muted: rgba(203, 213, 225, 0.72);
}
```

---

## Example: `_typography.css`

```css
.app-hero-title {
  font-size: clamp(1.9rem, 4vw, 2.6rem);
  font-weight: 800;
  line-height: 1.02;
  letter-spacing: -0.03em;
}

.app-section-title {
  font-size: 1.15rem;
  font-weight: 700;
  letter-spacing: -0.015em;
}

.app-body-copy {
  font-size: 0.95rem;
  line-height: 1.65;
  color: var(--brand-muted);
}

.app-label {
  font-size: 0.78rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  color: var(--brand-muted);
}
```

---

## Example: `_layout.css`

```css
body {
  background: radial-gradient(circle at top, rgba(91, 108, 255, 0.12), transparent 38%),
    var(--brand-shell);
  color: var(--brand-text);
}

.app-shell {
  min-height: 100vh;
}

.app-section {
  padding-block: clamp(3rem, 6vw, 5rem);
}

.app-stack-lg > * + * {
  margin-top: var(--space-lg);
}

.app-stack-md > * + * {
  margin-top: var(--space-md);
}
```

---

## Example: `_surfaces.css`

```css
.app-card {
  background: var(--brand-surface);
  border: 1px solid var(--brand-border);
  border-radius: var(--radius-md);
  box-shadow: 0 12px 40px rgba(15, 23, 42, 0.12);
  backdrop-filter: blur(12px);
}

.app-stat-card {
  padding: 1.25rem;
  border-left: 4px solid var(--brand-primary);
}

.app-shell-panel {
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.04), transparent),
    var(--brand-surface);
  border: 1px solid var(--brand-border);
  border-radius: var(--radius-lg);
}
```

---

## Example: `_interactions.css`

```css
.btn-primary {
  background: linear-gradient(135deg, var(--brand-primary), #4655d4);
  border-color: transparent;
  box-shadow: 0 10px 24px rgba(91, 108, 255, 0.28);
  transition:
    transform 0.2s ease,
    box-shadow 0.2s ease;
}

.btn-primary:hover {
  transform: translateY(-1px);
  box-shadow: 0 14px 30px rgba(91, 108, 255, 0.34);
}

.btn-outline-secondary {
  border-color: var(--brand-border);
  color: var(--brand-text);
}
```

---

## Example: `custom.css`

```css
@import url("./_brand.css");
@import url("./_typography.css");
@import url("./_layout.css");
@import url("./_surfaces.css");
@import url("./_interactions.css");
```

---

## Mounting Pattern

For a production-style app:

```python
from fasthtml.common import FastHTML, Link
from faststrap import add_bootstrap, mount_assets

app = FastHTML(hdrs=[])

add_bootstrap(app, theme=theme, mode="dark")
mount_assets(app, "assets")

app.hdrs.append(Link(rel="stylesheet", href="/assets/css/custom.css"))
```

Keep project CSS mounted after Faststrap so local brand polish can override defaults cleanly.

---

## Practical Rules

- Use Bootstrap and Faststrap for grid, spacing utilities, containers, and structural responsiveness first.
- Put repeated visual decisions into CSS classes, not inline `style=...` fragments.
- Treat mobile as the base layout. Use CSS for polish, not to replace Bootstrap's responsive structure.
- Keep app-level classes semantic and stable:
  - `.app-shell`
  - `.app-section`
  - `.app-card`
  - `.app-label`
- Avoid large anonymous utility piles such as long class strings repeated across every card.

---

## When Inline `Style(...)` Is Still Fine

Inline style blocks are acceptable when:

- the file is a one-off showcase
- the code is intentionally self-contained
- the app does not yet have multiple pages or shared assets

As soon as a project has multiple routes or reusable sections, move the CSS into mounted asset files.
