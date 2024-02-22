from odoo import models

class SaleOrder(models.Model):
    _inherit = "sale.order"


    def action_view_so_history(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "res_model": "order.line.history",
            "name": "Sales Order History",
            'view_mode': 'form',
            "target": "new",    # make a new pop-up 
            "context": {"active_model": 'sale.order'},
        }
    