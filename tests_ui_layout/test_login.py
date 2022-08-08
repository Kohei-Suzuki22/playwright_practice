import pdb
import time

import pytest


@pytest.mark.skip
def test_logged_user_can_view_my_orders_menu(login_set_up) -> None:

    page = login_set_up

    page.locator("[aria-label='foo account menu']").click()

    assert page.locator("text='My Orders'").is_visible()

