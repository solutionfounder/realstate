# -*- coding: utf-8 -*-
{
    'name': "Enter Petty Cash and Bank Transfer",
    'summary': """Enter your petty cash into accounting system or direct enter your income and expense for office hardware or supplies or stationaries or old assests for bank transfer""",
    'description': """Enter your petty cash into accounting system or direct enter your income and expense for office hardware or supplies or stationaries or old assests for bank transfer""",
    'version': '15.0.0',
    'category': 'Accounting',
    'author':'Preciseways',
    'website': "http://www.preciseways.com",
    'depends': ['account', 'l10n_generic_coa'],
    'data': [
    	'data/ir_sequence.xml',
     	'security/ir.model.access.csv',
        'views/lc_direct_transfer_view.xml',
        'views/account_deshbord.xml',
    ],
    'installable': True,
    'application': True,
    'price': 15.0,
    'currency': 'EUR',
    'images':['static/description/banner.png'],
    'license': 'OPL-1',
}