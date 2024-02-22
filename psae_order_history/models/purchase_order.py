from odoo import models

class ProductVariants(models.Model):
    _inherit = "purchase.order"

    def action_view_po_history(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "res_model": "order.line.history",
            "name": "Purchase Order History",
            'view_mode': 'form',
            "target": "new",    # make a new pop-up 
            "context": {"active_model": 'purchase.order'},
        }