import pdb
import time


def test_login(login_set_up) -> None:

    page = login_set_up

    page.locator("[aria-label='foo account menu']").click()

    assert page.locator("text='My Orders'").is_visible()

