"""Tests for Avatar components."""

from fasthtml.common import to_xml

from faststrap import Avatar, AvatarGroup


def test_avatar_renders_initials_from_name() -> None:
    html = to_xml(Avatar("Ada Lovelace"))

    assert "AL" in html
    assert "faststrap-avatar" in html
    assert "rounded-circle" in html
    assert 'aria-label="Ada Lovelace"' in html


def test_avatar_renders_image_when_src_is_provided() -> None:
    html = to_xml(Avatar("Grace Hopper", src="/grace.jpg", alt="Grace"))

    assert 'src="/grace.jpg"' in html
    assert 'alt="Grace"' in html
    assert "object-fit-cover" in html


def test_avatar_supports_status_indicator() -> None:
    html = to_xml(Avatar("Lin", status="online"))

    assert 'aria-label="online"' in html
    assert "bg-success" in html


def test_avatar_group_wraps_avatars_and_count() -> None:
    html = to_xml(
        AvatarGroup(
            Avatar("Ada Lovelace"),
            Avatar("Grace Hopper"),
            Avatar("Katherine Johnson"),
            max_visible=2,
        )
    )

    assert "faststrap-avatar-group" in html
    assert "+1" in html
    assert html.count("faststrap-avatar") >= 3
