# -*- coding: utf-8 -*-
{
    'name': "Sale Customer Credit Limit",
    'summary': "Displays the customer's credit limit and related information directly on the sale order form.",
    'description': """
This module extends the Sale Order functionality by displaying the customer's credit limit, available credit, and Days Sales Outstanding (DSO) on the sale order form. 
These values are automatically fetched from the selected customer (partner) and kept up-to-date, allowing sales teams to quickly assess a customer's credit status before confirming sales.

Key Features:
- Shows customer credit limit on the sale order.
- Displays available credit and total receivables.
- Presents Days Sales Outstanding (DSO) for the selected customer.
- Enhances sales and credit control visibility.

Ideal for businesses that need to monitor customer credit directly from the sales process.
    """,

    'author': "Ismail Waxir",
    'website': "https://www.odoo.com/apps/modules/browse?author=Ismail%20Waxir",
    'category': 'Sales',
    'version': '18.0',
    'license': 'LGPL-3',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

    'images': [
        'static/description/icon.png',  # Logo/Icon
        'static/description/main_screenshot.png',  # First Feature/Screenshot
    ],

    'application': False,
    'installable': True,
}
