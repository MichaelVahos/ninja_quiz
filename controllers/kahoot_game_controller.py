from odoo import http
from odoo.http import request

class KahootGameController(http.Controller):

    # Ruta para iniciar el juego
    @http.route('/kahoot/start/<int:survey_id>', type='http', auth='user', website=True)
    def start_kahoot_game(self, survey_id, **kwargs):
        survey = request.env['survey.survey'].browse(survey_id)
        if not survey.exists():
            return request.not_found()

        # Buscar sesión activa o crear una
        session = request.env['survey.game.session'].search([
            ('survey_id', '=', survey.id),
            ('state', '=', 'started')
        ], limit=1)

        if not session:
            session_data = request.env['survey.game.session'].create_from_survey(survey.id)
            session = request.env['survey.game.session'].browse(session_data['res_id'])
            session.action_start_game()

        return request.render('ninja_quiz.kahoot_game_template', {
            'survey': survey,
            'question': session.current_question_id,
            'answers': session.current_question_id.suggested_answer_ids,
        })

    # Ruta para procesar la respuesta
    @http.route('/kahoot/answer', type='http', auth='user', website=True, methods=['POST'])
    def submit_answer(self, **post):
        question_id = int(post.get('question_id', 0))
        answer_id = int(post.get('answer_id', 0))
        survey_id = int(post.get('survey_id', 0))

        user = request.env.user

        # Obtener la sesión activa del usuario
        session = request.env['survey.game.session'].search([
            ('survey_id', '=', survey_id),
            ('state', '=', 'started')
        ], limit=1)

        if not session:
            return request.redirect('/kahoot/start/%d' % survey_id)

        # Obtener participante (por ahora asociado al usuario actual)
        participant = request.env['survey.game.participant'].search([
            ('session_id', '=', session.id),
            ('name', '=', user.name)
        ], limit=1)

        if not participant:
            participant = request.env['survey.game.participant'].create({
                'name': user.name,
                'session_id': session.id,
            })

        # Verificar si la respuesta es correcta
        answer = request.env['survey.question.answer'].browse(answer_id)
        correct = answer.is_correct if answer else False

        if correct:
            participant.score += 100  # Sumar puntaje si es correcta

        return request.render('ninja_quiz.kahoot_answer_feedback', {
            'correct': correct,
            'score': participant.score,
            'survey_id': survey_id,
        })
