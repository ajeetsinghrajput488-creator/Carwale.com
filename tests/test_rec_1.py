import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.carwale.com/")
    page.wait_for_timeout(5000)
    