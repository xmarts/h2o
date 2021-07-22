# -*- coding: utf-8 -*-

from odoo import fields, models


class UnidadesUnidades(models.Model):
	_name = "unidades.unidades"

	float_id = fields.Many2one(
		"fleet.vehicle", 
		string="id"
	)
	employee_id = fields.Many2one(
		"hr.employee", 
		string="id"
	)
	float_ids = fields.One2many(
		"fleet.vehicle", 
		"id", 
		string="Unidad"
	)
	driver_id = fields.Many2one(
		"res.partner", 
		string="Chofer",
		domain=[
			('is_driver', '=', True)
		]
	)
	float_status = fields.Selection(
		[
			("available", "Disponible"), 
			("on_route", "En ruta"), 
			("filling_water", "Cargando agua"), 
			("filling_diesel", "Cargando Diesel"), 
			("canceled", "Cancelado")
		], 
		string="Estado"
	)

	def available_progressbar(self):
		self.float_status = "available"

	def on_route_progressbar(self):
		self.float_status = "on_route"

	def canceled_progressbar(self):
		self.float_status = "canceled"