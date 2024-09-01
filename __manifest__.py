# -*- coding: utf-8 -*-
{
    'name': "sale_order_versioning",

    'summary': "This module will help to create different versions of saleorder",

    'description': """
This module will help to create different versions of saleorder
    """,

    'author': "NIZAMUDHEEN MJ",
    'website': "www.linkedin.com/in/nizamudheen-m-j",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'sale',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/sale_order_version_views.xml',
        'wizard/version_wizard_views.xml',
        'wizard/sale_order_version_restore_wizard_views.xml',
    ],
    'application': True,
    'sequence': -96,
}

