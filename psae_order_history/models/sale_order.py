from odoo import api, models, fields

class SaleOrder(models.Model):
    _inherit = "sale.order"


    def action_view_so_history(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "res_model": "order.line.history",
            "name": "Sales Order History",
            'view_mode': 'form',
            # 'view_id':"view_so_history",
            "target": "new",    # make a new pop-up 
            # 'domain': [('id', 'in', self.order_line.product_id.ids)],  
            "context": {"active_model": 'sale.order'},
            # "res_id": self.order_line.id or self.id
        }
    

    # for all sale orders in the database --> "res_model": "sale.order",
    # for the sale order lines in one sale orrder --> 
