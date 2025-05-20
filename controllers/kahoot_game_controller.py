from odoo import http
from odoo.http import request

class KahootGameController(http.Controller):

    @http.route('/kahoot', type='http', auth='public', website=True)
    def kahoot_participant(self, **kwargs):
        _logger.info("===== Entró al controlador /kahoot =====")
        
        # Busca la primera encuesta en la base de datos
        survey = request.env['survey.survey'].sudo().search([], limit=1)
        
        if not survey:
            _logger.error("No se encontró ninguna encuesta disponible")
            return request.render('theme_ninja_quiz.error_template', {})
        
        # Crea una nueva entrada de usuario para la encuesta
        user_input = request.env['survey.user_input'].sudo().create({
            'survey_id': survey.id,
            'partner_id': request.env.user.partner_id.id,
            'state': 'new',
        })
        
        return request.render('theme_ninja_quiz.kahoot_page', {
            'survey_id': survey.id,
            'input_id': user_input.id,
        })

    @http.route('/kahoot/game/data/<int:survey_id>', type='json', auth='public')
    def kahoot_game_data(self, survey_id, **kwargs):
        survey = request.env['survey.survey'].sudo().browse(survey_id)
        
        # Verificar si la encuesta existe
        if not survey:
            return {'error': 'Encuesta no encontrada'}
        
        # Obtener la primera pregunta de la encuesta
        question = survey.survey_question_ids[:1]  # Solo la primera pregunta
        answers = [{'id': ans.id, 'value': ans.value} for ans in question.survey_answer_ids]
        
        return {
            'survey': {
                'title': survey.title,
            },
            'question': {
                'title': question.title,
                'answers': answers,
            }
        }
