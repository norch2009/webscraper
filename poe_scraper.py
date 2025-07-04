from flask import Flask, request
from playwright.sync_api import sync_playwright

# 🛑 Palitan mo ito ng Poe p-b cookie mo
PB_COOKIE = "9XW1lCrtQcjFMf4zyeWm8Q%3D%3D"

app = Flask(__name__)

@app.route("/", methods=["GET"])
def ask_route():
    question = request.args.get("ask", "")
    if not question:
        return "❌ Missing `ask` query parameter.", 400

    try:
        answer = ask_poe(question)
        return answer
    except Exception as e:
        return f"❌ Error: {e}", 500

def ask_poe(question: str):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()

        context.add_cookies([{
            'name': 'p-b',
            'value': PB_COOKIE,
            'domain': '.poe.com',
            'path': '/',
            'httpOnly': True,
            'secure': True,
            'sameSite': 'Lax'
        }])

        page = context.new_page()
        page.goto("https://poe.com/GPT-4o", wait_until="networkidle")
        page.wait_for_selector("textarea")
        page.fill("textarea", question)
        page.keyboard.press("Enter")
        page.wait_for_selector(".Message_botMessageBubble", timeout=20000)

        response = page.query_selector(".Message_botMessageBubble")
        answer = response.inner_text() if response else "❌ No response found."

        browser.close()
        return answer

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
