import { Component, useState, onWillStart } from '@odoo/owl';
import { rpc } from '@web/core/rpc_service';

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
                const surveyId = parseInt(this.props.surveyId); // Asegúrate de que este surveyId se pase correctamente
                console.log("Survey ID:", surveyId); // Verifica el valor de surveyId
                
                // Solicitar datos usando rpc.query
                const result = await rpc.query({
                    model: 'survey.survey',
                    method: 'get_game_data',  // Método en el backend
                    args: [surveyId],  // Argumentos pasados al método
                });

                console.log("Game Data:", result); // Verifica la respuesta de la solicitud RPC
                
                if (result.error) {
                    this.state.error = result.error;
                } else {
                    this.state.survey = result.survey;
                    this.state.question = result.question;
                }
            } catch (err) {
                console.error('Error loading data:', err); 
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
