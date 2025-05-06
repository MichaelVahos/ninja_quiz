from odoo import models, fields

class Survey(models.Model):
    _inherit = 'survey.survey'

    modo_juego = fields.Selection([
        ('individual', 'Individual'),
        ('equipos', 'Por equipos'),
        ('clasico', 'Clásico'),
        ('equipo', 'Por equipos'),
    ], string='Modo de juego')

    tiempo_por_pregunta = fields.Integer(string='Tiempo por pregunta (segundos)', default=30)
    color_tema = fields.Char(string='Color del tema (hex)', default='#0000FF')

    def action_start_kahoot_game(self):
        return {
            'type': 'ir.actions.act_url',
            'name': 'Ninja Quiz',
            'url': f'/kahoot/start/{self.id}',
            'target': 'self',
        }
