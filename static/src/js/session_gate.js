/** @odoo-module **/

import { registry } from "@web/core/registry";
import { _t } from "@web/core/l10n/translation";

function isStellarCheckinError(error) {
    const data = error?.data || error?.message?.data;
    return Boolean(
        data &&
        data.name &&
        data.name.includes("StellarCheckinRequiredError")
    );
}

function buildCheckinModal(env) {
    const overlay = document.createElement("div");
    overlay.className = "stellar-checkin-modal-overlay";

    const modal = document.createElement("div");
    modal.className =
        "stellar-session-gate no-session stellar-checkin-modal";

    const title = document.createElement("h4");
    title.textContent = _t("Check-in Required");
    modal.appendChild(title);

    const body = document.createElement("p");
    body.className = "session-info";
    body.textContent = _t(
        "You must check in before you can access the system. Please check in to continue."
    );
    modal.appendChild(body);

    const actions = document.createElement("div");
    actions.className = "stellar-checkin-modal-actions";

    const checkinBtn = document.createElement("button");
    checkinBtn.className = "stellar-checkin-button";
    checkinBtn.textContent = _t("Check In Now");

    checkinBtn.onclick = async () => {
        if (document.body.contains(overlay)) {
            document.body.removeChild(overlay);
        }

        await env.services.action.doAction(
            "mobipine_odoo_project_management.action_attendance_checkin_wizard"
        );
    };

    actions.appendChild(checkinBtn);

    const dismissBtn = document.createElement("button");
    dismissBtn.className = "stellar-checkin-dismiss-button";
    dismissBtn.textContent = _t("Close");

    dismissBtn.onclick = () => {
        if (document.body.contains(overlay)) {
            document.body.removeChild(overlay);
        }
    };

    actions.appendChild(dismissBtn);

    modal.appendChild(actions);
    overlay.appendChild(modal);

    return overlay;
}

export const stellarSessionGateService = {
    start(env) {
        let modalOpen = false;

        const showCheckinModal = () => {
            if (modalOpen) {
                return;
            }

            modalOpen = true;

            const overlay = buildCheckinModal(env);

            document.body.appendChild(overlay);

            const cleanup = () => {
                modalOpen = false;
            };

            overlay.addEventListener("click", (ev) => {
                if (ev.target === overlay) {
                    if (document.body.contains(overlay)) {
                        document.body.removeChild(overlay);
                    }
                    cleanup();
                }
            });

            const observer = new MutationObserver(() => {
                if (!document.body.contains(overlay)) {
                    cleanup();
                    observer.disconnect();
                }
            });

            observer.observe(document.body, {
                childList: true,
            });
        };

        return {
            showCheckinModal,
            isStellarCheckinError,
        };
    },
};

registry.category("services").add(
    "stellar_session_gate",
    stellarSessionGateService
);