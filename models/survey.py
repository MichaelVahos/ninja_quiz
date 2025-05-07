from odoo import models, fields, api

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
        self.ensure_one()
        session = self.env['survey.game.session'].create({
            'name': f'Sesión de {self.title}',
            'survey_id': self.id,
        })
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sesión de Juego',
            'res_model': 'survey.game.session',
            'view_mode': 'form',
            'res_id': session.id,
            'target': 'current',
        }
