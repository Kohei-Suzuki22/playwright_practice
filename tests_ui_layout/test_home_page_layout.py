from playwright.sync_api import Playwright, sync_playwright, expect
from pom.home_page_elements import HomePage
from pom.shop_women_elements import ShopWomem
import pytest



def test_about_us_selection_verbiage(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    shop_women = ShopWomem(page)
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()
    expect(shop_women.celebrating_beauty_header).to_be_visible()
    expect(shop_women.celebrating_beauty_body).to_be_visible()
    assert (1 + 1) == 2


@pytest.mark.xfail(reason="assert expect fail")     # 一時的に失敗することを許容する時
def test_about_us_selection_verbiage_xfail(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    shop_women = ShopWomem(page)
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()
    expect(shop_women.celebrating_beauty_header).to_be_visible()
    expect(shop_women.celebrating_beauty_body).to_be_visible()
    assert (1 + 1) == 3

@pytest.mark.xfail(reason="assert expect fail")     # xfailををつけていても、passする場合は結果に「xpass」とを表示される
def test_about_us_selection_verbiage_xpass(playwright: Playwright) -> None:
        browser = playwright.chromium.launch()
        page = browser.new_page()
        page.goto("https://symonstorozhenko.wixsite.com/website-1")

        shop_women = ShopWomem(page)
        home_page = HomePage(page)
        expect(home_page.celebrate_header).to_be_visible()
        expect(home_page.celebrate_body).to_be_visible()
        expect(shop_women.celebrating_beauty_header).to_be_visible()
        expect(shop_women.celebrating_beauty_body).to_be_visible()

@pytest.mark.skip(reason="not ready")       # テストをスキップする。 reasonは実行コンソールに出てくる。
def test_about_us_selection_verbiage_2(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    shop_women = ShopWomem(page)
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()
    expect(shop_women.celebrating_beauty_header).to_be_visible()
    expect(shop_women.celebrating_beauty_body).to_be_visible()
    expect(shop_women.celebrating_beauty_body).to_be_hidden()
    assert (1 + 1) == 3


@pytest.mark.skip
def test_about_us_selection_verbiage_fail(playwright: Playwright) -> None:
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    shop_women = ShopWomem(page)
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()
    expect(shop_women.celebrating_beauty_header).to_be_visible()
    expect(shop_women.celebrating_beauty_body).to_be_visible()
    expect(shop_women.celebrating_beauty_body).to_be_hidden()
    assert (1 + 1) == 3


'''
xfailをつけていて、failしないものに関しては、xpassという出力がされる。
xfailは失敗することを期待しているという意味合いもあるため、成功している場合は、出力結果の色バーが黄色(注意の色)で表示される。
'''



