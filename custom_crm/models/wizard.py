# -*- coding: utf-8 -*-

from odoo import models, fields, api


class VisitWizard(models.TransientModel):
    _name = 'custom_crm.visit.wizard'

    visit_id = fields.Many2one(string='Visita', comodel_name='custom_crm.visit')
    appointment_date = fields.Date(string='Cita de la visita')

    def create_appointment(self):
        print(self)
