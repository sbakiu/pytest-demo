import pytest

from src.square import square


@pytest.mark.math
@pytest.mark.parametrize("x, sq", [(1, 1), (2, 4), (3, 9), (4, 16)])
def test_square(x, sq):
    assert square(x) == sq
