# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import Response
import json

class VisitController(http.Controller):

    @http.route('/api/visits', auth='public', method=['GET'], csrf=False)
    def _get_visits(self, **kwargs):
        try:
            visits = http.request.env['custom_crm.visit'].sudo().search_read([], ['id', 'name', 'customer', 'done'])
            response = json.dumps(visits, ensure_ascii=False).encode('utf-8')
            return Response(response, content_type={'application/json;charset=utf-8'}, status=200)
        except Exception as e:
            error = json.dumps({
                'error': str(e)
            })
            return Response(error, content_type={'application/json;charset=utf-8'}, status=505)
