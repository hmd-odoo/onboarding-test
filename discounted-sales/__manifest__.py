{
	'name': 'Sale Discounts',
	'depends':[
		'base',
        'sale',
		'account',
	],
    'data': [
    #     'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/account_move_views.xml',
    #     'views/estate_property_views.xml',
	# 	'views/estate_type_views.xml',
	# 	'views/estate_offer_views.xml',
	# 	'views/res_views.xml'
	],
	'application':True
}
