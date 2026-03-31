from flask import Flask, render_template, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# Replace 'your-api-key-here' with your actual OpenAI API Key
client = OpenAI(api_key="your-api-key-here")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message")
    
    try:
        # Calling the OpenAI API (Same tech behind ChatGPT)
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # or "gpt-4"
            messages=[
                {"role": "system", "content": "You are a helpful personal assistant named MyAI."},
                {"role": "user", "content": user_message}
            ]
        )
        ai_reply = response.choices[0].message.content
        return jsonify({"reply": ai_reply})
    except Exception as e:
        return jsonify({"reply": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)