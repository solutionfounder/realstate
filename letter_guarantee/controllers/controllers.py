# -*- coding: utf-8 -*-
from odoo import http

# class LetterCredit(http.Controller):
#     @http.route('/letter_credit/letter_credit/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/letter_credit/letter_credit/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('letter_credit.listing', {
#             'root': '/letter_credit/letter_credit',
#             'objects': http.request.env['letter_credit.letter_credit'].search([]),
#         })

#     @http.route('/letter_credit/letter_credit/objects/<model("letter_credit.letter_credit"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('letter_credit.object', {
#             'object': obj
#         })