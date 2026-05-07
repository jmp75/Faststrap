"""Tests for status badge components."""

from fasthtml.common import to_xml

from faststrap import BadgeGroup, StatusBadge


def test_status_badge_maps_status_to_variant_and_icon() -> None:
    html = to_xml(StatusBadge("Live", status="active"))

    assert "faststrap-status-badge" in html
    assert "text-bg-success" in html
    assert 'data-status="active"' in html
    assert "bi-check-circle" in html


def test_status_badge_supports_error_alias() -> None:
    html = to_xml(StatusBadge("Failed", status="error"))

    assert "text-bg-danger" in html
    assert 'data-status="error"' in html
    assert "bi-x-circle" in html


def test_status_badge_supports_dot_style() -> None:
    html = to_xml(StatusBadge("Pending", status="pending", show_dot=True))

    assert "text-bg-warning" in html
    assert "background:currentColor" in html
    assert "bi-clock" not in html


def test_badge_group_wraps_badges_with_gap() -> None:
    html = to_xml(
        BadgeGroup(
            StatusBadge("Online", status="success"),
            StatusBadge("Queued", status="pending"),
            gap=3,
        )
    )

    assert "faststrap-badge-group" in html
    assert "gap-3" in html
    assert "Online" in html
    assert "Queued" in html
