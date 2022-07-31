import time

from playwright.sync_api import Playwright, sync_playwright,expect
from pom.contact_us_page import ContactUsPage


def test_submit_form(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    contact_us = ContactUsPage(page)
    contact_us.navigate()

    contact_us.submit_form('taro', 'my address', 'test@gmail.com', '111-1111-1111', 'test subject', 'test message blah')


with sync_playwright() as playwright:
    test_submit_form(playwright)
    time.sleep(5)