"""Tests for v0.8 core layout and structured-data primitives."""

from fasthtml.common import to_xml

from faststrap import (
    Center,
    Cluster,
    CodeBlock,
    FormSection,
    JsonViewer,
    KeyValueList,
    PageHeader,
    RecordDetail,
    Stack,
)
from faststrap.core.registry import list_components
from faststrap.presets import PollUntil


def test_layout_primitives_render_bootstrap_flex_classes() -> None:
    stack = to_xml(Stack("A", "B", gap=4, align="start"))
    assert "d-flex flex-column" in stack
    assert "gap-4" in stack
    assert "align-items-start" in stack

    cluster = to_xml(Cluster("A", "B", justify="between", wrap=False))
    assert "flex-nowrap" in cluster
    assert "justify-content-between" in cluster

    center = to_xml(Center("Hero", min_height="50vh", max_width="40rem"))
    assert "align-items-center" in center
    assert "justify-content-center" in center
    assert "min-height: 50vh" in center
    assert "max-width: 40rem" in center


def test_page_header_renders_title_subtitle_and_actions() -> None:
    html = to_xml(PageHeader("Reports", subtitle="Quarterly summary", actions=["Export"]))
    assert "Reports" in html
    assert "Quarterly summary" in html
    assert "Export" in html
    assert "justify-content-between" in html


def test_structured_display_primitives_render_safely() -> None:
    kv = to_xml(KeyValueList({"Status": "Ready", "Owner": "Ops"}, striped=True))
    assert "Status" in kv
    assert "Ready" in kv
    assert "faststrap-key-value-list" in kv

    detail = to_xml(RecordDetail({"ID": 42}, title="Job"))
    assert "faststrap-record-detail" in detail
    assert "Job" in detail
    assert "ID" in detail

    code = to_xml(CodeBlock("<script>alert(1)</script>", language="html", filename="demo.html"))
    assert "language-html" in code
    assert "demo.html" in code
    assert "&lt;script&gt;" in code

    json_view = to_xml(JsonViewer({"b": 2, "a": 1}, title="Payload"))
    assert "Payload" in json_view
    assert '"a": 1' in json_view
    assert "faststrap-json-viewer" in json_view


def test_form_section_groups_fields_and_actions() -> None:
    html = to_xml(
        FormSection("Name field", title="Profile", description="Public details", actions="Save")
    )
    assert "Profile" in html
    assert "Public details" in html
    assert "Name field" in html
    assert "Save" in html
    assert "faststrap-form-section" in html


def test_poll_until_uses_htmx_polling_contract() -> None:
    html = to_xml(PollUntil(endpoint="/jobs/1", interval=1500, content="Checking"))
    assert 'hx-get="/jobs/1"' in html
    assert 'hx-trigger="load, every 1500ms"' in html
    assert 'hx-target="this"' in html
    assert 'hx-swap="outerHTML"' in html
    assert "Checking" in html


def test_v080_primitives_are_registered() -> None:
    registered = set(list_components())
    for name in {
        "Stack",
        "Cluster",
        "Center",
        "PageHeader",
        "KeyValueList",
        "RecordDetail",
        "CodeBlock",
        "JsonViewer",
        "FormSection",
    }:
        assert name in registered
