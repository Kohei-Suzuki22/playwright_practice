import pytest
from playwright.sync_api import Playwright


@pytest.fixture
def set_up(page):


    # cliでbase-urlを指定している場合でも、空文字で指定する必要がある。
    page.goto("")

    yield page
