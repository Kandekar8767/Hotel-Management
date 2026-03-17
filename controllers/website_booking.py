from odoo import http
from odoo.http import request

class WebsiteBooking(http.Controller):

    @http.route('/hotel/booking', type='http', auth='public', website=True)
    def hotel_booking_page(self):
        rooms = request.env['hotel.room'].sudo().search([])
        return request.render('hotel_room_booking.hotel_booking_page', {
            'rooms': rooms,
        })

    @http.route('/hotel/booking/submit', type='http', auth='public', website=True, csrf=False)
    def hotel_booking_submit(self, **kwargs):
        request.env['hotel.booking'].sudo().create({
            'customer_name': kwargs.get('customer_name'),
            'room_id': int(kwargs.get('room_id')),
            'check_in': kwargs.get('check_in'),
            'check_out': kwargs.get('check_out'),
        })

        return request.render('hotel_room_booking.hotel_booking_thanks')
