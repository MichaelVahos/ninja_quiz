from odoo import models, fields

class SurveyGameParticipantAnswer(models.Model):
    _name = 'survey.game.participant.answer'
    _description = 'Respuesta del Participante'

    participant_id = fields.Many2one('survey.game.participant', required=True)
    question_id = fields.Many2one('survey.question', required=True)
    answer_id = fields.Many2one('survey.question.answer', required=True)
    answered_at = fields.Datetime(string="Fecha de Respuesta", default=fields.Datetime.now)
