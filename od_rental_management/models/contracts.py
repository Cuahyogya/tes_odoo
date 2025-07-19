from odoo import models, fields

class Contracts(models.Model):
    _name = 'contracts'
    _description = "Contracts"

    name = fields.Char(string="Contract Name")
    driver_id = fields.Many2one('driver', string='Driver')
    vehicle_id = fields.Many2one('od_rental_management.vehicles', string='Vehicle')
    document_ids = fields.One2many('contract.document', 'contract_id', string='Documents')


class ContractDocument(models.Model):
    _name = 'contract.document'
    _description = 'Contract Document'

    name = fields.Char(string='Document Name')
    file = fields.Binary(string='File')
    file_name = fields.Char(string='Filename')
    contract_id = fields.Many2one('contracts', string='Contract')
