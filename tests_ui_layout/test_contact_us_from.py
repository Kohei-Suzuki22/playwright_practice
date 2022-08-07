import time

import pytest

from pom.contact_us_page import ContactUsPage


## parameterizeはテストメソッドにつけることができる。 fixtureにはつけたら読み込まれなかった。
@pytest.mark.parametrize("email, num", [("foo@gmail.com",1),("bar@gmail.com",2),("foo@gmail.com",3)])
def test_submit_form(set_up,email,num) -> None:

    page = set_up
    contact_us = ContactUsPage(page)
    contact_us.navigate()

    contact_us.submit_form('taro', 'my address', email, '111-1111-1111', 'test subject', 'test message blah')
    time.sleep(2)
    assert (1+1) == num
