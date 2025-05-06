from odoo import models, fields

class NinjaQuiz(models.Model):
    _inherit = 'survey.survey'

    modo_juego = fields.Selection([
        ('individual', 'Individual'),
        ('equipos', 'Por Equipos')
    ], string='Modo de juego', default='individual')

    tiempo_por_pregunta = fields.Integer(string='Tiempo por pregunta (segundos)', default=30)

    color_tema = fields.Char(string='Color del tema', help='Color en formato HEX, como #ff0000')

