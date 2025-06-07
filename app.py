from flask import Flask, render_template, request
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Load AWS credentials from .env file
aws_region = os.getenv("AWS_REGION")
polly_client = boto3.client('polly', region_name=aws_region)

@app.route('/', methods=['GET', 'POST'])
def index():
    output_text = ""
    audio_url = ""
    
    if request.method == 'POST':
        input_text = request.form['text']
        
        # Simulate calling Lambda here (later you'll integrate real Lambda + Bedrock)
        simplified_text = simulate_bedrock_simplification(input_text)

        # Use Amazon Polly to synthesize simplified text
        response = polly_client.synthesize_speech(
            Text=simplified_text,
            OutputFormat='mp3',
            VoiceId='Joanna'
        )

        # Save audio to file
        with open("static/output.mp3", "wb") as f:
            f.write(response['AudioStream'].read())
            audio_url = "static/output.mp3"

        output_text = simplified_text

    return render_template('index.html', output=output_text, audio=audio_url)

def simulate_bedrock_simplification(text):
    # Replace this later with real Lambda+Bedrock call
    return "Simplified: " + text.lower()

if __name__ == '__main__':
    app.run(debug=True)
