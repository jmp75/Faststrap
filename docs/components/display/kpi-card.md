# KPICard

`KPICard` groups multiple related metrics inside one compact card.

## Quick Start

```python
from faststrap import KPICard

KPICard(
    "Campaign Health",
    metrics=[
        ("Leads", "1,240", "+18%", "up"),
        ("CAC", "$42", "-6%", "up"),
        ("Churn", "2.1%", "+0.4%", "down"),
    ],
    columns=3,
)
```

## Metric Tuple Format

Each metric must include at least `(label, value)`.

```python
("Revenue", "$82k")
("Revenue", "$82k", "+12%", "up")
```

The optional fourth value must be one of `up`, `down`, or `neutral`. Unknown values are treated as `neutral`.

## Parameters

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
| `title` | `str` | required | Card label. |
| `metrics` | `Sequence[Sequence[Any]]` | required | Metric tuples. |
| `columns` | `int` | `2` | Number of metric columns. Must be at least `1`. |
| `variant` | Bootstrap variant | `UNSET` | Card background variant. |
| `inverse` | `bool` | `False` | Use inverted text colors. |
| `**kwargs` | `Any` | | Extra HTML attributes. |

## API Reference

::: faststrap.components.display.stat_card.KPICard
