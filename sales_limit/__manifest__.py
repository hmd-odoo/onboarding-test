{
    'name': 'What Ever I want it to be for the customer to understand the module',
    'summary': 'block confirming sales orders where the total is greater than the sales order limit',
    'depends': [
        'base',
        'account',
        'sale',
    ],
    'data': [
       "views/view_partner_form.xml",
    ],
    'application': True,
}