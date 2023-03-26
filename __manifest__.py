# -*- coding: utf-8 -*-
{
    'name': "HR Madagascar Leave Management",

    'summary': """
        "HR Madagascar Leave Management" is an Odoo Community module for managing leaves and absences in compliance 
        with Madagascar's legal requirements.""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Odoo Community Madagascar",
    'website': "https://github.com/Odoo-Madagascar-Community",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
