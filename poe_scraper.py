from playwright.sync_api import sync_playwright
import time

PB_COOKIE = "9XW1lCrtQcjFMf4zyeWm8Q%3D%3D"  # palitan mo ng bago kung nag-expire

def ask_poe(prompt):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--no-sandbox"])
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
        try:
            page.goto("https://poe.com/GPT-4o", wait_until="domcontentloaded", timeout=30000)
            time.sleep(2)

            page.wait_for_selector("textarea", timeout=10000)
            page.fill("textarea", prompt)
            page.keyboard.press("Enter")

            # wait for response up to 40s
            page.wait_for_selector(".Message_botMessageBubble", timeout=40000)
            messages = page.query_selector_all(".Message_botMessageBubble")

            if messages:
                last_message = messages[-1].inner_text()
            else:
                last_message = "❌ GPT-4o did not reply."

        except Exception as e:
            last_message = f"❌ Error: {str(e)}"

        browser.close()
        return last_message
