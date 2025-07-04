# poe_scraper.py
from playwright.sync_api import sync_playwright

PB_COOKIE = "9XW1lCrtQcjFMf4zyeWm8Q%3D%3D"

def ask_poe(question: str) -> str:
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
        answer = response.inner_text() if response else "❌ No response."
        browser.close()
        return answer
