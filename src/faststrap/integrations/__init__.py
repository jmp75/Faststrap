"""Optional third-party integrations for Faststrap."""

from .chartjs import (
    CHARTJS_CDN_URL,
    CHARTJS_VERSION,
    ChartJS,
    ChartJSType,
    add_chartjs,
    chartjs_assets,
)
from .gsap import (
    GSAP_CDN_URL,
    GSAP_VERSION,
    Gsap,
    GsapPreset,
    GsapReveal,
    Motion,
    MotionPreset,
    add_gsap,
    gsap_assets,
)

__all__ = [
    "CHARTJS_CDN_URL",
    "CHARTJS_VERSION",
    "ChartJS",
    "ChartJSType",
    "add_chartjs",
    "chartjs_assets",
    "GSAP_CDN_URL",
    "GSAP_VERSION",
    "Gsap",
    "GsapPreset",
    "GsapReveal",
    "Motion",
    "MotionPreset",
    "add_gsap",
    "gsap_assets",
]
