import day3 as d3


def test_find_highest_value():
    assert d3.find_highest_value("987654321111111") == (9, 0)
    assert d3.find_highest_value("87654321111111") == (8, 0)
    assert d3.find_highest_value("811111111111119") == (9, 14)
    assert d3.find_highest_value("11111111111119") == (9, 13)
    assert d3.find_highest_value("123454325111") == (5, 4)


def test_find_joltage():
    assert d3.find_joltage("987654321111111") == 98
    assert d3.find_joltage("811111111111119") == 89
    assert d3.find_joltage("234234234234278") == 78
    assert d3.find_joltage("818181911112111") == 92


def test_solve1():
    assert d3.solve1("data/day3_sample") == 357


def test_find_twelve_char_joltage():
    assert d3.find_twelve_char_joltage("987654321111111") == 987654321111
    assert d3.find_twelve_char_joltage("811111111111119") == 811111111119
    assert d3.find_twelve_char_joltage("234234234234278") == 434234234278
    assert d3.find_twelve_char_joltage("818181911112111") == 888911112111
