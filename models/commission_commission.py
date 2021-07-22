# -*- coding: utf-8 -*-

from odoo import fields, models


class CommissionCommission(models.Model):
	_name = "commission.commission"

	name = fields.Char(
		string="Tipo de comision",
		required=True
	)
	cost_commission = fields.Float(
		string="Costo",
		required=True
	)