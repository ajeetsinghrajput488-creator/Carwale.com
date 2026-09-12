from playwright.sync_api import Page

def test_google_search (page):

    page.wait_for_timeout(3000) # wait for 3 seconds to ensure the page is fully loaded

    page.goto("https://www.google.com/ncr")

    print('page is loaded and pass')
