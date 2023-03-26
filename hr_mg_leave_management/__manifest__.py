# -*- coding: utf-8 -*-
{
    "name": "HR Leave Management Madagascar",
    "summary": (
        "Manage employee leave requests and calculate paid leave balances"
        " according to Malagasy regulations"
    ),
    "description": (
        "This module allows managers to approve or reject employee leave"
        " requests and automatically calculates paid leave balances based on"
        " days worked and leave already taken. It includes support for various"
        " types of paid leave mandated by Malagasy regulations, including"
        " annual leave, sick leave, and maternity leave. Employees can view"
        " their remaining paid leave balances and request leave directly from"
        " their Odoo profile. Managers can generate reports to track leave"
        " requests, leave balances, and past absences for each employee."
    ),
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
    "version": "0.1",
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
    "sequence": "1",
    "price": "0",
    "currency": "USD",
}
