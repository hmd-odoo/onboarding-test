from odoo import fields, models, api, exceptions


class SaleOrderLine(models.Model):
    _inherit="sale.order.line"

    discount_amount = fields.Monetary(compute="_compute_discount_amount", default = 0)

    @api.depends("discount", "price_total")
    def _compute_discount_amount(self):
        for record in self:
            record.discount_amount= (record.discount/100) * record.price_subtotal
            print("YOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\n")
            print(record.discount_amount)


