from pom.home_page_elements import HomePage
from playwright.sync_api import Playwright, sync_playwright, expect



def test_visual_landing2_1(page, assert_snapshot) -> None:
    page.goto("https://symonstorozhenko.wixsite.com/website-1/shop")
    homepage = HomePage(page)
    # expect(homepage.celebrate_header).to_be_visible()
    assert_snapshot(page.screenshot())


def test_visual_landing2_2(page, assert_snapshot) -> None:
    page.goto("https://symonstorozhenko.wixsite.com/website-1/shop")
    homepage = HomePage(page)
    # expect(homepage.celebrate_header).to_be_visible()
    assert_snapshot(page.screenshot())