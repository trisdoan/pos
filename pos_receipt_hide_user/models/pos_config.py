from odoo import api, fields, models


class PosConfig(models.Model):
    _inherit = "pos.config"

    hide_user_option = fields.Selection(
        [("remove", "Remove"), ("replace", "Replace")],
        string="Hide User Options",
        default="remove",
    )


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    hide_user_option = fields.Selection(
        related="pos_config_id.hide_user_option", readonly=False
    )
