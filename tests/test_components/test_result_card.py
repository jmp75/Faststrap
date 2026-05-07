"""Tests for ResultCard component."""

from fasthtml.common import to_xml

from faststrap import Button, ResultCard


def test_result_card_renders_success_state() -> None:
    html = to_xml(ResultCard("Saved", "Your changes were applied."))

    assert "faststrap-result-card" in html
    assert "border-success" in html
    assert 'role="status"' in html
    assert "Saved" in html
    assert "Your changes were applied." in html
    assert "bi-check-circle" in html


def test_result_card_renders_error_as_alert() -> None:
    html = to_xml(ResultCard("Failed", status="error"))

    assert "border-danger" in html
    assert 'role="alert"' in html
    assert "bi-x-circle" in html


def test_result_card_accepts_action_and_htmx_attrs() -> None:
    html = to_xml(
        ResultCard(
            "Ready",
            action=Button("Continue", variant="primary"),
            hx_get="/result",
            hx_target="#panel",
        )
    )

    assert "Continue" in html
    assert 'hx-get="/result"' in html
    assert 'hx-target="#panel"' in html
