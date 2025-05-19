import { Component, onWillStart, useState } from "@odoo/owl";
import { jsonrpc } from "@web/core/network/rpc_service";

export class KahootPlayer extends Component {
    static template = "ninja_quiz.KahootPlayer";

    setup() {
        this.state = useState({
            question: null,
            answers: [],
            completed: false,
            loading: true,
        });

        onWillStart(async () => {
            const inputId = parseInt(this.props.inputId);
            const surveyId = parseInt(this.props.surveyId);

            const result = await jsonrpc("/survey.user_input/get_current_question_and_answers", {
                survey_id: surveyId,
                input_id: inputId,
            });

            if (result.completed) {
                this.state.completed = true;
            } else {
                this.state.question = result.question;
                this.state.answers = result.answers;
            }

            this.state.loading = false;
        });
    }

    async submit(answerId) {
        const inputId = parseInt(this.props.inputId);
        const questionId = this.state.question.id;

        const result = await jsonrpc("/survey.user_input/submit_answer", {
            input_id: inputId,
            question_id: questionId,
            answer_id: answerId,
        });

        if (result.status === "ok") {
            // Refrescar para la siguiente pregunta
            window.location.reload();
        } else {
            alert("Error al enviar respuesta");
        }
    }
}
