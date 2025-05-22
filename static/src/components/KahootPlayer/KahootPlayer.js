/** @odoo-module **/

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
                const surveyId = parseInt(this.props.surveyId); 
                console.log("Survey ID:", surveyId); // Verifica el valor de surveyId

                // Uso rpc.query para llamar a la ruta de datos de la encuesta
                const result = await rpc.query({
                    model: 'survey.survey',
                    method: 'kahoot_game_data',  // Método que se usa en el backend
                    args: [surveyId],
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
