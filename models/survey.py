from odoo import models, fields

class Survey(models.Model):
    _inherit = 'survey.survey'

    current_question_id = fields.Many2one(
        comodel_name='survey.question',
        string='Pregunta activa',
    )
