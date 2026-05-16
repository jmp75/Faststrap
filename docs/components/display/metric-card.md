# MetricCard

`MetricCard` displays one important value with an optional delta and icon. Use it for dashboard KPIs, analytics summaries, and operational health cards.

## Quick Start

```python
from faststrap import Icon, MetricCard

MetricCard(
    "Revenue",
    "$42.8k",
    delta="+12.4%",
    delta_type="up",
    icon=Icon("graph-up"),
)
```

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `title` | `str` | required | Metric label. |
| `value` | `str \| int \| float` | required | Primary metric value. |
| `delta` | `str \| int \| float \| None` | `None` | Change text such as `+12%`. |
| `delta_type` | `"up" \| "down" \| "neutral"` | `"neutral"` | Delta color treatment. |
| `icon` | `Any \| None` | `None` | Optional icon or custom element. |
| `variant` | Bootstrap variant | `UNSET` | Card background variant. |
| `inverse` | `bool` | `False` | Use inverted text colors. |
| `icon_bg` | `str \| None` | `UNSET` | Icon wrapper background class. |
| `**kwargs` | `Any` | | Extra HTML attributes. |

## Theming

`MetricCard` adds the `faststrap-metric-card` class, so you can style it with normal CSS or `theme_variant_css()`.

## API Reference

::: faststrap.components.display.stat_card.MetricCard
