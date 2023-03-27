# -*- coding: utf-8 -*-
{
    "name": "HR Payroll Malagasy",
    "summary": """Manage employee leave requests and calculate paid leave balances
    according to Malagasy regulations""",
    "author": "Odoo Madagascar Community",
    "license": "LGPL-3",
    "support": "Odoo Madagascar Community",
    "images": ["static/img/background.png"],
    "development_status": "development",
    "maintainers": ["rivo2302" ,"BriceCG"],
    "author": "Odoo Community Madagascar",
    "website": "https://github.com/Odoo-Madagascar-Community",
    "live_test_url": "https://www.facebook.com/groups/odoomadacommunity",
    "category": "Human Resources",
    "version": "0.1",
    "depends": ["hr", "hr_holidays", "om_hr_payroll"],
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
        "views/templates.xml",
    ],
    "installable": True,
    "application": True,
    "sequence": "1",
    "price": "0",
    "currency": "USD",
}
