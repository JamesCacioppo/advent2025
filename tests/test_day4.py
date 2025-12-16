import day4 as d4
from day1 import read_file


lines = read_file("data/day4_sample")

paper_rolls_array = []
for line in lines:
    paper_rolls_array.append(list(line))


def test_check_adjacent_places():
    assert d4.check_adjacent_places(0, 2, paper_rolls_array)
    assert d4.check_adjacent_places(0, 3, paper_rolls_array)
    assert d4.check_adjacent_places(0, 5, paper_rolls_array)
    assert not d4.check_adjacent_places(0, 7, paper_rolls_array)

    assert d4.check_adjacent_places(1, 0, paper_rolls_array)
    assert not d4.check_adjacent_places(1, 1, paper_rolls_array)
    assert not d4.check_adjacent_places(1, 2, paper_rolls_array)


def test_solve1():
    assert d4.solve1("data/day4_sample") == 13


def test_solve2():
    assert d4.solve2("data/day4_sample") == 43
