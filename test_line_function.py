import pytest

@pytest.mark.parametrize("point1, point2, x, expected", [
    [(1, 1), (4, 4), 8, 8],
    [(2, 4), (6, 12), 3, 6],
    [(-3, -1), (-15, -5), -18, -6]
    ])
def test_find_y(point1, point2, x, expected):
    from line_function import find_y
    answer = find_y(point1, point2, x)
    assert answer == expected
