# -*- coding: utf-8 -*-

from odoo import fields, models, api

class SaleOrder(models.Model):
	_inherit = "sale.order"

	h2o_id = fields.Many2one(
		"h2o.h2o", 
		string="H2O"
	)
	driver_id = fields.Many2one(
		"res.partner",
		string="Chofer", 
		help="Seleccione nombre del chofer",
		domain=[
			('is_driver', '=', True)
		]
	)
	vehicle_id = fields.Many2one(
		"fleet.vehicle",
		string="Unidad",
		help="Seleccione unidad"
	)
	folio = fields.Char(string="Folio")
	date_travel = fields.Date(string="Fecha del viaje")
	customer_id = fields.Many2one(
		"res.partner", 
		string="Cliente"
	)
	origen_travel_id = fields.Many2one(
		"origen.travel", 
		string="Origen del viaje"
	)
	street_name = fields.Many2one(
		"res.partner", 
		string="Destino del viaje"
	)
	sale_status = fields.Selection(
		[
			("waiting", "En espera"),
			("started", "Iniciado"),
			("finished", "Terminado")
		], 
		string="Estado",
		default=False
	)

	def waiting_progressbar(self):
		self.sale_status = "waiting"

	def started_progressbar(self):
		self.sale_status = "started"

	def done_progressbar(self):
		self.sale_status = "finished"

	@api.model
	def create(self, vals):
		vals["folio"] = self.env["ir.sequence"].next_by_code("folio.sequence")
		result = super(SaleOrder, self).create(vals)
		return result

	travel_status = fields.Selection(
		[
			("started", "Iniciado"),
			("finished", "Terminado"),
			("canceled", "Cancelado")
		], 
		string="Estado",
		default=False
	)

	def started_travel_progressbar(self):
		self.travel_status = "started"

	def completed_travel_progressbar(self):
		self.travel_status = "finished"

	def canceled_travel_progressbar(self):
		self.travel_status = "canceled"

	