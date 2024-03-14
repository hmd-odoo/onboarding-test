from odoo import fields, models, api, exceptions


class AccountMoveLine(models.Model):
    _inherit="account.move.line"

    discount_amount = fields.Monetary(compute="_compute_discount_amount", default = 0)

    @api.depends("discount", "price_total")
    def _compute_discount_amount(self):
        for record in self:
            record.discount_amount= (record.discount/100) * record.price_subtotal
            print("YOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO\n")
            print(record.discount_amount)

#c
#c
#If you want to invoice based on ordered quantities instead:
#    • For consumable or storable products, open the product, go to the 'General Information' tab and change the 'Invoicing Policy' from 'Delivered Quantities' to 'Ordered Quantities'.
#    • For services (and other products), change the 'Invoicing Policy' to 'Prepaid/Fixed Price'.