import time

import pytest
from playwright.sync_api import Playwright


@pytest.fixture()
def set_up(page):

    # cliでbase-urlを指定している場合でも、空文字で指定する必要がある。
    page.goto("")

    yield page


@pytest.fixture()
def login_set_up(set_up):

    page = set_up
    time.sleep(2)

    page.locator("button >> text='Log In'").click()
    page.locator("[data-testid='signUp.switchToSignUp']").click()

    page.locator("[data-testid='switchToEmailLink'] >> [data-testid='buttonElement']").click()
    page.locator("[data-testid='emailAuth'] >> input[type='email']").click()
    page.locator("[data-testid='emailAuth'] >> input[type='email']").fill("foo@gmail.com")
    page.locator("input[type='password']").click()
    page.locator("input[type='password']").fill("password")
    page.locator("[data-testid='submit'] [data-testid='buttonElement']").click()

    yield page

@pytest.fixture
def go_to_new_collection_page(page):


    # cliでbase-urlを指定している場合でも、空文字で指定する必要がある。
    page.goto("/new-collection")
    page.set_default_timeout(3000)

    yield page
