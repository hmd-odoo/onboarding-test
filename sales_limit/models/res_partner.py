from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    sale_order_ids = fields.One2many("sale.order", "partner_id", string="Partner Sale Orders")

    sale_order_limit = fields.Float(default= 10000)
    sale_order_limit_used = fields.Float(compute = '_compute_sale_order_limit_used')

    @api.depends('sale_order_ids','sale_order_limit')
    def _compute_sale_order_limit_used(self):
        sale_records = self.env['sale.order'].read_group(
                [('partner_id','in',self.ids),('invoice_status','!=','invoiced')],
                ['partner_id','amount_total:sum'],
                ['partner_id']
            )
        sale_records_partner = {partner['partner_id'][0]:partner['amount_total'] for partner in sale_records}
        for record in self:
            print(record.sale_order_limit_used)
            record.sale_order_limit_used = record.sale_order_limit - sale_records_partner.get(record.id ,0)