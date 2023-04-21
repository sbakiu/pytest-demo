from src.app import one_and_one


def test_one_and_one():
    result = one_and_one()
    expected_result = 2
    assert result == expected_result
