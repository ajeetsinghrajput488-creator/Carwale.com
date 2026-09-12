from playwright .sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.carwale.com/")
    input("Press enter once logged in")
    context.storage_state(path="auth/auth.json")
    browser.close()