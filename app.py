# app.py
from flask import Flask, request, jsonify
from poe_scraper import ask_poe

app = Flask(__name__)

@app.route("/")
def home():
    return "🧠 Poe GPT-4o Scraper is running."

@app.route("/ask")
def ask():
    prompt = request.args.get("prompt")
    if not prompt:
        return jsonify({"error": "Missing 'prompt' query"}), 400
    try:
        answer = ask_poe(prompt)
        return jsonify({"question": prompt, "answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
