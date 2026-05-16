# FilterBar

Composable filter layout with HTMX integration and optional apply mode.

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <form class="d-flex flex-wrap gap-3 align-items-end">
      <div class="mb-3">
        <label class="form-label">Team</label>
        <select class="form-select" multiple>
          <option>Ops</option>
          <option>Data</option>
        </select>
      </div>
      <div class="mb-3">
        <label class="form-label">Score</label>
        <input type="range" class="form-range" min="0" max="100">
      </div>
      <button class="btn btn-primary">Apply</button>
    </form>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import FilterBar, MultiSelect, RangeSlider

FilterBar(
    MultiSelect("team", ("ops", "Ops"), ("data", "Data")),
    RangeSlider("score", min_value=0, max_value=100),
    mode="apply",
)
```
  </div>
</div>

---

## Auto vs Apply Mode

- `mode="auto"` triggers HTMX on change and keyup
- `mode="apply"` renders an Apply button

```python
FilterBar(
    *filters,
    endpoint="/reports",
    mode="auto",
    debounce=400,
)
```

---

## Reset Button

```python
FilterBar(
    *filters,
    mode="apply",
    reset_label="Reset",
    reset_href="/reports",
)
```

---

## HTMX Integration

```python
FilterBar(
    *filters,
    endpoint="/reports",
    method="get",
    hx_target="#results",
    hx_swap="outerHTML",
    push_url=True,
)
```

---

## Layout Control

Use `filters_cls` and `actions_cls` to adjust spacing or alignment.

```python
FilterBar(
    *filters,
    filters_cls="gap-2",
    actions_cls="ms-auto",
)
```

---

## Security Notes

Validate filters server-side. If you use `method="post"`, enable CSRF protection.

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `*filters` | `Any` | | Filter controls to render. |
| `endpoint` | `str \| None` | `None` | Form action and optional HTMX endpoint. |
| `method` | `"get" \| "post"` | `"get"` | Submit method. |
| `mode` | `"auto" \| "apply"` | `"auto"` | Auto-submit on change or render Apply button. |
| `apply_label` | `str` | `"Apply"` | Apply button text in apply mode. |
| `apply_variant` | Bootstrap variant | `"primary"` | Apply button variant. |
| `reset_label` | `str \| None` | `None` | Reset link label. |
| `reset_href` | `str \| None` | `None` | Reset link target. |
| `debounce` | `int` | `300` | HTMX debounce in milliseconds for auto mode. |
| `hx_target` | `str \| None` | `None` | HTMX target selector. |
| `hx_swap` | `str \| None` | `"outerHTML"` | HTMX swap style. |
| `push_url` | `bool` | `False` | Push URL for HTMX GET flows. |
| `filters_cls` / `actions_cls` / `form_cls` | `str \| None` | `None` | Styling hooks. |
| `**kwargs` | `Any` | | Extra form attributes. |

---

## API Reference

::: faststrap.components.forms.filter_bar.FilterBar
    options:
        show_source: true
        heading_level: 4
