/** @odoo-module **/

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
                console.log("Survey ID:", surveyId); // Verifica el valor de surveyId

                // Llamada JSON-RPC para obtener los datos de la encuesta
                const result = await jsonrpc(`/kahoot/game/data/${surveyId}`);
                console.log("Game Data:", result); // Verifica la respuesta de la solicitud JSON-RPC
                
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
