# -*- coding: utf-8 -*-

from odoo import fields, models


class H2O(models.Model):
	_name = "h2o.h2o"

	travel_cost_id = fields.Many2one(
		"travel.cost",
		string="Costos adicionales",
		help="Seleccione si el viaje requiere costo adicional"
	)
	sale_order_ids = fields.One2many(
		"sale.order",
		"h2o_id",
		string="Ventas"
	)