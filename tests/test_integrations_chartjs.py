"""Tests for optional Chart.js integration."""

from fasthtml.common import to_xml

from faststrap import CHARTJS_CDN_URL, ChartJS, chartjs_assets


def test_chartjs_assets_use_cdn() -> None:
    html = "".join(to_xml(asset) for asset in chartjs_assets())

    assert CHARTJS_CDN_URL in html
    assert "defer" in html


def test_chartjs_renders_canvas_and_config_script() -> None:
    html = to_xml(
        ChartJS(
            "revenue-chart",
            type="bar",
            data={"labels": ["Jan"], "datasets": [{"label": "Revenue", "data": [42]}]},
            options={"plugins": {"legend": {"display": False}}},
            height=240,
        )
    )

    assert "faststrap-chartjs" in html
    assert '<canvas height="240" id="revenue-chart"></canvas>' in html
    assert '"type":"bar"' in html
    assert '"Revenue"' in html
    assert "new window.Chart" in html
