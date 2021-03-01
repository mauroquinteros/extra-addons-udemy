# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class Visit(models.Model):
    _name = 'custom_crm.visit'
    _description = 'Visit Model'

    name = fields.Char(string='Descripción')
    customer = fields.Many2one(string='Cliente', comodel_name='res.partner')
    date = fields.Datetime(string='Fecha')
    type = fields.Selection([('P', 'Presencial'), ('W', 'WhatsApp'), ('T', 'Teléfono')], string='Tipo de visita', required=True)
    done = fields.Boolean(string='Realizada', readonly=True)
    image = fields.Binary(string="Imagen")

    def toggle_state(self):
        self.done = not self.done

    def f_create(self):
        visit = {
            'name': 'ORM Test',
            'customer': 1,
            'date': datetime.date(2021, 3, 15),
            'type': 'T',
            'done': False,
        }
        print(visit)
        self.env['custom_crm.visit'].create(visit)

    def f_search_update(self):
        visitname = self.name

        visit_a = self.env['custom_crm.visit'].search([('name', '=', self.name)])
        print('search()', visit_a, visit_a.name)

        visit_b = self.env['custom_crm.visit'].browse(1)
        print('browse()', visit_b, visit_b.name)

        visit_b.write({
            'name': 'ORM Test Write'
        })

    def f_delete(self):
        pass
        print(self.name)
        print(self)
        visit = self.env['custom_crm.visit'].search([('name', '=', self.name)])
        visit.unlink()


class VisitReport(models.AbstractModel):
    _name = 'report.custom_crm.report_visit_card'

    @api.model
    def _get_report_values(self, docIds, data: None):
        report_obj = self.env['ir.actions.report']
        # report = report_obj._get_report_from_name('custom_crm.report_visit_card')
        return {
            'doc_ids': docIds,
            'doc_model': self.env['custom_crm.visit'],
            'docs': self.env['custom_crm.visit'].browse(docIds)
        }
