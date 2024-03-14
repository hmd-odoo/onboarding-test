from odoo import fields, models,Command, exceptions


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def action_confirm(self):
            if (self.amount_total > self.partner_id.sale_order_limit_used):
                print('partner id: ', self.partner_id)
                print('partner name: ', self.partner_id.name)
                print('amount total:', self.amount_total)
                print('sale limit used: ', self.partner_id.sale_order_limit_used)
                print('sale limit used: ', self.partner_id.sale_order_limit)
                raise exceptions.UserError('The sale order total exceeds the sale order limit of the user!')
            return super().action_confirm()