{
    'name': "Auto Fill (Date or DateTime) Field Value",
    'version': '17.0',
    "summary": """  
        The 'Auto Fill (Date or DateTime) Field Value' is module for Odoo 17 
        With custom js code for fields types (Date & DateTime) 
        When Click on any field of types (Date or DateTime) it will add Current (Date or DateTime) value.
    """,
    'author': "Abanob Ashraf",
    'website': "http://zadsolutions.com",
    'category': 'Tools',
    'depends': ['base', 'base_setup'],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'auto_fill_field_date_or_datetime/static/src/js/auto_fill_field.js',
        ],
    },
    "auto_install": False,
    "installable": True,
}
