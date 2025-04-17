from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/transcript', methods=['GET'])
def get_transcript():
    video_id = request.args.get('video_id')
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['de', 'en'])
        text = " ".join([entry['text'] for entry in transcript])
        return jsonify({"transcript": text})
    except Exception as e:
        return jsonify({"error": str(e)}), 400
