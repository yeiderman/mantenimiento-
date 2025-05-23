# -*- coding: utf-8 -*-
from odoo import models, fields, api

class MaintenanceEquipment(models.Model):
    _inherit = 'maintenance.equipment' # Heredamos del modelo de equipos de mantenimiento existente

    # Agregamos un nuevo campo, por ejemplo, "Número de Serie"
    numero_serie = fields.Char(string='Número de Serie', required=True, copy=False,
                              help="Número de serie único del equipo.")
    # Puedes añadir más campos según tus necesidades
    ultima_revision = fields.Date(string='Fecha Última Revisión')
    proxima_revision = fields.Date(string='Fecha Próxima Revisión', compute='_compute_proxima_revision', store=True)

    @api.depends('ultima_revision')
    def _compute_proxima_revision(self):
        for record in self:
            if record.ultima_revision:
                # Ejemplo: la próxima revisión es 6 meses después de la última
                from datetime import timedelta
                record.proxima_revision = record.ultima_revision + timedelta(days=180)
            else:
                record.proxima_revision = False