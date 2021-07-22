# -*- coding: utf-8 -*-
# from odoo import http


# class CustomAddon(http.Controller):
#     @http.route('/custom_addon/custom_addon/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_addon/custom_addon/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_addon.listing', {
#             'root': '/custom_addon/custom_addon',
#             'objects': http.request.env['custom_addon.custom_addon'].search([]),
#         })

#     @http.route('/custom_addon/custom_addon/objects/<model("custom_addon.custom_addon"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_addon.object', {
#             'object': obj
#         })
