from odoo import models, fields, api

class SurveyUserInput(models.Model):
    _inherit = 'survey.user_input'

    @api.model
    def get_current_question_and_answers(self, survey_id, input_id):
        input_record = self.browse(input_id).sudo()
        question = input_record._get_next_question()

        if not question:
            return {'completed': True}

        return {
            'completed': False,
            'question': {
                'id': question.id,
                'title': question.title,
            },
            'answers': [{'id': ans.id, 'value': ans.value} for ans in question.suggested_answer_ids],
        }

    @api.model
    def submit_answer(self, input_id, question_id, answer_id):
        input_record = self.browse(input_id).sudo()
        input_record._save_lines({str(question_id): answer_id})
        return {'status': 'ok'}
