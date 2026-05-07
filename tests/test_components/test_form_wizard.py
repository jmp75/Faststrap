"""Tests for FormWizard components."""

import pytest
from fasthtml.common import P, to_xml

from faststrap import FormWizard, WizardStep


def test_form_wizard_renders_current_step_and_stepper() -> None:
    html = to_xml(
        FormWizard(
            WizardStep("Account", P("Account fields")),
            WizardStep("Billing", P("Billing fields")),
            current_step=1,
            endpoint="/setup",
            hx_target="#wizard",
        )
    )

    assert "faststrap-form-wizard" in html
    assert "Billing fields" in html
    assert "Account fields" not in html
    assert 'hx-post="/setup"' in html
    assert 'hx-target="#wizard"' in html
    assert "is-complete" in html
    assert "is-current" in html
    assert "Back" in html
    assert "Finish" in html


def test_form_wizard_clamps_current_step() -> None:
    html = to_xml(FormWizard(WizardStep("Only", P("One")), current_step=99))

    assert 'data-current-step="0"' in html
    assert "One" in html


def test_form_wizard_requires_steps_and_valid_method() -> None:
    with pytest.raises(ValueError, match="requires at least one"):
        FormWizard()
    with pytest.raises(ValueError, match="method must be"):
        FormWizard(WizardStep("One"), method="patch")  # type: ignore[arg-type]
