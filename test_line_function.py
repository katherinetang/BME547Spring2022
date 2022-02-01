import pytest

@pytest.mark.parametrize("point1, point2, x, expected", [
    [(1, 1), (4, 7), 8, 15],
    [(2, 4), (6, 12), 3, 6],
    [(-3, -1), (-2, -6), -5, 9]
    ])
def test_find_y(point1, point2, x, expected):
    from line_function import find_y
    answer = find_y(point1, point2, x)
    assert answer == expected


@pytest.mark.parametrize("point1, point2, expected1, expected2", [
    [(1, 1), (4, 7), 2.0, -1.0],
    [(2, 4), (6, 12), 2.0, 0],
    [(-3, -1), (-2, -6), -5, -16]
    ])
def test_find_eqn(point1, point2, expected1, expected2):
    from line_function import find_eqn
    answer1, answer2 = find_eqn(point1, point2)
    assert answer1 == expected1
    assert answer2 == expected2