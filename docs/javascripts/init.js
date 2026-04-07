function getMaterialScheme() {
    return (
        document.body?.getAttribute("data-md-color-scheme") ||
        document.documentElement.getAttribute("data-md-color-scheme") ||
        "default"
    );
}

function syncBootstrapTheme() {
    const scheme = getMaterialScheme();
    const bootstrapTheme = scheme === "slate" ? "dark" : "light";

    document.documentElement.setAttribute("data-bs-theme", bootstrapTheme);

    if (document.body) {
        document.body.setAttribute("data-bs-theme", bootstrapTheme);
    }
}

function initializeBootstrapOverlays(root = document) {
    if (typeof bootstrap === "undefined") {
        return;
    }

    const tooltipTriggerList = Array.from(
        root.querySelectorAll('[data-bs-toggle="tooltip"]'),
    );
    tooltipTriggerList.forEach((tooltipTriggerEl) => {
        bootstrap.Tooltip.getOrCreateInstance(tooltipTriggerEl);
    });

    const popoverTriggerList = Array.from(
        root.querySelectorAll('[data-bs-toggle="popover"]'),
    );
    popoverTriggerList.forEach((popoverTriggerEl) => {
        bootstrap.Popover.getOrCreateInstance(popoverTriggerEl);
    });
}

function observeThemeChanges() {
    const sync = () => syncBootstrapTheme();
    const targets = [document.documentElement, document.body].filter(Boolean);

    targets.forEach((target) => {
        new MutationObserver(sync).observe(target, {
            attributes: true,
            attributeFilter: ["data-md-color-scheme"],
        });
    });
}

document.addEventListener("DOMContentLoaded", function () {
    syncBootstrapTheme();
    initializeBootstrapOverlays();
    observeThemeChanges();
});
