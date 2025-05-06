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

    @api.model
    def _generate_game_code(self):
        return self.env['ir.sequence'].next_by_code('survey.game.session') or 'G0001'

