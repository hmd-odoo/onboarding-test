from odoo import api, models, fields

class ProductVariants(models.Model):
    _inherit = "purchase.order"

    def action_view_po_history(self):
        self.ensure_one()
        return {
            "type": "ir.actions.act_window",
            "res_model": "order.line.history",
            "name": "Purchase Order History",
            'view_mode': 'form',
            # 'view_id':"view_po_history",
            "target": "new",    # make a new pop-up 
            # 'domain': [('id', 'in', self.order_line.product_id.ids)],  
            "context": {"active_model": 'purchase.order'},
            # "res_id": self.order_line.id or self.id
        }