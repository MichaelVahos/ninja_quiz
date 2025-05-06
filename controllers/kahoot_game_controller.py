from odoo import http
from odoo.http import request

class KahootGameController(http.Controller):

    @http.route('/kahoot/start/<int:survey_id>', type='http', auth='user', website=True)
    def start_kahoot_game(self, survey_id, **kwargs):
        survey = request.env['survey.survey'].browse(survey_id)
        if not survey.exists():
            return request.not_found()

        questions = request.env['survey.question'].search([('survey_id', '=', survey.id)])

        return request.render('ninja_quiz.kahoot_game_template', {
            'survey': survey,
            'questions': questions,
        })
