from odoo import api, fields, models
    
class OrderLineProductHistory(models.TransientModel):
    _name = "order.line.history"
    
    product_id = fields.Many2one('product.product', string='Product')       # Many lines to one product,   to fetch the products list from produc.product
    last_sale_order_line_ids = fields.Many2many('sale.order.line', string="Sale Order Lines", compute='_compute_order_lines')
    last_purchase_order_line_ids = fields.Many2many('purchase.order.line', string="Purchase Order Lines", compute='_compute_order_lines')
    
    @api.depends('product_id')
    def _compute_order_lines(self, line_count = 5):
        for record in self:
            if self.env.context.get('active_model') == 'sale.order':
                last_sale_lines = self.env['sale.order.line'].search([('state', '=', 'sale'), ('product_id', '=', self.product_id.id)], limit=line_count)
                record.last_sale_order_line_ids = last_sale_lines.ids
                record.last_purchase_order_line_ids = False

                
            elif self.env.context.get('active_model') == 'purchase.order':
                last_purchase_lines = self.env['purchase.order.line'].search([ ('product_id', '=', self.product_id.id)], limit=line_count)
                record.last_purchase_order_line_ids = last_purchase_lines.ids
                record.last_sale_order_line_ids = False
        return True