from odoo import models, fields

class HotelRoom(models.Model):
    _name = "hotel.room"
    _description = "Hotel Room"

    name = fields.Char(required=True)
    room_number = fields.Char(required=True)
    room_type = fields.Selection([
        ('single', 'Single'),
        ('double', 'Double'),
        ('suite', 'Suite'),
    ], required=True)
    price = fields.Float(required=True)
    is_available = fields.Boolean(default=True)
