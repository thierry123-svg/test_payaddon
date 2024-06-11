# -*- coding: utf-8 -*-
{
    'name': "auto_createdit_remove",
    'version': '0.1',
    'summary': """
        This module is use to automatically remove the create edit option in view""",
    'sequence':-100,
    'description': """
        Long description of module's purpose
    """,
    'category': 'Uncategorized',
    'author': "Gattek Team",
    'maintainer': 'Gattek Team',
    'price': '50.0',
    'currency':'USD',
    'website': "https://ga-ttek.com",
    'license':'LGPL-3'
    'depends': [
        'base',
        'stock',
        'account',
        'purchase',
        'hr',
        'account_financial_report',
        'maintenance','repair'],
    'data': [
        'views/account_stock_employee_remove_option_view.xml',
        'views/purchase_remove_option_view.xml',
        'views/sale_remove_option_view.xml'
    ],
    'demo':[],
    'qweb':[],
    'images':['static/description/banner.gif'],
    'installable':True,
    'application':True,
    'auto_install':False,
}
