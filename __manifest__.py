{
    'name': "H2O",

    'summary': """Keep track the water sales and purchases""",

    'description': """
        Module to keep track of water sales and purchases
    """,

    'author': "[Xmarts], Josue Samuel Alfaro Montenegro (josue.alfaro@xmarts.com)",
    'website': "http://www.xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'SLI',
    'version': '14.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
        'contacts', 
        'sale_management',
        
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sequence.xml',
        'views/h2o_h2o_view.xml',
        'views/employee_employee_view.xml',
        'views/unidades_unidades_view.xml',
        'views/origen_travel_view.xml',
        'views/travel_cost_view.xml',
        'views/commission_commission_view.xml',
        'views/payment_driver_view.xml',
        'wizard/sale_order_wizard_view.xml',
        'views/sale_order_view.xml',
        
    ],

}
