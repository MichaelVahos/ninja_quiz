from odoo import models, fields

class SurveyGameParticipant(models.Model):
    _name = 'survey.game.participant'
    _description = 'Survey Game Participant'

    name = fields.Char(string='Player Name', required=True)
    session_id = fields.Many2one('survey.game.session', string='Game Session', required=True, ondelete='cascade')
    score = fields.Integer(string='Score', default=0)
