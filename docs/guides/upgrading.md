# Upgrading

This guide highlights the main changes to watch when upgrading Faststrap applications.

## From v0.6.x To v0.7.x

Faststrap v0.7.x adds a major component wave, optional integrations, and a safer defaults model.

### Component Defaults And `UNSET`

Faststrap now distinguishes omitted values from explicit `None`.

```python
from faststrap import Button, set_component_defaults

set_component_defaults("Button", size="lg")

Button("Large by default")
Button("Normal size here", size=None)
```

When writing wrapper components, default overridable options to `UNSET` instead of `None`.

```python
from faststrap import UNSET

def MyButton(*children, size=UNSET, **kwargs):
    ...
```

See [Component Defaults](../api/defaults.md).

### New Components

The v0.7.x wave includes:

- `ResultCard`
- `Avatar` and `AvatarGroup`
- `StatusBadge` and `BadgeGroup`
- `InlineEditor`
- `Timeline` and `TimelineItem`
- `Stepper` and `StepperStep`
- `CalendarDatePicker`
- `FormWizard` and `WizardStep`
- `CommandPalette` and `CommandItem`
- `LiveValidationField` and `ValidationMessage`

### Optional Integrations

Optional integrations remain outside the core dependency path:

```bash
pip install "faststrap[chartjs]"
pip install "faststrap[gsap]"
pip install "faststrap[markdown]"
```

Core `Fx` animations remain the default lightweight motion system. GSAP is opt-in.

### Pydantic Forms

Use `FormBuilder.from_pydantic()` for new code.

```python
from faststrap import FormBuilder
```

`Form.from_pydantic()` remains as a compatibility alias but emits a deprecation warning when called. The builder requires Pydantic v2.

### Tables

`Table`, `THead`, `TBody`, `TRow`, and `TCell` remain the primary table API.

If your app also imports native FastHTML table primitives, optional aliases are available:

```python
from faststrap import BsTable, BsTHead, BsTBody, BsTRow, BsTCell
```

### DataTable Pagination

Large `DataTable` paginators now render a bounded page window with ellipses instead of every page link. If you relied on every page number being present in the DOM, update that behavior.

### Button Type Default

Rendered `<button>` elements now default to `type="button"` to avoid accidental form submission.

Use `type="submit"` explicitly for submit buttons:

```python
Button("Save", type="submit")
```

## Upgrade Checklist

- Run your app and inspect forms that depend on implicit submit behavior.
- Replace new code using `Form.from_pydantic()` with `FormBuilder.from_pydantic()`.
- Review custom wrapper components and use `UNSET` where defaults should flow through.
- Run `faststrap doctor` to catch common setup issues.
- Run your test suite and `mkdocs build` if you publish docs.
