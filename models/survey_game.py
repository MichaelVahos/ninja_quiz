from odoo import models, fields, api

class SurveyGameSession(models.Model):
    _name = 'survey.game.session'
    _description = 'Survey Game Session'

    name = fields.Char(string='Game Code', required=True, copy=False, default=lambda self: self._generate_game_code())
    survey_id = fields.Many2one('survey.survey', string='Survey', required=True)
    state = fields.Selection([
        ('waiting', 'Waiting for Players'),
        ('in_progress', 'In Progress'),
        ('finished', 'Finished')
    ], default='waiting')
    participant_ids = fields.One2many('survey.game.participant', 'session_id', string='Participants')
    current_question_id = fields.Many2one('survey.question', string='Current Question') 

    @api.model
    def _generate_game_code(self):
        return self.env['ir.sequence'].next_by_code('survey.game.session') or 'G0001'

    def action_start_game(self):
        for session in self:
            first_question = session.survey_id.question_ids[:1]
            if first_question:
                session.current_question_id = first_question
                session.state = 'in_progress'
