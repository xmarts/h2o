# -*- coding: utf-8 -*-

from datetime import datetime
from odoo import fields, models, api


class PaymentDriver(models.Model):
	_name = "payment.driver"

	driver_id = fields.Many2one(
		"res.partner",
		string="Chofer",
		help="Seleccione nombre del chofer",
		domain=[
			('is_driver', '=', True)
		]
	)

	salary_driver = fields.Float(string="Sueldo base")
	commission_id = fields.Many2one(
		"commission.commission",
		string="Comisiones extra"
	)
	commission_travel = fields.Float(
		string="Comision por viaje",
		compute="_get_total_trips_per_day"
	)