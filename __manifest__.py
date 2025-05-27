{
    'name': 'Ninja Quiz',
    'version': '1.0',
    'category': 'Tools',
    'author': 'Michael Vahos',
    'license': 'LGPL-3',
    'depends': ['website'],
    'data': [
        'views/kahoot_game_template.xml',  
        'views/survey_views.xml',          
        'data/ir_sequence.xml',            
    ],
    'assets': {
        'web.assets_frontend': [
            'ninja_quiz/static/src/components/KahootPlayer/KahootPlayer.js'
        ],
    },
    'installable': True,
    'auto_install': False,
}
