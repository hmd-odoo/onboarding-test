from odoo import api, fields, models


class ProductSaleHistory(models.TransientModel):
    _name = 'product.sale.history'

    product_id = fields.Many2one('product.product')
    is_sale = fields.Boolean(default=lambda self: self.env.context.get('is_sale', False))
    is_purchase = fields.Boolean(default=lambda self: self.env.context.get('is_purchase', False))
    sale_order_lines = fields.Many2many('sale.order.line', compute='_compute_previous_order_history', readonly=True)
    purchase_order_lines = fields.Many2many('purchase.order.line', compute='_compute_previous_order_history',
                                            readonly=True)

    @api.depends('product_id')
    def _compute_previous_order_history(self):
        for order in self:
            if self.is_sale:
                order.sale_order_lines |= self.env['sale.order'].order_line.search(
                    [('product_id', '=', self.product_id.id), ('state', '=', 'sale')], limit=5)
                order.purchase_order_lines = []
            elif self.is_purchase:
                order.purchase_order_lines |= self.env['purchase.order'].order_line.search(
                    [('product_id', '=', self.product_id.id), ('state', '=', 'purchase')], limit=5)
                order.sale_order_lines = []
