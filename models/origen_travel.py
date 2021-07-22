# -*- coding: utf-8 -*-

from odoo import fields, models


class OrigenTravel(models.Model):
    _name = 'origen.travel'

    name = fields.Char(
    	string="Nombre",
    	required=True
    )
    street_origen = fields.Char(
    	string="Direccion"
    )