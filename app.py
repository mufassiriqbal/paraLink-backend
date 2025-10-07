from flask import Flask, request, jsonify, send_file
from services.ai_service import generate_message
from services.tts_service import text_to_speech
import os

app = Flask(__name__)

@app.route("/api/health", methods=["GET"])
def health_check():
    return jsonify({"status": "OK", "message": "ParaLink backend running!"})

@app.route("/api/generate_message", methods=["POST"])
def generate_ai_message():
    """
    Takes JSON: {"base_text": "I need water", "tone": "polite"}
    Returns AI-generated Roman Urdu response.
    """
    data = request.get_json()
    base_text = data.get("base_text", "")
    tone = data.get("tone", "polite")

    if not base_text:
        return jsonify({"error": "Missing base_text"}), 400

    try:
        result = generate_message(base_text, tone)
        return jsonify({"response": result})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/speak", methods=["POST"])
def speak_text():
    """
    Takes JSON: {"text": "mujhe pani chahiye"}
    Returns path to generated audio file
    """
    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "Missing text"}), 400

    audio_path = text_to_speech(text)
    return send_file(audio_path, mimetype="audio/mpeg")


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
