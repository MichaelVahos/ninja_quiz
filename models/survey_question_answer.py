from odoo import models, fields

class SurveyQuestionAnswer(models.Model):
    _inherit = 'survey.question.answer'

    is_correct = fields.Boolean(string='¿Es la respuesta correcta?', default=False)
