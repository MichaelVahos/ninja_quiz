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

    
    def get_game_data(self):
        survey = self.sudo()
        
        # Verificar si la encuesta existe
        if not survey:
            return {'error': 'Encuesta no encontrada'}

        # Obtener la primera pregunta de la encuesta
        question = survey.survey_question_ids[:1]  # Solo la primera pregunta
        answers = [{'id': ans.id, 'value': ans.value} for ans in question.survey_answer_ids]
        
        return {
            'survey': {
                'title': survey.title,
            },
            'question': {
                'title': question.title,
                'answers': answers,
            }
        }
