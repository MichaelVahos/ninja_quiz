from odoo import models, fields, api

class SurveySurvey(models.Model):
    _inherit = 'survey.survey'

    modo_juego = fields.Selection([
        ('individual', 'Individual'),
        ('equipos', 'Por Equipos'),
    ], string="Modo de Juego", default='individual')

    tiempo_por_pregunta = fields.Integer(string="Tiempo por pregunta (segundos)", default=30)
    color_tema = fields.Char(string="Color del tema", default="#00c3ff")

    def action_start_kahoot_game(self):
        # Aquí puedo agregar la lógica real para iniciar el modo Kahoot
        return {
            'type': 'ir.actions.act_window',
            'name': 'Kahoot Game Started',
            'res_model': 'survey.survey',
            'view_mode': 'form',
            'res_id': self.id,
            'target': 'current',
        }
