from odoo import http
from odoo.http import request

class KahootGameController(http.Controller):

    @http.route('/kahoot/start/<int:survey_id>', type='http', auth='user', website=True)
    def start_kahoot_game(self, survey_id, **kwargs):
        survey = request.env['survey.survey'].browse(survey_id)
        if not survey.exists():
            return request.not_found()

        # Buscar sesión existente o crear una nueva
        session = request.env['survey.game.session'].search([
            ('survey_id', '=', survey.id),
            ('state', '=', 'started')
        ], limit=1)

        if not session:
            session = request.env['survey.game.session'].create_from_survey(survey.id)
            session_id = session.get('res_id') if isinstance(session, dict) else session.id
            session = request.env['survey.game.session'].browse(session_id)
            session.action_start_game()

        return request.render('ninja_quiz.kahoot_game_template', {
            'survey': survey,
            'question': session.current_question_id,
        })

