# Copyright 2024 Camptocamp (<https://www.camptocamp.com>).
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from odoo.addons.pos_loyalty.tests.test_frontend import TestUi


class TestPosLoyaltyExclude(TestUi):

    def test_exclude_loyalty_program(self):
        self.env["loyalty.program"].search([]).write({"active": False})
        self.test_product_1 = self.env["product.product"].create(
            {
                "name": "Product Exclude Loyalty",
                "type": "product",
                "list_price": 100,
                "available_in_pos": True,
                "loyalty_exclude": True,
                "taxes_id": False,
            }
        )
        self.test_product_2 = self.env["product.product"].create(
            {
                "name": "Product Include Loyalty",
                "type": "product",
                "list_price": 100,
                "available_in_pos": True,
                "loyalty_exclude": False,
                "taxes_id": False,
            }
        )
        self.loyalty_program = self.env["loyalty.program"].create(
            {
                "name": "Loyalty Program",
                "program_type": "loyalty",
                "pos_ok": True,
                "rule_ids": [
                    (
                        0,
                        0,
                        {
                            "minimum_amount": 1,
                            "minimum_qty": 1,
                            "reward_point_mode": "order",
                            "reward_point_amount": 500,
                        },
                    )
                ],
                "reward_ids": [
                    (
                        0,
                        0,
                        {
                            "required_points": 500,
                            "reward_type": "discount",
                            "discount": "10",
                            "discount_mode": "per_order",
                        },
                    )
                ],
            }
        )

        partner = self.env["res.partner"].create({"name": "Mr Odoo"})
        self.env["loyalty.card"].create(
            {
                "partner_id": partner.id,
                "program_id": self.loyalty_program.id,
                "points": 500,
            }
        )

        self.main_pos_config.open_ui()

        self.start_tour(
            "/pos/web?config_id=%d" % self.main_pos_config.id,
            "PosExcludeLoyaltyPromotion",
            login="accountman",
        )
