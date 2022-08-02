import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


@pytest.fixture
def set_up(playwright: Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    yield  page
