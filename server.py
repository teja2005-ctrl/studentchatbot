"""
EduBot — Optional Python Proxy Server
======================================
Use this if you want to hide your Anthropic API key on the server side.
Run: python server.py

The frontend will call /api/chat instead of Anthropic directly.
Update the fetch URL in index.html:
  FROM: https://api.anthropic.com/v1/messages
  TO:   /api/chat
"""

import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__, static_folder=".", static_url_path="")
CORS(app)

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
ANTHROPIC_API_URL = "https://api.anthropic.com/v1/messages"


@app.route("/")
def index():
    return app.send_static_file("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    if not ANTHROPIC_API_KEY:
        return jsonify({"error": "ANTHROPIC_API_KEY not set on server."}), 500

    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid request body."}), 400

    # Proxy the request to Anthropic
    headers = {
        "Content-Type": "application/json",
        "x-api-key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
    }

    try:
        resp = requests.post(ANTHROPIC_API_URL, json=data, headers=headers, timeout=30)
        return jsonify(resp.json()), resp.status_code
    except requests.exceptions.Timeout:
        return jsonify({"error": "Request to Anthropic timed out."}), 504
    except requests.exceptions.RequestException as e:
        return jsonify({"error": str(e)}), 502


@app.route("/health")
def health():
    return jsonify({"status": "ok", "service": "EduBot Proxy"})


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    print(f"🎓 EduBot proxy running on http://localhost:{port}")
    print(f"   API key configured: {'✅ Yes' if ANTHROPIC_API_KEY else '❌ No — set ANTHROPIC_API_KEY in .env'}")
    app.run(host="0.0.0.0", port=port, debug=debug)
