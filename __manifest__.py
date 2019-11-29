# -*- coding: utf-8 -*-
{
    'name': "vit_accounting_asset",

    'summary': """
        inherit field detail ke form asset di model accounting""",

    'description': """
        inherit field detail ke form asset di model accounting
    """,

    'author': "firmanrizaldiyusup@gmail.com",
    'website': "http://www.vitraining.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','om_account_asset'],

    # always loaded
    'data': [
        'views/asset_detail.xml',
    ],
  
}