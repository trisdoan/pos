from odoo import api, fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    hide_user_option = fields.Selection(
        related="pos_config_id.hide_user_option", readonly=False
    )
