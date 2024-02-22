{
    'name': 'Sales / Purchase history',
    'depends': ['sale','purchase'],
    'version': '0.1',
    'author': 'KHOM',
    'category': 'Sales',
    'installable': True,
    'description': 'View the history of Sales / Purchases',
    'data': [
        # Security
        'security/ir.model.access.csv',
        # Views
        'views/sale_order_views.xml',
        'views/purchase_order_views.xml',
        'views/product_sale_history_views.xml',
    ]
}
