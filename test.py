import pdb

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://symonstorozhenko.wixsite.com/website-1
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    pdb.set_trace()
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
