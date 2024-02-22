from odoo import models, fields

class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    order_date = fields.Datetime(related='order_id.date_order', string="Order Date", store=True)
