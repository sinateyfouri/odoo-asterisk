{
    'name': 'Asiapardaz VoIP Integration',
    'version': '1.0',
    'summary': 'Integration with Asterisk PBX through Asiapardaz VoIP',
    'category': 'Tools',
    'author': 'Sina Teyfouri',
    'website': 'https://asiapardaz.ir',
    'depends': ['base', 'web', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_users_views.xml',
        'views/res_config_settings_views.xml',
        'views/res_partner_views.xml',
        'views/asiapardaz_voip_assets.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'asiapardaz_voip/static/src/js/asia_call.js',
        ],
    },
    'installable': True,
    'application': True,
}