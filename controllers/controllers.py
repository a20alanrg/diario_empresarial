# -*- coding: utf-8 -*-
# from odoo import http


# class DiarioEmpresarial(http.Controller):
#     @http.route('/diario_empresarial/diario_empresarial/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/diario_empresarial/diario_empresarial/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('diario_empresarial.listing', {
#             'root': '/diario_empresarial/diario_empresarial',
#             'objects': http.request.env['diario_empresarial.diario_empresarial'].search([]),
#         })

#     @http.route('/diario_empresarial/diario_empresarial/objects/<model("diario_empresarial.diario_empresarial"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('diario_empresarial.object', {
#             'object': obj
#         })
