# -*- coding: utf-8 -*-
from odoo import models, fields, api, _

class AccountMove(models.Model):
	_inherit = 'account.move'

	transfer_id = fields.Many2one('account.direct.transfer', string="Transfer")

class account_journal(models.Model):
    _inherit = "account.journal"

    def open_action_lc_direct_transfer(self):
    	return {
            'name': _('Direct Transfer'),
            'view_type': 'form',
            'view_mode': 'tree,form',
            'res_model': 'account.direct.transfer',
            'view_id': False,
            'type': 'ir.actions.act_window',
        }