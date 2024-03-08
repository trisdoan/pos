# Copyright 2024 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models, api

class HrEmployee(models.Model):
    _inherit = "hr.employee"

    pos_trigram = fields.Char(related="work_contact_id.pos_trigram")