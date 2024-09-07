from transformers import pipeline
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize the chatbot
chatbot = pipeline('conversational', model='facebook/blenderbot-400M-distill')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Parse the JSON body from the request
        body = request.get_json()
        message = body['message']
        
        # Generate a response
        response = chatbot(message)
        reply = response[0]['generated_text']
        
        # Return the response as JSON
        return jsonify({'reply': reply}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
