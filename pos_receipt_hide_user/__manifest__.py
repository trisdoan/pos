# -*- coding: utf-8 -*-
{
    "name": "POS Receipt Hide User",
    "summary": "Add button to remove user from receipt.",
    "author": "Tris Doan",
    "website": "https://github.com/OCA/pos",
    "category": "Point of Sale",
    "version": "16.0.1.0.0",
    "depends": ["point_of_sale"],
    "assets": {
        "point_of_sale.assets": [
            "pos_receipt_hide_user/static/src/js/receipt_screen.js",
            "pos_receipt_hide_user/static/src/js/order_receipt.js",
            "pos_receipt_hide_user/static/src/xml/**/*"
        ],
    },
    "data": [
        "views/res_config_settings.xml"
    ]
}
