# CalendarDatePicker

`CalendarDatePicker` is a single-date picker built around the native HTML `date` input. It is intentionally lightweight and works without custom JavaScript.

Use `DateRangePicker` when users need a start and end date. Use `CalendarDatePicker` when users choose one date, such as a publish date, appointment date, or filter date.

## Import

```python
from faststrap import CalendarDatePicker
```

## Basic Usage

```python
CalendarDatePicker(
    "publish_date",
    label="Publish date",
    value="2026-05-07",
)
```

## Date Limits

```python
CalendarDatePicker(
    "appointment_date",
    label="Appointment date",
    min_date="2026-05-01",
    max_date="2026-05-31",
)
```

## HTMX Filtering

```python
CalendarDatePicker(
    "day",
    label="Activity day",
    endpoint="/activity",
    hx_target="#activity-feed",
    auto=True,
    push_url=True,
)
```

When `auto=True`, the picker submits after the selected date changes.

## With Clear Button

```python
CalendarDatePicker(
    "due_date",
    label="Due date",
    clear_label="Clear",
)
```

## Parameters

| Param | Type | Description |
| :--- | :--- | :--- |
| `name` | `str` | Input name. |
| `label` | `str` | Label shown above the date input. |
| `value` | `str | None` | Initial date in `YYYY-MM-DD` format. |
| `min_date` | `str | None` | Earliest selectable date. |
| `max_date` | `str | None` | Latest selectable date. |
| `endpoint` | `str | None` | Optional form/HTMX endpoint. |
| `method` | `get | post` | Submission method. |
| `auto` | `bool` | Submit on date change when an endpoint is present. |
| `apply_label` | `str | None` | Submit button label. Set to `None` to hide. |
| `clear_label` | `str | None` | Optional reset button label. |
| `hx_target` | `str | None` | HTMX target for responses. |
| `push_url` | `bool` | Whether HTMX should push the URL. |

::: faststrap.components.forms.calendar_date_picker.CalendarDatePicker
    options:
        show_source: true
        heading_level: 3
