{
    'name': "Order History",
    'version': '1.2',
    'depends': ['base', 'sale_management', 'purchase'],
    'author': "Shahed Obaid",
    'sequence':200, 

    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_history.xml',
        'views/purchase_order_history.xml',
        'wizards/order_line_history_view.xml'
    ],
    'installable': True,
    # 'application': True,   # its just a module so no need for this
    'auto_install': False,
    'license': 'LGPL-3',
}