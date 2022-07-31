import pdb

from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


@pytest.mark.smoke
def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    # Open new page
    page = context.new_page()
    # Go to https://symonstorozhenko.wixsite.com/website-1
    page.goto("https://symonstorozhenko.wixsite.com/website-1")
    assert (1 + 1) == 2


    # ---------------------
    context.close()
    browser.close()

@pytest.mark.integration
def test_run2(playwright: Playwright) -> None:

    assert (1 + 1) == 2



@pytest.mark.regression
def test_run3(playwright: Playwright) -> None:
    assert (1 + 1) == 2