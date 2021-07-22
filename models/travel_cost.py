# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TravelCost(models.Model):
	_name = 'travel.cost'

	name = fields.Char(
		string="Nombre",
		required=True
	)
	code = fields.Char(string="Código")