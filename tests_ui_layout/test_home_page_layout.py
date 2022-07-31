from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePage
from pom.shop_women_elements import ShopWomem


def about_us_selection_verbiage(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    shop_women = ShopWomem(page)
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()
    expect(shop_women.celebrating_beauty_header).to_be_visible()
    expect(shop_women.celebrating_beauty_body).to_be_visible()


with sync_playwright() as playwright:
    about_us_selection_verbiage(playwright)