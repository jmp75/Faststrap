"""Tests for InlineEditor component."""

import pytest
from fasthtml.common import to_xml

from faststrap import InlineEditor


def test_inline_editor_read_mode_renders_value_and_edit_action() -> None:
    html = to_xml(
        InlineEditor(
            "title",
            "Original title",
            id="title-editor",
            edit_endpoint="/title/edit",
        )
    )

    assert "faststrap-inline-editor" in html
    assert "Original title" in html
    assert "Edit" in html
    assert 'hx-get="/title/edit"' in html
    assert 'hx-target="#title-editor"' in html


def test_inline_editor_editing_mode_renders_htmx_form() -> None:
    html = to_xml(
        InlineEditor(
            "title",
            "Updated title",
            editing=True,
            endpoint="/title",
            hx_target="#title-editor",
            method="patch",
        )
    )

    assert "<form" in html
    assert 'hx-patch="/title"' in html
    assert 'hx-target="#title-editor"' in html
    assert 'name="title"' in html
    assert 'value="Updated title"' in html
    assert "Save" in html
    assert "Cancel" in html


def test_inline_editor_rejects_unknown_method() -> None:
    with pytest.raises(ValueError, match="method must be one of"):
        InlineEditor("title", method="delete")  # type: ignore[arg-type]
