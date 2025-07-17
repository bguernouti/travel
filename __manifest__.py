# -*- coding: utf-8 -*-
{
    'name': "Travel",

    'summary': "Travel management",

    'description': """ 
    Travel management created by Billel and Salah
    """,

    'author': "Billel & Salah",

    'category': 'Sales/Sales',
    'version': '0.1',

    'depends': ['base', 'sale'],

    'data': [
        'security/res_groups.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/reports.xml',
        'reports/qweb_training.xml',
        'data/tags.xml',
        'data/fuel_types.xml',
        'data/types.xml',
        'data/ir_sequence.xml'
    ],

    "application": True
}

