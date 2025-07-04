from flask import Flask, request, jsonify
from poe_scraper import ask_poe

app = Flask(__name__)

@app.route("/")
def home():
    return "🤖 GPT-4o scraper is live!"

@app.route("/ask")
def ask():
    prompt = request.args.get("prompt")
    if not prompt:
        return jsonify({"error": "Missing 'prompt' query."}), 400
    answer = ask_poe(prompt)
    return jsonify({"question": prompt, "answer": answer})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
