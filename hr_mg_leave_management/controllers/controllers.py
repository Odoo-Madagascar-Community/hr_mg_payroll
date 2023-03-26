# -*- coding: utf-8 -*-
# from odoo import http


# class HrMgLeaveManagement(http.Controller):
#     @http.route('/hr_mg_leave_management/hr_mg_leave_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_mg_leave_management/hr_mg_leave_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_mg_leave_management.listing', {
#             'root': '/hr_mg_leave_management/hr_mg_leave_management',
#             'objects': http.request.env['hr_mg_leave_management.hr_mg_leave_management'].search([]),
#         })

#     @http.route('/hr_mg_leave_management/hr_mg_leave_management/objects/<model("hr_mg_leave_management.hr_mg_leave_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_mg_leave_management.object', {
#             'object': obj
#         })
