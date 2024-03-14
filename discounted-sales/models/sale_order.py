from odoo import fields, models, api, exceptions


class SaleOrder(models.Model):
    _inherit="sale.order"

    total_discount_amount = fields.Monetary(compute="_compute_total_discount_amount", default = 0)

    @api.depends("order_line.discount_amount")
    def _compute_total_discount_amount(self):
        for record in self:
            self.total_discount_amount += record.order_line.discount_amount
