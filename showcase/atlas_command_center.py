"""Flagship v0.7.0 showcase - Atlas Command Center.

A premium operations dashboard that proves the v0.7.0 component wave works together:

- CommandPalette for quick navigation/search
- ChartJS optional integration for rich charts
- ModernToast for polished feedback
- Timeline for incident/audit activity
- AvatarGroup and StatusBadge for team/status context
- DataTable query helpers and Pagination HTMX ergonomics
- theme_variant_css for light/dark surface variants
"""

from __future__ import annotations

from fasthtml.common import H1, H5, Div, FastHTML, P, Span, Style, serve

from faststrap import (
    Avatar,
    AvatarGroup,
    BadgeGroup,
    Button,
    Card,
    ChartJS,
    Col,
    CommandItem,
    CommandPalette,
    ConfirmAction,
    Container,
    DataTable,
    Icon,
    ModernToast,
    ModernToastStack,
    Pagination,
    ResultCard,
    Row,
    StatCard,
    StatusBadge,
    Timeline,
    TimelineItem,
    add_bootstrap,
    add_chartjs,
    create_theme,
    theme_variant_css,
)

ATLAS_THEME = create_theme(
    primary="#2563EB",
    secondary="#111827",
    success="#10B981",
    danger="#EF4444",
    warning="#F59E0B",
    info="#06B6D4",
)

app = FastHTML()
add_bootstrap(app, theme=ATLAS_THEME, mode="dark", font_family="Inter")
add_chartjs(app)

CHART_DATA = {
    "labels": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "datasets": [
        {
            "label": "Resolved incidents",
            "data": [18, 24, 21, 31, 34, 29, 37],
            "borderColor": "#38BDF8",
            "backgroundColor": "rgba(56, 189, 248, 0.18)",
            "tension": 0.35,
            "fill": True,
        },
        {
            "label": "Open incidents",
            "data": [11, 9, 12, 8, 7, 6, 5],
            "borderColor": "#F59E0B",
            "backgroundColor": "rgba(245, 158, 11, 0.12)",
            "tension": 0.35,
            "fill": True,
        },
    ],
}

INCIDENTS = [
    {"id": "INC-1042", "service": "Payments", "severity": "High", "owner": "Ada"},
    {"id": "INC-1041", "service": "Search", "severity": "Medium", "owner": "Grace"},
    {"id": "INC-1038", "service": "Auth", "severity": "Low", "owner": "Alan"},
    {"id": "INC-1037", "service": "API", "severity": "High", "owner": "Katherine"},
]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700&display=swap');

