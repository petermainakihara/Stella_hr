/** @odoo-module */

import { ActivityMenu } from "@hr_attendance/components/attendance_menu/attendance_menu";
import { rpc } from "@web/core/network/rpc";
import { patch } from "@web/core/utils/patch";

patch(ActivityMenu.prototype, {
    setup() {
        super.setup(...arguments);
        this.actionService = this.env.services.action;
    },

    async signInOut() {
        this.dropdown.close();
        if (this._attendanceInProgress) {
            return;
        }
        this._attendanceInProgress = true;

        try {
            if (!this.state.checkedIn) {
                const actionService = this.actionService || this.env.services.action;
                if (!actionService) {
                    throw new Error("Attendance action service is unavailable.");
                }
                await actionService.doAction("mobipine_odoo_project_management.action_attendance_checkin_wizard");
                return;
            }

            await rpc("/hr_attendance/systray_check_in_out", {});
            window.location.reload();
        } finally {
            this._attendanceInProgress = false;
        }
    },
});