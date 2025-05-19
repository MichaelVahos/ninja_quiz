{
    'name': 'Ninja Quiz',
    'version': '1.0',
    'author': 'Michael Vahos',
    'category': 'Tools',
    'summary': 'Quiz interactivo tipo Kahoot integrado con encuestas',
    'license': 'LGPL-3',
    'depends': ['survey', 'website'],
    'data': [
        'security/menu_access.xml',
        'data/ir_sequence.xml',
        'views/survey_views.xml',
        'views/kahoot_game_template.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/ninja_quiz/static/src/components/KahootPlayer/KahootPlayer.js',
        ],
    },
    'qweb': [
        'static/src/components/KahootPlayer/KahootPlayer.xml',
    ],
    'installable': True,
    'auto_install': False,
}
