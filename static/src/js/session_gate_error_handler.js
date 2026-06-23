/** @odoo-module **/

import { registry } from "@web/core/registry";

function stellarCheckinErrorHandler(env, error, originalError) {
    const data = originalError?.data || error?.data;
    const name = data?.name || "";
    if (name.includes("StellarCheckinRequiredError")) {
        const gate = env.services.stellar_session_gate;
        if (gate) {
            gate.showCheckinModal();
            return true; // mark as handled, suppress default error dialog
        }
    }
    return false;
}

registry.category("error_handlers").add("stellarCheckinErrorHandler", stellarCheckinErrorHandler, {
    sequence: 1,
});