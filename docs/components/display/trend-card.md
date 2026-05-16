# TrendCard

`TrendCard` is a metric card with a sparkline slot. It is useful when the value matters, but the direction of movement matters too.

## Quick Start

```python
from faststrap import TrendCard

TrendCard(
    "Active Users",
    "18.2k",
    delta="+8.1%",
    delta_type="up",
    sparkline=MiniSparkline(),
)
```

## Raw SVG Sparklines

Raw string sparklines are blocked by default. Set `sparkline_safe=True` only for trusted SVG/HTML.

```python
TrendCard(
    "Latency",
    "184ms",
    delta="-12ms",
    delta_type="up",
    sparkline="<svg><!-- trusted svg --></svg>",
    sparkline_safe=True,
)
```

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `title` | `str` | required | Metric label. |
| `value` | `str \| int \| float` | required | Primary metric value. |
| `sparkline` | `Any \| None` | `None` | Sparkline element or trusted raw string. |
| `sparkline_safe` | `bool` | `False` | Required before embedding raw string sparkline markup. |
| `delta` | `str \| int \| float \| None` | `None` | Change text such as `+8%`. |
| `delta_type` | `"up" \| "down" \| "neutral"` | `"neutral"` | Delta color treatment. |
| `variant` | Bootstrap variant | `UNSET` | Card background variant. |
| `inverse` | `bool` | `False` | Use inverted text colors. |
| `**kwargs` | `Any` | | Extra HTML attributes. |

## API Reference

::: faststrap.components.display.stat_card.TrendCard
