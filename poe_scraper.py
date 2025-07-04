import os
from flask import Flask, request
from playwright.sync_api import sync_playwright

app = Flask(__name__)

# 🔑 Poe p-b cookie
PB_COOKIE = "9XW1lCrtQcjFMf4zyeWm8Q%3D%3D"

@app.route("/", methods=["GET"])
def ask_route():
    question = request.args.get("ask")
    if not question:
        return "🤖 Poe GPT-4o Scraper is running. Use '?ask=your-question' to ask."

    try:
        response = ask_poe(question)
        return response
    except Exception as e:
        return f"❌ Error: {str(e)}", 500

def ask_poe(prompt):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox", "--disable-setuid-sandbox"])
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
        page.fill("textarea", prompt)
        page.keyboard.press("Enter")
        page.wait_for_selector(".Message_botMessageBubble", timeout=20000)

        result = page.query_selector(".Message_botMessageBubble")
        text = result.inner_text() if result else "⚠️ No response found."
        browser.close()
        return text

# ✅ Required for Render to detect PORT
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port)
