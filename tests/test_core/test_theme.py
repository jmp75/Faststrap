import pytest
from fasthtml.common import FastHTML

from faststrap.core import assets as assets_module
from faststrap.core.assets import add_bootstrap
from faststrap.core.theme import (
    UNSET,
    Theme,
    create_theme,
    get_builtin_theme,
    reset_component_defaults,
    resolve_defaults,
    set_component_defaults,
    theme_variant_css,
)


def test_theme_initialization():
    """Test Theme object creation and properties."""
    theme = Theme({"--bs-primary": "#112233"})
    assert theme.variables["--bs-primary"] == "#112233"


def test_create_theme_rgb_extraction_supports_rgba_and_alpha_hex():
    theme = create_theme(primary="#12345678", secondary="rgba(12, 34, 56, 0.4)")
    assert theme.variables["--bs-primary-rgb"] == "18, 52, 86"
    assert theme.variables["--bs-secondary-rgb"] == "12, 34, 56"


def test_builtin_themes():
    """Test retrieving and checking builtin themes."""
    theme = get_builtin_theme("green-nature")
    assert theme is not None
    assert theme.variables["--bs-primary"] == "#7BA05B"

    with pytest.raises(ValueError):
        get_builtin_theme("nonexistent")


def test_builtin_themes_are_cached():
    t1 = get_builtin_theme("green-nature")
    t2 = get_builtin_theme("green-nature")

    assert t1 is t2


def test_theme_css_generation():
    """Test Theme.to_style() output for different modes."""
    theme = get_builtin_theme("blue-ocean")

    # Light mode
    light_css = theme.to_style(mode="light")
    assert ":root" in str(light_css)
    assert f"--bs-primary: {theme.variables['--bs-primary']}" in str(light_css)

    # Dark mode (should contain variables from _DARK_MODE_VARS)
    dark_css = theme.to_style(mode="dark")
    assert "--bs-body-bg: #212529" in str(dark_css)

    # Auto mode (should contain both and media query)
    auto_css = theme.to_style(mode="auto")
    assert '[data-bs-theme="dark"]' in auto_css
    assert "@media (prefers-color-scheme: dark)" in auto_css
    assert ":root {" in auto_css
    assert "@media (prefers-color-scheme: dark) {\n  :root {" in auto_css


def test_theme_surface_tokens_are_present_in_generated_css():
    """Theme CSS includes Faststrap surface polish tokens and component overrides."""
    theme = get_builtin_theme("blue-ocean")
    css = str(theme.to_style(mode="light"))

    assert "--fs-surface-bg: #ffffff;" in css
    assert "--fs-radius: 0.9rem;" in css
    assert ".card," in css
    assert "box-shadow: var(--fs-surface-shadow-sm);" in css
    assert ".form-control," in css


def test_create_theme_supports_faststrap_surface_tokens():
    """create_theme maps surface and radius kwargs to Faststrap tokens."""
    theme = create_theme(
        primary="#112233",
        radius="1.1rem",
        surface_bg_light="#f5f0ff",
        surface_bg_dark="#17131f",
        surface_shadow="0 20px 50px rgba(10, 10, 20, 0.2)",
    )

    assert theme.variables["--fs-radius"] == "1.1rem"
    assert theme.variables["--fs-surface-bg-light"] == "#f5f0ff"
    assert theme.variables["--fs-surface-bg-dark"] == "#17131f"
    assert theme.variables["--fs-surface-shadow"] == "0 20px 50px rgba(10, 10, 20, 0.2)"


def test_mode_specific_surface_tokens_apply_to_matching_mode():
    """Light/dark surface token overrides should resolve per mode."""
    theme = create_theme(
        surface_bg_light="#f7f4ff",
        surface_bg_dark="#15121d",
        surface_border_dark="rgba(255, 255, 255, 0.18)",
    )

    light_css = str(theme.to_style(mode="light"))
    dark_css = str(theme.to_style(mode="dark"))

    assert "--fs-surface-bg: #f7f4ff;" in light_css
    assert "--fs-surface-bg: #15121d;" in dark_css
    assert "--fs-surface-border: rgba(255, 255, 255, 0.18);" in dark_css
    assert "--fs-surface-bg-dark" not in dark_css


def test_theme_variant_css_outputs_light_and_dark_blocks():
    css = str(
        theme_variant_css(
            ".premium-card",
            light={"background": "#fff", "border_color": "#eee"},
            dark={"background": "#111", "border_color": "#333"},
        )
    )

    assert '[data-bs-theme="light"] .premium-card' in css
    assert "background: #fff;" in css
    assert "border-color: #eee;" in css
    assert '[data-bs-theme="dark"] .premium-card' in css
    assert "background: #111;" in css


