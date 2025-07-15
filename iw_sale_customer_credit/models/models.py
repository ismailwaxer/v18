from odoo import models, fields, api

class SaleCustomerCreditLimit(models.Model):
    _inherit = 'sale.order'

    partner_credit_limit = fields.Monetary(
        string="Customer Total Receivable",
        related='partner_id.credit',
        store=True,
        readonly=True,
        currency_field='currency_id',
    )
    partner_total_due = fields.Float(
        string="Days Sales Outstanding (DSO)",
        related='partner_id.days_sales_outstanding',
        store=True,
        readonly=True,
    )

    partner_available_credit = fields.Float(
        string="Available Credit",
        compute='_compute_partner_available_credit',
        store=False,  # because it's not a related field anymore
        readonly=True,
    )

    @api.depends('partner_id.credit_limit')
    def _compute_partner_available_credit(self):
        for rec in self:
            credit_limit = rec.partner_id.credit_limit
            if isinstance(credit_limit, dict):
                # Change 'amount' to whatever key you actually need from the JSON
                rec.partner_available_credit = credit_limit.get('amount', 0.0)
            else:
                rec.partner_available_credit = credit_limit or 0.0

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_qty_available = fields.Float(
        string="QOH",
        related='product_id.qty_available',
        store=True,
        readonly=True,
    )
