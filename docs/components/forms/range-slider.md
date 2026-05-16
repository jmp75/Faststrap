# RangeSlider

Single or dual range slider with optional live value display.

---

## Quick Start

<div class="component-preview">
  <div class="preview-header">Live Preview</div>
  <div class="preview-render">
    <div class="mb-3">
      <label class="form-label">Score</label>
      <input type="range" class="form-range" min="0" max="100" value="75">
      <span class="small text-muted">75</span>
    </div>
  </div>
  <div class="preview-code" markdown>
```python
from faststrap import RangeSlider

RangeSlider("score", min_value=0, max_value=100, value=75, label="Score")
```
  </div>
</div>

---

## Dual Range

```python
RangeSlider(
    "budget",
    dual=True,
    min_selected=200,
    max_selected=1200,
    min_name="min_budget",
    max_name="max_budget",
)
```

Dual mode renders two range inputs. Validate that min is not greater than max server-side.

---

## Value Display

```python
RangeSlider(
    "score",
    value=25,
    show_value=True,
    value_suffix="%",
)
```

---

## Step Control

```python
RangeSlider("score", min_value=0, max_value=100, step=5)
```

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `name` | `str` | required | Field name. |
| `label` | `str \| None` | `None` | Optional label. |
| `help_text` | `str \| None` | `None` | Optional helper text. |
| `min_value` | `int \| float` | `0` | Minimum allowed value. |
| `max_value` | `int \| float` | `100` | Maximum allowed value. |
| `step` | `int \| float` | `1` | Step interval. |
| `value` | `int \| float \| None` | `None` | Selected value for single-slider mode. |
| `dual` | `bool` | `False` | Render min and max sliders. |
| `min_name` | `str \| None` | `None` | Field name for dual minimum. Defaults to `{name}_min`. |
| `max_name` | `str \| None` | `None` | Field name for dual maximum. Defaults to `{name}_max`. |
| `min_selected` | `int \| float \| None` | `None` | Selected dual minimum. |
| `max_selected` | `int \| float \| None` | `None` | Selected dual maximum. |
| `show_value` | `bool` | `True` | Render a static value display. |
| `value_suffix` | `str` | `""` | Suffix shown in the value display. |
| `**kwargs` | `Any` | | Extra input attributes. |

## Notes

- The displayed value is static server-rendered text; it does not live-update without app-side JavaScript.
- Dual mode renders two native range inputs. Validate min/max consistency server-side.

---

## API Reference

::: faststrap.components.forms.range_slider.RangeSlider
    options:
        show_source: true
        heading_level: 4
