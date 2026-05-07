"""Tests for CommandPalette components."""

import pytest
from fasthtml.common import to_xml

from faststrap import CommandItem, CommandPalette


def test_command_item_renders_link_command() -> None:
    html = to_xml(
        CommandItem(
            "Open settings",
            href="/settings",
            description="Manage workspace preferences",
            icon="gear",
            shortcut="Ctrl+K",
        )
    )

    assert "faststrap-command-item" in html
    assert 'href="/settings"' in html
    assert "Open settings" in html
    assert "Manage workspace preferences" in html
    assert "bi-gear" in html
    assert "Ctrl+K" in html


def test_command_palette_renders_htmx_search() -> None:
    html = to_xml(
        CommandPalette(
            CommandItem("Dashboard", href="/dashboard"),
            endpoint="/commands",
            id="global-command",
        )
    )

    assert "faststrap-command-palette" in html
    assert 'hx-get="/commands"' in html
    assert 'hx-target="#global-command-results"' in html
    assert 'type="search"' in html
    assert "Dashboard" in html


def test_command_palette_rejects_unknown_method() -> None:
    with pytest.raises(ValueError, match="method must be"):
        CommandPalette(method="put")  # type: ignore[arg-type]
