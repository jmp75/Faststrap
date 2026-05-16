# Documentation Standards

Faststrap component docs should be consistent enough that a beginner can move from one page to another without relearning the page shape.

## Component Page Template

Use this structure for new or refreshed component pages:

~~~markdown
# ComponentName

One short paragraph describing what the component does and when to use it.

## Quick Start

```python
from faststrap import ComponentName

ComponentName(...)
```

## Common Patterns

Add 2-4 realistic examples. Prefer common app use cases over toy snippets.

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `name` | `str` | required | What this controls. |

## Notes

- Mention JavaScript requirements.
- Mention optional dependencies.
- Mention security or accessibility constraints.
- Mention HTMX behavior if relevant.

## API Reference

::: faststrap.components.category.module.ComponentName
~~~

## Required Sections

Every public component page should have:

- A concise opening explanation.
- A runnable import and usage example.
- A parameter table with defaults.
- Notes for JavaScript, HTMX, optional dependencies, accessibility, or security when relevant.
- An API reference block using `mkdocstrings`.

## Parameter Table Rules

- Use `required` in the default column for required arguments.
- Use backticks around parameter names, types, values, and literals.
- Prefer actual source defaults over prose.
- Use `UNSET` when the source uses the component defaults sentinel.
- Include `**kwargs` when the component forwards extra attributes.

## Example Rules

- Prefer Faststrap components over raw Bootstrap HTML.
- Keep examples short enough to copy.
- Avoid fake parameters that are not in source.
- Use `variant="danger", outline=True`, not `variant="outline-danger"`.
- Use Python attribute names such as `data_bs_toggle`, `aria_label`, and `hx_get`.

## Warning Blocks

Use admonitions for sharp edges:

```markdown
!!! warning "Optional dependency"
    Install with `pip install "faststrap[markdown]"`.
```

Good warning topics:

- Optional extras such as Markdown, GSAP, ChartJS, or map libraries.
- Raw HTML/SVG rendering.
- Pydantic v2-only helpers.
- Required layout containers such as `ToastContainer`.
- Components that require Bootstrap JavaScript.

## Visual Previews

When a page includes an HTML preview block, keep it small and representative. For full-page visual references, link to the Showcase section instead of embedding large screenshots in every component page.
