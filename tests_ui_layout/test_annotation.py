import pdb

import pytest


@pytest.mark.smoke
def test_run(set_up) -> None:
    assert (1 + 1) == 2

@pytest.mark.integration
def test_run2(set_up) -> None:

    assert (1 + 1) == 2



@pytest.mark.regression
def test_run3(set_up) -> None:
    assert (1 + 1) == 2

@pytest.mark.regression
def test_run4(set_up) -> None:
    assert (1 + 1) == 2