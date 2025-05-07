from odoo import models, fields

class SurveyGameParticipant(models.Model):
    _name = 'survey.game.participant'
    _description = 'Game Participant'
    _order = 'create_date desc'

    name = fields.Char(string='Nombre del participante', required=True)
    session_id = fields.Many2one(
        'survey.game.session',
        string='Sesión de juego',
        required=True,
        ondelete='cascade'
    )
    survey_id = fields.Many2one(
        related='session_id.survey_id',
        string='Encuesta',
        store=True,
        readonly=True
    )
    score = fields.Integer(string='Puntaje', default=0)
    is_host = fields.Boolean(string='Es anfitrión', default=False)
