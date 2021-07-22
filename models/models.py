# -*- coding: utf-8 -*-

from odoo import models, fields, api

class LessMinimalModel(models.Model):
    _name = 'custom_addon.custom_addon'

    name = fields.Char('Nombre del campo')


# class custom_addon(models.Model):
#     _name = 'custom_addon.custom_addon'
#     _description = 'custom_addon.custom_addon'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
