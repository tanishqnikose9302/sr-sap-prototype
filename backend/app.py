# backend/app.py
from flask import Flask, jsonify, request
import os

app = Flask(__name__)

@app.route("/api/health")
def health():
    return jsonify({"status": "ok"}), 200

@app.route("/api/reports", methods=["POST"])
def create_report():
    data = request.json or {}
    required = ["user_id", "title", "latitude", "longitude"]
    for key in required:
        if key not in data:
            return jsonify({"error": f"Missing field: {key}"}), 400

    resp = {
        "report_id": "rpt_001",
        "received": data
    }
    return jsonify(resp), 201

@app.route("/api/recommend", methods=["POST"])
def recommend():
    profile = request.json or {}
    skills = profile.get("skills", "")

    if "agro" in skills:
        rec = [
            "Course: Climate-smart agriculture",
            "Nearby resource: Krishi Vigyan Kendra"
        ]
    else:
        rec = ["Please complete skill assessment for better recommendations"]

    return jsonify({"recommendations": rec})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
