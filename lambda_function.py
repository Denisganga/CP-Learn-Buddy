import boto3
import uuid
import json

def lambda_handler(event, context):
    text = event.get("body", "")
    if not text:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Text is required"})
        }

    polly = boto3.client("polly")
    s3 = boto3.client("s3")

    audio_file_name = f"{uuid.uuid4()}.mp3"
    bucket_name = "cp-learn-audio-bucket"

    try:
        response = polly.synthesize_speech(
            Text=text,
            OutputFormat="mp3",
            VoiceId="Joanna"
        )

        audio_stream = response['AudioStream'].read()


        s3.put_object(
            Bucket=bucket_name,
            Key=audio_file_name,
            Body=audio_stream,
            ContentType='audio/mpeg'
        )

        audio_url = f"https://{bucket_name}.s3.amazonaws.com/{audio_file_name}"

        return {
            "statusCode": 200,
            "body": json.dumps({"audio_url": audio_url})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }