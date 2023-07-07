from flask import Flask, request, render_template
from flask_cors import CORS
import openai
import html

app = Flask(__name__)
CORS(app)
app.debug = True

openai.api_key = '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'

@app.route('/')
def home():
    return 'Welcome to the chatbot!'

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']

    # Call the OpenAI API to generate a response
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=50,
        temperature=0.7
    )

    # Extract the response text and unescape any special characters
    response_text = html.unescape(response.choices[0].text.strip())

    # Return the response as plain text
    return response_text

if __name__ == '__main__':
    app.run()
