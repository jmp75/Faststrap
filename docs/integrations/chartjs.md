# ChartJS

`ChartJS` is an optional Chart.js integration for teams that want the Chart.js ecosystem while keeping Faststrap's core package lightweight.

Core Faststrap still ships `Chart`. Use `ChartJS` when you specifically want Chart.js configuration, plugins, or behavior.

## Install

```bash
pip install faststrap
```

The `chartjs` extra is intentionally dependency-free in the Python package. The integration loads Chart.js from a CDN unless you pass your own asset URL, so no additional Python dependency is required.

Faststrap exposes `CHARTJS_VERSION` and `CHARTJS_CDN_URL` when you need to inspect or reuse the default pinned asset. `ChartJSType` is the type alias for supported Chart.js chart kinds.

## Import

```python
from faststrap import ChartJS, add_chartjs
```

## Add Assets

```python
app, rt = fast_app()
add_chartjs(app)
```

## Basic Usage

```python
ChartJS(
    "revenue-chart",
    type="bar",
    data={
        "labels": ["Jan", "Feb", "Mar"],
        "datasets": [
            {"label": "Revenue", "data": [120, 180, 240]},
        ],
    },
)
```

## With Options

```python
ChartJS(
    "conversion-chart",
    type="line",
    data={
        "labels": ["Mon", "Tue", "Wed"],
        "datasets": [{"label": "Conversion", "data": [4.2, 5.1, 4.8]}],
    },
    options={
        "plugins": {"legend": {"display": False}},
        "scales": {"y": {"beginAtZero": True}},
    },
    height=260,
)
```

## Parameters

| Param | Type | Description |
| :--- | :--- | :--- |
| `chart_id` | `str` | Canvas element ID. Must be unique on the page. |
| `type` | `ChartJSType` | Chart.js chart type. |
| `data` | `dict | None` | Chart.js data config. |
| `options` | `dict | None` | Chart.js options config. |
| `height` | `int | None` | Canvas height. |
| `width` | `int | None` | Canvas width. |
| `responsive` | `bool` | Adds Chart.js responsive option. |

::: faststrap.integrations.chartjs.chartjs_assets
    options:
        show_source: true
        heading_level: 3

::: faststrap.integrations.chartjs.add_chartjs
    options:
        show_source: true
        heading_level: 3

::: faststrap.integrations.chartjs.ChartJS
    options:
        show_source: true
        heading_level: 3
