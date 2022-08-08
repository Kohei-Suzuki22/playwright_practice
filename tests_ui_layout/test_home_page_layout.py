import time

from playwright.sync_api import expect
from pom.home_page_elements import HomePage
from pom.shop_women_elements import ShopWomem
import pytest


@pytest.mark.login_check
def test_about_us_selection_verbiage(set_up) -> None:

    page = set_up
    shop_women = ShopWomem(page)
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()
    expect(shop_women.celebrating_beauty_header).to_be_visible()
    expect(shop_women.celebrating_beauty_body).to_be_visible()


@pytest.mark.login_check
def test_about_us_selection_verbiage_after_login(login_set_up) -> None:

    page = login_set_up
    shop_women = ShopWomem(page)
    home_page = HomePage(page)
    time.sleep(5)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()
    expect(shop_women.celebrating_beauty_header).to_be_visible()
    expect(shop_women.celebrating_beauty_body).to_be_visible()


@pytest.mark.xfail(reason="assert expect fail")     # 一時的に失敗することを許容する時
def test_about_us_selection_verbiage_xfail(login_set_up) -> None:

    page = login_set_up
    shop_women = ShopWomem(page)
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()
    expect(shop_women.celebrating_beauty_header).to_be_visible()
    expect(shop_women.celebrating_beauty_body).to_be_visible()
    assert (1 + 1) == 3


@pytest.mark.xfail(reason="assert expect fail")     # xfailををつけていても、passする場合は結果に「xpass」とを表示される
def test_about_us_selection_verbiage_xpass(set_up) -> None:

    page = set_up
    shop_women = ShopWomem(page)
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()
    expect(shop_women.celebrating_beauty_header).to_be_visible()
    expect(shop_women.celebrating_beauty_body).to_be_visible()


@pytest.mark.skip(reason="not ready")       # テストをスキップする。 reasonは実行コンソールに出てくる。
def test_about_us_selection_verbiage_2(set_up) -> None:

    page = set_up
    shop_women = ShopWomem(page)
    home_page = HomePage(page)
    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()
    expect(shop_women.celebrating_beauty_header).to_be_visible()
    expect(shop_women.celebrating_beauty_body).to_be_visible()
    expect(shop_women.celebrating_beauty_body).to_be_hidden()
    assert (1 + 1) == 3


@pytest.mark.skip
def test_about_us_selection_verbiage_fail(set_up) -> None:

    page = set_up
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
