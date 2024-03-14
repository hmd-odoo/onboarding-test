from odoo import fields, models, api, exceptions


class AccountMove(models.Model):
    _inherit="account.move"


    total_discount_amount = fields.Monetary(compute="_compute_total_discount_amount", default = 0)

    @api.depends("amount_total")
    def _compute_total_discount_amount(self):
        for record in self:
            self.total_discount_amount += line.discount_amount
        print("NOOOOOOOOOOOOOOOOO")
        print(self.total_discount_amount)
