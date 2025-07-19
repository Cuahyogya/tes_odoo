from odoo import models, fields

class Driver(models.Model):
    _name = 'driver'
    _description = "Driver"
    name = fields.Char()

    contracts_ids = fields.One2many('contracts', 'driver_id', string='contracts')