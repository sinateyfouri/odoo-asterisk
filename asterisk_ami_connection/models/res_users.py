from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users'
    asiapardaz_extension = fields.Char(string="User Extension for Asiapardaz VoIP")