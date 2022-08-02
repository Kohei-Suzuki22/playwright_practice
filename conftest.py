import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


@pytest.fixture
def set_up(page):
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    yield page
