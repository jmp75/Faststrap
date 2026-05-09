"""Tests for ModernToast components."""

from fasthtml.common import to_xml

from faststrap import Button, ModernToast, ModernToastStack


def test_modern_toast_renders_configurable_surface() -> None:
    html = to_xml(
        ModernToast(
            "Saved",
            "Your settings were updated.",
            variant="success",
            position="top-end",
            duration=3000,
            style="glass",
            action=Button("Undo", variant="link"),
        )
    )

    assert "faststrap-modern-toast" in html
    assert "faststrap-modern-toast-glass" in html
    assert 'data-duration="3000"' in html
    assert 'data-position="top-end"' in html
    assert 'role="status"' in html
    assert "Saved" in html
    assert "Undo" in html
    assert "bi-check-circle" in html
    assert 'type="button"' in html
    assert "data-bs-dismiss" not in html
    assert ">x</button>" not in html


def test_modern_toast_warning_uses_alert_role() -> None:
    html = to_xml(ModernToast("Careful", variant="warning"))

    assert 'role="alert"' in html
    assert "border-warning" in html


def test_modern_toast_stack_positions_toasts() -> None:
    html = to_xml(ModernToastStack(ModernToast("Saved"), position="bottom-end"))

    assert "faststrap-modern-toast-stack" in html
    assert "bottom-0 end-0" in html
    assert "Saved" in html
