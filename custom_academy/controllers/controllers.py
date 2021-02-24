# -*- coding: utf-8 -*-
# from odoo import http


# class CustomAcademy(http.Controller):
#     @http.route('/custom_academy/custom_academy/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_academy/custom_academy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_academy.listing', {
#             'root': '/custom_academy/custom_academy',
#             'objects': http.request.env['custom_academy.custom_academy'].search([]),
#         })

#     @http.route('/custom_academy/custom_academy/objects/<model("custom_academy.custom_academy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_academy.object', {
#             'object': obj
#         })