.atlas-shell {
  min-height: 100vh;
  background:
    radial-gradient(circle at 8% 8%, rgba(37, 99, 235, 0.28), transparent 28%),
    radial-gradient(circle at 90% 10%, rgba(6, 182, 212, 0.18), transparent 26%),
    linear-gradient(180deg, #030712 0%, #07111f 48%, #0b1220 100%);
  color: #e5eefc;
}

.atlas-shell[data-bs-theme="light"] {
  background:
    radial-gradient(circle at 8% 8%, rgba(37, 99, 235, 0.09), transparent 30%),
    radial-gradient(circle at 90% 10%, rgba(6, 182, 212, 0.09), transparent 28%),
    linear-gradient(180deg, #eef5ff 0%, #f8fbff 54%, #eef4fb 100%);
  color: #0f172a;
}

.atlas-title {
  font-family: 'Space Grotesk', sans-serif;
  letter-spacing: -0.045em;
}

.atlas-card {
  border: 1px solid rgba(148, 163, 184, 0.18) !important;
  background: rgba(15, 23, 42, 0.62) !important;
  backdrop-filter: blur(18px);
  border-radius: 18px !important;
  box-shadow: 0 22px 70px rgba(0, 0, 0, 0.22);
}

.atlas-shell[data-bs-theme="light"] .atlas-card {
  background: rgba(255, 255, 255, 0.82) !important;
  border-color: rgba(37, 99, 235, 0.14) !important;
  box-shadow: 0 22px 70px rgba(15, 23, 42, 0.08);
}

.atlas-command .faststrap-command-palette {
  background: transparent;
  border: 0;
  box-shadow: none !important;
}

.atlas-command .faststrap-command-item:hover {
  background: rgba(37, 99, 235, 0.12);
}

.atlas-stat.faststrap-stat-card { min-height: 100%; }
.atlas-section-label { color: rgba(226, 232, 240, 0.66); }
.atlas-shell[data-bs-theme="light"] .atlas-section-label { color: rgba(15, 23, 42, 0.58); }
""" + theme_variant_css(
    ".atlas-live-panel",
    light={"background": "rgba(255, 255, 255, 0.74)"},
    dark={"background": "rgba(2, 6, 23, 0.34)"},
)


def command_palette() -> CommandPalette:
    return CommandPalette(
        CommandItem(
            "Open incidents",
            description="Review unresolved incidents",
            icon="activity",
            shortcut="G I",
            href="#incidents",
        ),
        CommandItem(
            "Invite responder",
            description="Add a teammate to the war room",
            icon="person-plus",
            shortcut="I R",
            href="#team",
        ),
        CommandItem(
            "Export report",
            description="Download the weekly operations packet",
            icon="download",
            shortcut="E R",
            href="#report",
        ),
        id="atlas-command",
        placeholder="Search commands...",
        title=None,
        cls="atlas-command",
    )


def page() -> Div:
    query_params = DataTable.query_params(
        sort="severity",
        direction="desc",
        search="incident",
        filters={"status": "open"},
        page=1,
        per_page=4,
    )
    next_page = DataTable.page_url(
        "/", page=2, per_page=4, sort="severity", filters={"status": "open"}
    )

    return Div(
        Style(CSS),
        Container(
            Div(
                Div(
                    Span("ATLAS", cls="badge text-bg-primary rounded-pill mb-3"),
                    H1(
                        "Command center for teams that ship under pressure",
                        cls="atlas-title display-4 fw-bold mb-3",
                    ),
                    P(
                        "A v0.7.0 Faststrap reference for operations dashboards: command palette, data helpers, rich charts, toasts, timelines, and team surfaces in one shell.",
                        cls="lead text-muted mb-0",
                    ),
                    cls="col-lg-8",
                ),
                Div(
                    AvatarGroup(
                        Avatar("Ada Lovelace", status="online", size="lg"),
                        Avatar("Alan Turing", status="busy", size="lg"),
                        Avatar("Grace Hopper", status="away", size="lg"),
                        total=9,
                        max_visible=3,
                        size="lg",
                    ),
                    BadgeGroup(
                        StatusBadge("Live ops", status="active", show_dot=True),
                        StatusBadge("P95 stable", status="success", show_dot=True),
                    ),
                    cls="col-lg-4 d-grid gap-3 justify-content-lg-end align-content-center",
                    id="team",
                ),
                cls="row g-4 align-items-center py-5",
            ),
            Row(
                Col(
                    StatCard(
                        "MTTR",
                        "18m",
                        delta="-22%",
                        delta_type="up",
                        icon=Icon("stopwatch"),
                        cls="atlas-card atlas-stat",
                    ),
                    cols=12,
                    md=6,
                    xl=3,
                ),
                Col(
                    StatCard(
                        "Incidents",
                        "42",
                        delta="+8",
                        delta_type="down",
                        icon=Icon("activity"),
                        cls="atlas-card atlas-stat",
                    ),
                    cols=12,
                    md=6,
                    xl=3,
                ),
                Col(
                    StatCard(
                        "Uptime",
                        "99.98%",
                        delta="SLO met",
                        delta_type="up",
                        icon=Icon("shield-check"),
                        cls="atlas-card atlas-stat",
                    ),
                    cols=12,
                    md=6,
                    xl=3,
                ),
                Col(
                    StatCard(
                        "Deploys",
                        "128",
                        delta="+16%",
                        delta_type="up",
                        icon=Icon("rocket-takeoff"),
                        cls="atlas-card atlas-stat",
                    ),
                    cols=12,
                    md=6,
                    xl=3,
                ),
                cls="g-4 mb-4",
            ),
            Row(
                Col(
                    Card(H5("Command palette", cls="mb-3"), command_palette(), cls="atlas-card"),
                    cols=12,
                    lg=5,
                ),
                Col(
                    Card(
                        H5("Incident trend", cls="mb-3"),
                        ChartJS("atlas-incidents", type="line", data=CHART_DATA, height=230),
                        cls="atlas-card",
                    ),
                    cols=12,
                    lg=7,
                ),
                cls="g-4 mb-4",
            ),
            Row(
                Col(
                    Card(
                        H5("Open incidents", cls="mb-3", id="incidents"),
                        DataTable(
                            INCIDENTS,
                            sortable=True,
                            searchable=True,
                            pagination=True,
                            per_page=2,
                            base_url="/",
                            filters={"status": "open"},
                        ),
                        Div(
                            P(
                                f"Reusable query contract: {query_params}",
                                cls="small text-muted mb-1",
                            ),
                            P(f"Next page URL: {next_page}", cls="small text-muted mb-0"),
                            cls="atlas-live-panel rounded-4 border p-3 mt-3",
                        ),
                        Pagination(
                            current_page=1,
                            total_pages=4,
                            base_url="/",
                            query_params={"status": "open"},
                            htmx=True,
                            hx_target="#incidents",
                            hx_push_url=True,
                            cls="mt-3",
                        ),
                        cls="atlas-card",
                    ),
                    cols=12,
                    lg=7,
                ),
                Col(
                    Card(
                        H5("Activity stream", cls="mb-3"),
                        Timeline(
                            TimelineItem(
                                "Payment latency recovered",
                                description="Traffic shifted back to primary region.",
                                time="4m ago",
                                icon="check",
                                variant="success",
                                active=True,
                            ),
                            TimelineItem(
                                "Responder invited",
                                description="Grace joined the payments war room.",
                                time="12m ago",
                                icon="person-plus",
                                variant="info",
                            ),
                            TimelineItem(
                                "Deploy guard enabled",
                                description="Risky deploys now require approval.",
                                time="28m ago",
                                icon="shield-lock",
                                variant="warning",
                            ),
                        ),
                        cls="atlas-card",
                    ),
                    cols=12,
                    lg=5,
                ),
                cls="g-4 mb-4",
            ),
            Row(
                Col(
                    ResultCard(
                        "Weekly packet ready",
                        "The incident digest can be exported or archived.",
                        status="success",
                        action=Button("Download report", variant="primary"),
                        cls="atlas-card",
                    ),
                    cols=12,
                    lg=8,
                ),
                Col(
                    Card(
                        H5("Safe destructive action", cls="mb-3"),
                        ConfirmAction(
                            "Archive digest",
                            url="/archive",
                            method="delete",
                            confirm="Archive this digest?",
                            target="#archive-result",
                            swap="outerHTML",
                        ),
                        Div(id="archive-result", cls="mt-3"),
                        cls="atlas-card",
                    ),
                    cols=12,
                    lg=4,
                ),
                cls="g-4 pb-5",
            ),
        ),
        ModernToastStack(
            ModernToast(
                "Ops digest ready",
                "Weekly summary generated successfully.",
                variant="success",
                style="glass",
            ),
            position="top-end",
        ),
        cls="atlas-shell",
        data_bs_theme="dark",
    )


@app.get("/")
def home():
    return page()


@app.delete("/archive")
def archive():
    return ResultCard(
        "Archived", "The digest was archived.", status="success", compact=True, id="archive-result"
    )


if __name__ == "__main__":
    serve(port=5028)
