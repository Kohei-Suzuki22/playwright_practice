from pom.contact_us_page import ContactUsPage


def test_submit_form(set_up) -> None:

    page = set_up
    contact_us = ContactUsPage(page)
    contact_us.navigate()

    contact_us.submit_form('taro', 'my address', 'test@gmail.com', '111-1111-1111', 'test subject', 'test message blah')
    assert (1+1) == 3
