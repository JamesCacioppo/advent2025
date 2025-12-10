import day3 as d3


def test_find_highest_number():
    assert d3.find_highest_number("987654321111111") == (9, 0)
    assert d3.find_highest_number("87654321111111") == (8, 0)
    assert d3.find_highest_number("811111111111119") == (8, 0)
    assert d3.find_highest_number("11111111111119") == (9, 13)


def test_find_joltage():
    assert d3.find_joltage("987654321111111") == 98
    assert d3.find_joltage("811111111111119") == 89
    assert d3.find_joltage("234234234234278") == 78
    assert d3.find_joltage("818181911112111") == 92


def test_solve1():
    assert d3.solve1("data/day3_sample") == 357
