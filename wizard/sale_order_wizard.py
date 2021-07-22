# -*- coding: utf-8 -*-

from odoo import fields, models, api

class SaleOrderWizard(models.TransientModel):
	_name = "sale.order.wizard"
	_description = "Sale Order Wizard"

	details = fields.Text(string="Detalles", required=True)

	def canceled_travel(self):
		self.env['sale.order'].canceled_travel_progressbar()