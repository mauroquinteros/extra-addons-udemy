# -*- coding: utf-8 -*-
{
    'name': "Custom CRM",

    'summary': """
        Módulo CRM para la gestión de visitas
    """,

    'description': """
        Módulo CRM para la gestión de visitas ...
    """,

    'author': "Mauro Quinteros",
    'website': "http://www.github.com/mauroquinteros",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/wizard.xml',
        'views/views.xml',
        'views/templates.xml',
        'reports/visit.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
