# -*- coding: utf-8 -*-
from datetime import datetime
from email.policy import default
from odoo import models, fields, api


class Registro(models.Model):
    _name = 'diario_empresarial.registro'
    _description = 'Registro'

    name = fields.Many2one('res.users',String='Name',required=True)
    description = fields.Text(String='Descriptionn')
    date=fields.Date(String='Date',default=lambda *a:datetime.now().strftime('%Y-%m-%d'))
