# -*- coding: utf-8 -*-
{
    "name": "HR Madagascar Leave Management",
    "summary": """
        "HR Madagascar Leave Management" is an Odoo Community module for managing leaves and absences in compliance 
        with Madagascar's legal requirements.""",
    "author": "Odoo Madagascar Community",
    "license": "LGPL-3",
    "support": "Odoo Madagascar Community",
    "images": ["static/img/background.png"],
    "development_status": "development",
    "maintainers": ["rivo2302"],
    "author": "Odoo Community Madagascar",
    "website": "https://github.com/Odoo-Madagascar-Community",
    "live_test_url": "https://www.facebook.com/groups/odoomadacommunity",
    "category": "Human Resources",
    "version": "16.0.1.1.1",
    "depends": [
        "base",
        "hr",
        "hr_holidays",
    ],
    "data": [
        # 'security/ir.model.access.csv',
        "views/views.xml",
        "views/templates.xml",
    ],
    "installable": True,
    "application": True,
    "price": "0",
    "currency": "USD",
}
