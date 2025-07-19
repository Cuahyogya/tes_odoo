from odoo import models, fields

class Vehicles(models.Model):
    _name = 'od_rental_management.vehicles'
    _description = 'Vehicles'

    name = fields.Char(string='Name')
    date = fields.Date('date')
    state = fields.Selection([
        ('available', 'Available'),
        ('unavailable', 'Unavailable'),
        ('under maintenance', 'Under maintenance')
    ], string='State')
    license_plate = fields.Char(string='License Plate')
    start_date = fields.Datetime("Start Date", required=True)
