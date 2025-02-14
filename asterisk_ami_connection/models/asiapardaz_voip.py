from asterisk.ami import AMIClient, SimpleAction
from mako.runtime import Context
from odoo import models, fields, api, _
import asterisk.ami
from odoo.addons.mail.models.discuss.discuss_channel import Channel
from speechd import Priority
from odoo.exceptions import UserError


class AsiapardazVoip(models.Model):
    _name = 'asiapardaz.voip'
    _description = 'Asiapardaz VoIP Integration'

    def originate_call(self, phone_number):
        """Initiate a call via Asterisk AMI."""
        server = self.env['ir.config_parameter'].sudo().get_param('asiapardaz_voip.server')
        port = int(self.env['ir.config_parameter'].sudo().get_param('asiapardaz_voip.port', default=5038))
        ami_user = self.env['ir.config_parameter'].sudo().get_param('asiapardaz_voip.user')
        ami_password = self.env['ir.config_parameter'].sudo().get_param('asiapardaz_voip.password')
        context = self.env['ir.config_parameter'].sudo().get_param('asiapardaz_voip.context', default='from-internal')
        user_extension = self.env.user.asiapardaz_extension  # Get the current user's extension

        try:
            # Create AMI Client
            client = AMIClient(address=f'{server}', port=port)
            client.login(username=f'{ami_user}', secret=f'{ami_password}')

            # Ensure the socket is initialized
            if not client._socket:
                raise UserError("Could not connect to AMI")

            # Prepare call action
            action = SimpleAction(
                'Originate',
                Channel = f'pjsip/{user_extension}',
                Exten = f'{phone_number}',
                Priority = 1,
                Context = context,
                Async = True,
                CallerID = f'{phone_number}',
            )


            # Send the call request
            response = client.send_action(action)

            # Close connection
            client.logoff()

            # Check response from Asterisk
            # if response and response.get('Response') != 'Success':
            #     raise UserError("An Error Occured")

        except :
            raise UserError("An Error Occured")
