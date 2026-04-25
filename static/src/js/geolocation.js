/** @odoo-module **/

import { Component, onMounted, useState } from "@odoo/owl";
import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";

export class StellarGeoCaptureField extends Component {
    setup() {
        this.state = useState({ status: "capturing" });
        onMounted(() => {
            if (!navigator.geolocation) {
                this.state.status = "unsupported";
                return;
            }
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    this.props.record.update({
                        geo_lat: position.coords.latitude,
                        geo_lng: position.coords.longitude,
                    });
                    this.state.status = "captured";
                },
                () => {
                    this.state.status = "denied";
                },
                {
                    enableHighAccuracy: true,
                    timeout: 10000,
                    maximumAge: 0,
                }
            );
        });
    }
}

StellarGeoCaptureField.template = "mobipine_odoo_project_management.StellarGeoCaptureField";
StellarGeoCaptureField.props = standardFieldProps;

registry.category("fields").add("stellar_geo_capture", {
    component: StellarGeoCaptureField,
});
