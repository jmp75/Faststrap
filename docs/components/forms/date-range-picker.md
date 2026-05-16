# DateRangePicker

Lightweight date range input with HTMX-friendly hooks.

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <form class="d-flex flex-wrap gap-3 align-items-end">
      <div class="mb-3">
        <label class="form-label">Start date</label>
        <input type="date" class="form-control">
      </div>
      <div class="mb-3">
        <label class="form-label">End date</label>
        <input type="date" class="form-control">
      </div>
      <button class="btn btn-primary">Apply</button>
    </form>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import DateRangePicker

DateRangePicker(
    start_name="start",
    end_name="end",
    auto=True,
)
```
  </div>
</div>

---

## Presets

```python
DateRangePicker(
    presets=[
        ("Last 7 days", "2026-03-10", "2026-03-17"),
        ("Last 30 days", "2026-02-16", "2026-03-17"),
    ],
)
```

Preset buttons populate the form inputs. If you also set `auto=True`, Faststrap submits the form after applying the preset.

---

## HTMX Integration

```python
DateRangePicker(
    endpoint="/reports",
    method="get",
    auto=True,
    hx_target="#results",
    push_url=True,
)
```

---

## Limits and Defaults

Use `min_date`, `max_date`, `start_value`, and `end_value` to control allowed ranges.

For `method="post"`, ensure CSRF protection is enabled.

Preset shortcuts rely on the Faststrap runtime from `add_bootstrap(app)`.

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `start_name` | `str` | `"start_date"` | Start date field name. |
| `end_name` | `str` | `"end_date"` | End date field name. |
| `start_label` | `str` | `"Start date"` | Start date label. |
| `end_label` | `str` | `"End date"` | End date label. |
| `start_value` | `str \| None` | `None` | Initial start date in `YYYY-MM-DD` format. |
| `end_value` | `str \| None` | `None` | Initial end date in `YYYY-MM-DD` format. |
| `min_date` | `str \| None` | `None` | Earliest selectable date. |
| `max_date` | `str \| None` | `None` | Latest selectable date. |
| `presets` | `list[tuple[str, str, str]] \| None` | `None` | Preset buttons as `(label, start, end)`. |
| `endpoint` | `str \| None` | `None` | Form action and optional HTMX endpoint. |
| `method` | `"get" \| "post"` | `"get"` | Submit method. |
| `auto` | `bool` | `False` | Submit on change when an endpoint exists. |
| `apply_label` | `str \| None` | `"Apply"` | Submit button label. Set `None` to hide. |
| `hx_target` | `str \| None` | `None` | HTMX target selector. |
| `hx_swap` | `str \| None` | `"outerHTML"` | HTMX swap style. |
| `push_url` | `bool` | `False` | Push URL for HTMX GET flows. |
| `form_cls` / `presets_cls` / `inputs_cls` | `str \| None` | `None` | Styling hooks. |
| `**kwargs` | `Any` | | Extra form attributes. |

---

## API Reference

::: faststrap.components.forms.date_range_picker.DateRangePicker
    options:
        show_source: true
        heading_level: 4
