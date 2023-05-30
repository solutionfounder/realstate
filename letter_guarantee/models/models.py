from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError

class LetterCreditType(models.Model):
    _name = 'letter.guarantee.type'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Letter Of Guarantee Type'

    name = fields.Char()
    lc_journal = fields.Many2one("account.journal", string="LOG Journal", required=True)
    lc_bank_journal = fields.Many2one("account.journal", string="Bank Journal", required=True)
    bank_fees = fields.Float("Bank Fees (%)")
    bank_expense_account = fields.Many2one("account.account", string="Bank Expense Account", required=True)
    intermediate_account = fields.Many2one("account.account", string="Intermediate Account", required=True)
    bank_account_number = fields.Char("Bank Account Number")
    bank_fees_from_lc = fields.Boolean("Bank Fees From LOG")
    type = fields.Selection(
        [('advance_payment', 'Advance Payment'), ('business_insurance', 'Business Insurance'),
         ('final_insurance', 'Final Insurance')])
    log_cover_percentage = fields.Float("LOG Cover Percentage")
    state = fields.Selection([('draft', 'Draft'), ('active', 'Active'), ('archived', 'Archived')], string='Status',
                             default='draft')

    def activate_action(self):
        self.state = 'active'


class LCAmountExtend(models.Model):
    _name = 'lc.amount.extend'

    name = fields.Char("Description")
    amount = fields.Float("Amount")
    lc_seq = fields.Char("LOG Sequence")


class LCPeriodExtend(models.Model):
    _name = 'lc.period.extend'

    name = fields.Char("Description")
    date = fields.Datetime("Expiration Date")
    lc_seq = fields.Char("LOG Sequence")


class JournalEntriesInherit(models.Model):
    _inherit = 'account.move'

    lc_seq = fields.Char("LOG Sequence")


class LetterCredit(models.Model):
    _name = 'letter.guarantee'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Letter Of Guarantee'

    name = fields.Char(string='Name', required=True, copy=False, readonly=True, index=True,
                       default=lambda self: _('New'))
    partner_id = fields.Many2one("res.partner", string="Customer", required=True)
    lc_type = fields.Many2one("letter.guarantee.type", string="LOG Type", required=True)
    log_amount = fields.Float("LOG Amount", required=True)
    lc_amount = fields.Float("LOG Cover Amount", readonly=True)
    lc_remaining_amount = fields.Float("LOG Cover Remaining Amount", readonly=True)
    log_remaining_amount = fields.Float("LOG Remaining Amount", readonly=True)
    currency_id = fields.Many2one("res.currency", string="Currency", required=True)
    curr_rate = fields.Float("Currency Rate", required=True)
    sale_order = fields.Many2one("sale.order", string="Sale Order")
    date = fields.Datetime("Date")
    expiration_date = fields.Datetime("Expiration Date")
    delivery_date = fields.Datetime("Delivery Date")
    lc_number = fields.Char("LOG Bank Number")
    project_percentage = fields.Float("Percentage Of The Project")
    account_move_count = fields.Integer(compute='compute_count')
    amount_extend_count = fields.Integer(compute='compute_count')
    period_extend_count = fields.Integer(compute='compute_count')
    state = fields.Selection([('draft', 'Draft'), ('open', 'Open'), ('close', 'Close'),
                              ('cancel', 'Cancel')],
