from transformers import pipeline
import json

def handler(request):
    try:
        # Parse the JSON body from the request
        body = request.json()
        message = body['message']
        
        # Initialize the chatbot
        chatbot = pipeline('conversational', model='facebook/blenderbot-400M-distill')
        
        # Generate a response
        response = chatbot(message)
        reply = response[0]['generated_text']

        # Return the response as JSON
        return {
            'statusCode': 200,
            'body': json.dumps({'reply': reply}),
            'headers': {'Content-Type': 'application/json'}
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)}),
            'headers': {'Content-Type': 'application/json'}
        }
