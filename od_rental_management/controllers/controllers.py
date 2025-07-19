# -*- coding: utf-8 -*-
# from odoo import http


# class OdRentalManagement(http.Controller):
#     @http.route('/od_rental_management/od_rental_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/od_rental_management/od_rental_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('od_rental_management.listing', {
#             'root': '/od_rental_management/od_rental_management',
#             'objects': http.request.env['od_rental_management.od_rental_management'].search([]),
#         })

#     @http.route('/od_rental_management/od_rental_management/objects/<model("od_rental_management.od_rental_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('od_rental_management.object', {
#             'object': obj
#         })

