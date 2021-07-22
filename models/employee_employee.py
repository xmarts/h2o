# -*- coding: utf-8 -*-

from odoo import fields, models


class Employee(models.Model):
	_name = "employee.employee"

	id_employee = fields.Char(
		string="Numero de Identificacion"
	)
	name = fields.Char(
		string="Nombre"
	)