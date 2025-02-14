odoo.define('asia_call.AsiaCall', function (require) {
    "use strict";

    var FormRenderer = require('web.FormRenderer');
    var rpc = require('web.rpc');

    FormRenderer.include({
        _renderTagLabel: function (node) {
            var $label = this._super.apply(this, arguments);

            if (node.attrs.for === 'phone' || node.attrs.for === 'mobile') {
                var fieldName = node.attrs.for;

                // Style the label to indicate it is clickable
                $label.css({ "color": "blue", "cursor": "pointer", "text-decoration": "underline" });

                // Add click event
                $label.on('click', function (e) {
                    e.preventDefault();

                    // Find phone number value
                    var phoneNumber = $("input[name='" + fieldName + "']").val() || $("span[name='" + fieldName + "']").text().trim();

                    if (!phoneNumber) {
                        alert("No phone number found!");
                        return;
                    }

                    // Get user extension from session context
                    var userExtension = odoo.session_info.user_context['user_extension_for_asia_call'];
                    if (!userExtension) {
                        alert("User extension is not set!");
                        return;
                    }

                    rpc.query({
                        route: '/asia_call/originate_call',
                        params: {
                            phone_number: phoneNumber,
                            user_extension: userExtension,
                        },
                    }).then(function (result) {
                        if (result.error) {
                            alert("Error: " + result.error);
                        } else {
                            alert("Success: Call initiated.");
                        }
                    }).catch(function (err) {
                        alert("RPC Error: " + err);
                    });
                });
            }

            return $label;
        },
    });
});
