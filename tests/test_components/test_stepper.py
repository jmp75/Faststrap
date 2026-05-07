"""Tests for Stepper components."""

from fasthtml.common import to_xml

from faststrap import Stepper, StepperStep


def test_stepper_step_maps_status_to_variant() -> None:
    html = to_xml(
        StepperStep(
            "Account",
            description="Create your workspace",
            status="current",
            step=1,
        )
    )

    assert "faststrap-stepper-step" in html
    assert "is-current" in html
    assert 'aria-current="step"' in html
    assert "text-bg-primary" in html
    assert "Create your workspace" in html


def test_stepper_complete_step_uses_check_icon() -> None:
    html = to_xml(StepperStep("Profile", status="complete"))

    assert "text-bg-success" in html
    assert "bi-check" in html


def test_stepper_wraps_string_steps_and_orientation() -> None:
    html = to_xml(Stepper("Account", "Profile", orientation="vertical"))

    assert "faststrap-stepper" in html
    assert 'role="list"' in html
    assert 'role="listitem"' in html
    assert 'data-orientation="vertical"' in html
    assert "Account" in html
    assert "Profile" in html
