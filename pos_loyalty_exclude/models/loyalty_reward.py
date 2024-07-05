# Copyright 2024 Camptocamp (https://www.camptocamp.com).
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import models, api


class LoyaltyRule(models.Model):
    _inherit = "loyalty.rule"

    @api.depends("product_ids", "product_category_id", "product_tag_id")
    def _compute_valid_product_ids(self):
        super()._compute_valid_product_ids()
        for rule in self:
            rule.any_product = False
            excldue_products = rule.valid_product_ids.filtered("loyalty_exclude")
            rule.valid_product_ids = rule.valid_product_ids - excldue_products
        return True
