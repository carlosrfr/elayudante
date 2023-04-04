import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
openai.api_key = "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"
app = Flask(__name__)
@app.route('/whatsapp', methods=['POST'])
def whatsapp():
    # Obtén el mensaje entrante
    mensaje_entrante = request.values.get('Body', '').strip()

    # Procesa el mensaje utilizando la API de GPT-3
    respuesta_gpt3 = openai.Completion.create(
        engine="davinci-codex",
        prompt=mensaje_entrante,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    )
    
    # Extrae la respuesta del modelo GPT-3
    respuesta_texto = respuesta_gpt3.choices[0].text.strip()

    # Prepara la respuesta de Twilio
    respuesta = MessagingResponse()
    respuesta.message(respuesta_texto)

    return str(respuesta)
if __name__ == '__main__':
    app.run(debug=True)
