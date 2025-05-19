import { Component, useState, onWillStart } from '@odoo/owl';
import { jsonrpc } from '@web/core/network/rpc_service';

export class KahootPlayer extends Component {
    setup() {
        this.state = useState({
            loading: true,
            error: null,
            survey: null,
            question: null,
        });

        onWillStart(async () => {
            try {
                const surveyId = parseInt(this.props.surveyId);
                const result = await jsonrpc(`/kahoot/game/data/${surveyId}`);
                this.state.survey = result.survey;
                this.state.question = result.question;
            } catch (err) {
                this.state.error = 'Error al cargar los datos del juego';
            } finally {
                this.state.loading = false;
            }
        });
    }

    async submitAnswer(answerId) {
        alert(`Respuesta enviada: ${answerId}`);
    }
}
KahootPlayer.template = 'ninja_quiz.KahootPlayer';

export default KahootPlayer;
