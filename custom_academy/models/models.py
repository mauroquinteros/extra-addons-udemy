# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class custom_academy(models.Model):
#     _name = 'custom_academy.custom_academy'
#     _description = 'custom_academy.custom_academy'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
