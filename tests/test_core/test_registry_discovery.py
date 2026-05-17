"""Tests for component discovery helpers."""

from faststrap import (
    Button,
    find_components,
    get_component,
    get_components_by_pattern,
    list_component_metadata,
    list_components,
    register,
)


def test_find_components_searches_names_and_docs() -> None:
    matches = find_components("button")

    assert "Button" in matches


def test_get_components_by_pattern_returns_callables() -> None:
    components = get_components_by_pattern("button", category="forms")

    assert Button in components


def test_list_component_metadata_includes_names_and_categories() -> None:
    metadata = list_component_metadata(category="forms")

    assert any(record["name"] == "Button" and record["category"] == "forms" for record in metadata)


def test_list_components_and_get_component_remain_available() -> None:
    assert "Button" in list_components(category="forms")
    assert get_component("Button") is Button


def test_register_is_available_from_top_level_for_custom_component_docs() -> None:
    assert callable(register)
