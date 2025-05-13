from odoo import models, fields, api

class SurveyGameSession(models.Model):
    _name = 'survey.game.session'
    _description = 'Game Session'

    name = fields.Char(string='Nombre de la sesión', required=True)
    survey_id = fields.Many2one('survey.survey', string='Encuesta', required=True)
    participant_ids = fields.One2many('survey.game.participant', 'session_id', string='Participantes')

    state = fields.Selection([
        ('draft', 'Borrador'),
        ('started', 'Iniciado'),
        ('finished', 'Finalizado'),
    ], string='Estado', default='draft')

    current_question_id = fields.Many2one('survey.question', string='Pregunta actual')

    @api.model
    def create_from_survey(self, survey_id):
        survey = self.env['survey.survey'].browse(survey_id)
        session = self.create({
            'name': f"Sesión de {survey.title}",
            'survey_id': survey.id,
        })
        return {
            'type': 'ir.actions.act_window',
            'name': 'Sesión de Juego',
            'res_model': 'survey.game.session',
            'view_mode': 'form',
            'res_id': session.id,
            'target': 'current',
        }

    def action_start_game(self):
        """Inicia el juego con la primera pregunta"""
        for session in self:
            first_question = session.survey_id.question_ids[:1]
            if first_question:
                session.write({
                    'state': 'started',
                    'current_question_id': first_question.id,
                })
