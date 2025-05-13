from odoo import models, fields, api  

class SurveyGameAnswer(models.Model):
    _name = 'survey.game.answer'
    _description = 'Respuesta del Jugador en el Juego'

    participant_id = fields.Many2one('survey.game.participant', string='Participante', required=True)
    question_id = fields.Many2one('survey.question', string='Pregunta', required=True)
    answer_id = fields.Many2one('survey.question.answer', string='Respuesta elegida', required=True)
    is_correct = fields.Boolean(string='¿Es correcta?', compute='_compute_is_correct', store=True)

    @api.depends('answer_id')  
    def _compute_is_correct(self):
        for record in self:
            record.is_correct = record.answer_id.is_correct if record.answer_id else False

