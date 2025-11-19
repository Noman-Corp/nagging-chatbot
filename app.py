from flask import Flask
from flask import Flask, request, jsonify
from utils.groq_client import ask_groq

app = Flask(__name__)

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()

    if not data or "message" not in data:
        return jsonify({"error": "Missing 'message' field"}), 400

    user_msg = data["message"]

    if not isinstance(user_msg, str):
        return jsonify({"error": "'message' must be a string"}), 400

    if user_msg.strip() == "":
        return jsonify({"error": "Message cannot be empty"}), 400

    if len(user_msg) > 500:
        return jsonify({"error": "Message too long (max 500 chars)"}), 400

    # 
    try:
        reply = ask_groq(user_msg)
        return jsonify({"reply": reply})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
