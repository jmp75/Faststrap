"""Tests for Timeline components."""

from fasthtml.common import to_xml

from faststrap import Timeline, TimelineItem


def test_timeline_item_renders_event_content() -> None:
    html = to_xml(
        TimelineItem(
            "Deployment completed",
            description="Version 1.2.0 reached production.",
            time="10:30",
            icon="rocket",
            variant="success",
        )
    )

    assert "faststrap-timeline-item" in html
    assert "Deployment completed" in html
    assert "Version 1.2.0 reached production." in html
    assert "10:30" in html
    assert "text-bg-success" in html
    assert "bi-rocket" in html


def test_timeline_wraps_items_with_density() -> None:
    html = to_xml(
        Timeline(
            TimelineItem("Created"),
            TimelineItem("Reviewed"),
            density="compact",
        )
    )

    assert "faststrap-timeline" in html
    assert "gap-3" in html
    assert "Created" in html
    assert "Reviewed" in html
