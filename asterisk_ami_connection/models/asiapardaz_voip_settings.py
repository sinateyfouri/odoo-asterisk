from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    _description = 'Asiapardaz VoIP Settings'

    use_asiapardaz_voip = fields.Boolean(string="", config_parameter='asiapardaz_voip.use_feature')
    asiapardaz_server = fields.Char(string="Server Address")
    asiapardaz_port = fields.Char(string="AMI Port")
    asiapardaz_user = fields.Char(string="AMI User")
    asiapardaz_password = fields.Char(string="AMI Password")
    asiapardaz_context = fields.Char(string="Context")

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param('asiapardaz_voip.use_feature', self.use_asiapardaz_voip)
        self.env['ir.config_parameter'].set_param('asiapardaz_voip.server', self.asiapardaz_server)
        self.env['ir.config_parameter'].set_param('asiapardaz_voip.port', self.asiapardaz_port)
        self.env['ir.config_parameter'].set_param('asiapardaz_voip.user', self.asiapardaz_user)
        self.env['ir.config_parameter'].set_param('asiapardaz_voip.password', self.asiapardaz_password)
        self.env['ir.config_parameter'].set_param('asiapardaz_voip.context', self.asiapardaz_context)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        params = self.env['ir.config_parameter'].sudo()
        res.update(
            use_asiapardaz_voip=params.get_param('asiapardaz_voip.server', default=''),
            asiapardaz_server=params.get_param('asiapardaz_voip.server', default=''),
            asiapardaz_port=params.get_param('asiapardaz_voip.port', default=''),
            asiapardaz_user=params.get_param('asiapardaz_voip.user', default=''),
            asiapardaz_password=params.get_param('asiapardaz_voip.password', default=''),
            asiapardaz_context=params.get_param('asiapardaz_voip.context', default=''),
        )
        return res