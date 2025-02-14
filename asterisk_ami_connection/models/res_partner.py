from odoo import models, fields, api
from odoo.exceptions import UserError


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def action_call_phone(self):
        """Initiates a VoIP call to the partner's phone number"""
        if not self.phone:
            raise UserError("No phone number found for this contact.")

        user_extension = self.env.user.asiapardaz_extension
        if not user_extension:
            raise UserError("Your VoIP extension is not set.")

        # Initiate the call using Odoo RPC or API
        self.env['asiapardaz.voip'].originate_call(self.phone)

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': "VoIP Call",
                'message': f"Calling {self.phone}...",
                'sticky': False,
            }
        }

    def action_call_mobile(self):
        """Initiates a VoIP call to the partner's mobile number"""
        if not self.mobile:
            raise UserError("No mobile number found for this contact.")

        user_extension = self.env.user.asiapardaz_extension
        if not user_extension:
            raise UserError("Your VoIP extension is not set.")

        # Initiate the call using Odoo RPC or API
        self.env['asiapardaz.voip'].originate_call(self.mobile)

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': "VoIP Call",
                'message': f"Calling {self.mobile}...",
                'sticky': False,
            }
        }
