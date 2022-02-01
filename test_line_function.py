import pytest

@pytest.mark.parametrize("point1, point2, x, expected", [
    [(1, 1), (4, 7), 8, 15],
    [(2, 4), (6, 12), 3, 6],
    [(-3, -1), (-13, -5), 5, 11/5]
    ])
def test_find_y(point1, point2, x, expected):
    from line_function import find_y
    answer = find_y(point1, point2, x)
    assert answer == expected
