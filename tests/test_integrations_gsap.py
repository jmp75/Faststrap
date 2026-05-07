"""Tests for optional GSAP motion integration."""

import pytest
from fasthtml.common import FastHTML, to_xml

from faststrap import GSAP_CDN_URL, Gsap, GsapReveal, Motion, add_gsap, gsap_assets


def _hdrs_to_text(app: FastHTML) -> str:
    return "\n".join(str(h) for h in app.hdrs)


def test_gsap_assets_include_cdn_and_runtime_script() -> None:
    assets = gsap_assets()
    rendered = "\n".join(str(asset) for asset in assets)

    assert GSAP_CDN_URL in rendered
    assert "window.FaststrapGsap" in rendered
    assert "data-fs-gsap" in rendered


def test_add_gsap_appends_assets_once() -> None:
    app = FastHTML()

    add_gsap(app)
    add_gsap(app)

    rendered = _hdrs_to_text(app)
    assert rendered.count("gsap.min.js") == 1
    assert rendered.count("window.FaststrapGsap") == 1


def test_gsap_attrs_convert_to_html_data_attributes() -> None:
    attrs = Gsap.attrs(
        Gsap.fade_up,
        duration=0.6,
        delay=0.1,
        ease="power3.out",
        stagger=0.05,
        id="hero-card",
    )

    assert attrs["data-fs-gsap"] == "fade-up"
    assert attrs["data-fs-gsap-duration"] == "0.6"
    assert attrs["data-fs-gsap-delay"] == "0.1"
    assert attrs["data-fs-gsap-ease"] == "power3.out"
    assert attrs["data-fs-gsap-stagger"] == "0.05"
    assert attrs["id"] == "hero-card"


def test_gsap_named_preset_helpers_are_pythonic_shortcuts() -> None:
    attrs = Gsap.fade_up_attrs(duration=0.4, delay=0.2, cls="metric-card")

    assert attrs["data-fs-gsap"] == "fade-up"
    assert attrs["data-fs-gsap-duration"] == "0.4"
    assert attrs["data-fs-gsap-delay"] == "0.2"
    assert attrs["cls"] == "metric-card"


def test_gsap_stagger_attrs_default_to_child_sequence() -> None:
    attrs = Gsap.stagger_attrs(Gsap.pop, duration=0.35)

    assert attrs["data-fs-gsap"] == "pop"
    assert attrs["data-fs-gsap-stagger"] == "0.08"
    assert attrs["data-fs-gsap-duration"] == "0.35"


def test_gsap_attrs_reject_unknown_preset() -> None:
    with pytest.raises(ValueError, match="Unknown GSAP preset"):
        Gsap.attrs("spin-around")  # type: ignore[arg-type]


def test_gsap_reveal_wraps_children_with_motion_attributes() -> None:
    html = to_xml(GsapReveal("Hello", preset="pop", cls="mb-3"))

    assert "faststrap-gsap-reveal mb-3" in html
    assert 'data-fs-gsap="pop"' in html
    assert "Hello" in html


def test_motion_alias_matches_gsap_reveal() -> None:
    html = to_xml(Motion("Hello", preset="scale"))

    assert "faststrap-gsap-reveal" in html
    assert 'data-fs-gsap="scale"' in html
