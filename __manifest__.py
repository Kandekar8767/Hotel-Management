{
    'name': 'Hotel Room Booking',
    'version': '1.0.0',
    'author': 'Pratik',
    'category': 'Services',
    'summary': 'Simple hotel room booking management',
    'depends': ['base', 'website'],
    'data': [
        'security/ir.model.access.csv',
        'views/hotel_room_views.xml',       # <-- must load actions/views first
        'views/hotel_booking_views.xml',
        'views/hotel_menu.xml',             # <-- menus last (needs actions to exist)
        'views/website_templates.xml',
    ],
    'installable': True,
    'application': True,
}
