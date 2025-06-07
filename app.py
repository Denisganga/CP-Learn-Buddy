from flask import Flask, render_template, request
import requests

app = Flask(__name__)

LAMBDA_API_URL = "https://31xtjgdsjc.execute-api.us-east-1.amazonaws.com/dev/learn"  # Replace with your real URL

@app.route('/', methods=['GET', 'POST'])
def index():
    audio_url = None
    if request.method == 'POST':
        user_text = request.form.get('text')
        response = requests.post(LAMBDA_API_URL, data=user_text)
        if response.status_code == 200:
            audio_url = response.json().get('audio_url')
        else:
            audio_url = None
    return render_template('index.html', audio_url=audio_url)

if __name__ == '__main__':
    app.run(debug=True)