def test_resolve_defaults_mechanics():
    """Test the priority logic of resolve_defaults."""
    reset_component_defaults()

    # 1. Omitted values use global defaults
    res = resolve_defaults("Button", variant=UNSET)
    assert res.get("variant") == "primary"

    # 2. Set global default
    set_component_defaults("Button", variant="success", size="lg")
    res = resolve_defaults("Button", variant=UNSET, size=UNSET)
    assert res["variant"] == "success"
    assert res["size"] == "lg"

    # 3. Explicit argument overrides global default
    res = resolve_defaults("Button", variant="danger", size=UNSET)
    assert res["variant"] == "danger"
    assert res["size"] == "lg"

    # 4. Explicit None clears a default
    res = resolve_defaults("Button", variant=None, size=UNSET)
    assert res["variant"] is None
    assert res["size"] == "lg"

    reset_component_defaults()


def test_add_bootstrap_integration():
    """Test add_bootstrap API with various themes and modes."""
    app = FastHTML()

    # String theme
    add_bootstrap(app, theme="green-nature", mode="dark")
    assert app.htmlkw["data-bs-theme"] == "dark"

    # Theme object
    app2 = FastHTML()
    theme = Theme({"--bs-primary": "#ff0000"})
    add_bootstrap(app2, theme=theme, mode="light")
    assert app2.htmlkw["data-bs-theme"] == "light"
    assert any("#ff0000" in str(a) for a in app2.hdrs)


def test_slot_classes_resolution():
    """Test resolution of slot classes (like header_cls)."""
    reset_component_defaults()
    set_component_defaults("Card", header_cls="bg-primary text-white")

    # No explicit override
    res = resolve_defaults("Card", header_cls=UNSET)
    assert res["header_cls"] == "bg-primary text-white"

    # Explicit None clears the slot class default
    res = resolve_defaults("Card", header_cls=None)
    assert res["header_cls"] is None

    # Explicit override
    res = resolve_defaults("Card", header_cls="custom-header")
    assert res["header_cls"] == "custom-header"

    reset_component_defaults()


def test_google_fonts_integration():
    """Test Google Fonts integration in add_bootstrap."""
    app = FastHTML()

    # Add bootstrap with Google Font
    add_bootstrap(app, font_family="Inter", font_weights=[400, 700])

    # Check that Google Fonts link is in headers
    hdrs_str = [str(h) for h in app.hdrs]
    assert any("fonts.googleapis.com" in s and "Inter" in s for s in hdrs_str)

    # Check that font-family CSS is in headers
    assert any("--bs-body-font-family" in s and "Inter" in s for s in hdrs_str)


def test_google_fonts_with_theme():
    """Test Google Fonts work with themes."""
    app = FastHTML()

    # Built-in theme + font
    add_bootstrap(app, theme="green-nature", font_family="Roboto")

    hdrs_str = [str(h) for h in app.hdrs]
    # Should have both theme and font
    assert any("#7BA05B" in s for s in hdrs_str)  # Theme color
    assert any("Roboto" in s for s in hdrs_str)  # Font


def test_google_fonts_default_weights():
    """Test that default font weights are applied when not specified."""
    app = FastHTML()

    add_bootstrap(app, font_family="Poppins")

    hdrs_str = [str(h) for h in app.hdrs]
    # Should use default weights [400, 500, 700]
    font_link = next((s for s in hdrs_str if "fonts.googleapis.com" in s and "Poppins" in s), None)
    assert font_link is not None
    assert "400" in font_link
    assert "500" in font_link
    assert "700" in font_link


def test_google_fonts_custom_weights():
    """Test custom font weights."""
    app = FastHTML()

    add_bootstrap(app, font_family="Inter", font_weights=[300, 600, 800])

    hdrs_str = [str(h) for h in app.hdrs]
    font_link = next((s for s in hdrs_str if "fonts.googleapis.com" in s and "Inter" in s), None)
    assert font_link is not None
    assert "300" in font_link
    assert "600" in font_link
    assert "800" in font_link


def test_google_fonts_with_spaces():
    """Test font names with spaces are properly URL-encoded."""
    app = FastHTML()

    add_bootstrap(app, font_family="Open Sans")

    hdrs_str = [str(h) for h in app.hdrs]
    # Should encode spaces as %20 (URL encoding)
    assert any("Open%20Sans" in s for s in hdrs_str)


def test_no_font_when_not_specified():
    """Test that no font link is added when font_family is None."""
    app = FastHTML()

    add_bootstrap(app, theme="green-nature")

    hdrs_str = [str(h) for h in app.hdrs]
    # Should not have Google Fonts link
    assert not any("fonts.googleapis.com" in s for s in hdrs_str)


def test_add_bootstrap_cdn_fallback_preserves_font_configuration(monkeypatch):
    """If local mounting fails, fallback CDN call should keep font settings."""
    app = FastHTML()

    monkeypatch.setattr(
        assets_module, "get_static_path", lambda: (_ for _ in ()).throw(RuntimeError)
    )
    add_bootstrap(
        app, use_cdn=False, mount_static=True, font_family="Inter", font_weights=[400, 600]
    )

    hdrs_str = [str(h) for h in app.hdrs]
    assert any("fonts.googleapis.com" in s and "Inter" in s for s in hdrs_str)
    assert any("wght@400;600" in s for s in hdrs_str)
