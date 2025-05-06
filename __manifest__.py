{
    'name': 'Ninja Quiz',
    'version': '1.0',
    'summary': 'Clon de Kahoot con Odoo Surveys',
    'description': 'Permite crear quizzes interactivos como Kahoot.',
    'author': 'Michael Vahos',
    'depends': ['survey'],
    'data': [
      'views/survey_views.xml',
],
    'installable': True,
    'application': True,
}
