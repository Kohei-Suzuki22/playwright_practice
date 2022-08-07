import time

import pytest

from pom.contact_us_page import ContactUsPage


## parameterizeはテストメソッドにつけることができる。 fixtureにはつけたら読み込まれなかった。
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
