from odoo import models, fields, api

class HotelBooking(models.Model):
    _name = "hotel.booking"
    _description = "Hotel Booking"

    customer_name = fields.Char(string="Customer Name")
    customer_id = fields.Many2one("res.partner", string="Customer")
    room_id = fields.Many2one("hotel.room", string="Room")

    check_in = fields.Date(string="Check-in")
    check_out = fields.Date(string="Check-out")

    total_price = fields.Float(string="Total Price", compute="_compute_total_price", store=True)

    @api.depends('room_id', 'check_in', 'check_out')
    def _compute_total_price(self):
        for rec in self:
            if rec.room_id and rec.check_in and rec.check_out:
                days = (rec.check_out - rec.check_in).days
                rec.total_price = rec.room_id.price * days if days > 0 else 0.0
            else:
                rec.total_price = 0.0
