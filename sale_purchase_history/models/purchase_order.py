from odoo import models, _


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    def action_view_history(self):
        return {
            'name': _('View History'),
            'res_model': 'product.sale.history',
            'view_mode': 'form',
            'view_id': self.env.ref('sale_purchase_history.product_sale_history_form').id,
            'context': {
                'active_model': 'purchase.order',
            },
            'target': 'new',
            'type': 'ir.actions.act_window',
        }
