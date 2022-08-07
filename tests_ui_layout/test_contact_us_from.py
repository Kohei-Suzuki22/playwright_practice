import time

import pytest

from pom.contact_us_page import ContactUsPage


# parameterizeはテストメソッドにつけることができる。 fixtureにはつけたら読み込まれなかった。
# パラメータが2つ以上ある際は、値はタプル = () でくくる。 一つの場合は、タプルは必要ない。
@pytest.mark.parametrize("email, num", [
                          # パラメータによっては、xfailにしたいものが出てくる。その場合は、以下のように設定。
                          pytest.param("foo@gmail.com", 1, marks=pytest.mark.xfail(reason='wrong calc')),
                          ("bar@gmail.com", 2),
                          pytest.param("foo@gmail.com", 3, marks=pytest.mark.xfail(reason='wrong calc'))
                          ])
def test_submit_form(set_up, email, num) -> None:

    page = set_up
    contact_us = ContactUsPage(page)
    contact_us.navigate()

    contact_us.submit_form('taro', 'my address', email, '111-1111-1111', 'test subject', 'test message blah')
    assert (1+1) == num


# 各パラメータを別々に分けることによって、すべてのパターンに対してのテストができる。ここでは、email3パターン✖ ︎password3パターンで 9パターンのテストをすることになる。
@pytest.mark.parametrize("email", [
                          # パラメータによっては、xfailにしたいものが出てくる。その場合は、以下のように設定。
                          "foo@gmail.com",
                          "bar@gmail.com",
                          "baz@gmail.com"
                          ])
@pytest.mark.parametrize("num", [
                          # パラメータによっては、xfailにしたいものが出てくる。その場合は、以下のように設定。
                          pytest.param(1, marks=pytest.mark.xfail(reason='wrong calc')),
                          2,
                          pytest.param(3, marks=pytest.mark.xfail(reason='wrong calc'))
                          ])

def test_submit_form2(set_up, email, num) -> None:

    page = set_up
    contact_us = ContactUsPage(page)
    contact_us.navigate()

    contact_us.submit_form('taro', 'my address', email, '111-1111-1111', 'test subject', 'test message blah')
    assert (1+1) == num
