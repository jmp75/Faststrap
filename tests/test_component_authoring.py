"""Guardrails for component authoring conventions."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WRAPPER_FILES = {
    "src/faststrap/components/display/sheet.py",
    "src/faststrap/components/display/stat_card.py",
    "src/faststrap/components/feedback/confirm.py",
    "src/faststrap/components/feedback/error_dialog.py",
    "src/faststrap/components/feedback/install_prompt.py",
    "src/faststrap/components/feedback/notifications.py",
    "src/faststrap/components/forms/errors.py",
    "src/faststrap/components/patterns/navbar.py",
}


def iter_component_files() -> list[Path]:
    files: list[Path] = []
    for pattern in (
        "src/faststrap/components/**/*.py",
        "src/faststrap/layouts/*.py",
        "src/faststrap/presets/interactions.py",
        "src/faststrap/accessibility.py",
    ):
        files.extend(ROOT.glob(pattern))
    return [path for path in files if path.name != "__init__.py"]


def test_component_files_with_kwargs_reference_convert_attrs() -> None:
    missing: list[str] = []

    for path in iter_component_files():
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(ROOT).as_posix()
        if rel in WRAPPER_FILES:
            continue
        if "**kwargs" in text and "convert_attrs(" not in text:
            missing.append(rel)

    assert not missing, (
        "Component files that accept **kwargs should route attributes through "
        f"convert_attrs(): {missing}"
    )
