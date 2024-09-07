import json
from flask import Flask, request, jsonify
from transformers import pipeline
from huggingface_hub import login
import os

app = Flask(__name__)

# Retrieve the Hugging Face token from environment variables
hf_token = os.getenv('HUGGINGFACE_TOKEN')

# Log into Hugging Face using the token
if hf_token:
    login(token=hf_token)
else:
    raise ValueError("HUGGINGFACE_TOKEN environment variable not set.")

# Initialize the chatbot pipeline with the token for private model access
chatbot = pipeline(
    'text-generation',
    model='google/gemma-2-2b-it',
    use_auth_token=hf_token  # Pass the token here for model access
)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Parse the JSON body from the request
        body = request.get_json()
        message = body['message']
        
        # Generate a response from the chatbot
        response = chatbot(message)
        reply = response[0]['generated_text']
        
        # Return the response as JSON
        return jsonify({'reply': reply}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
