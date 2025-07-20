from flask import Blueprint, request, jsonify
from app.spotify_utils import analyze_track, extract_track_id

routes = Blueprint("routes", __name__)  # ✅ MUST be called 'routes'

@routes.route("/", methods=["GET"])  # Optional root route to test
def home():
    return "API is live!", 200

@routes.route("/analyze", methods=["POST"])
def analyze():
    print("📩 Received POST /analyze")  # Debug

    data = request.get_json()
    print("🔍 Data received:", data)

    if not data or "track" not in data:
        return jsonify({"error": "Missing 'track' in request body."}), 400

    track_input = data["track"]
    track_id = extract_track_id(track_input)
    print("🎵 Track ID:", track_id)

    result = analyze_track(track_id)
    print("✅ Analysis result:", result)

    return jsonify(result)
