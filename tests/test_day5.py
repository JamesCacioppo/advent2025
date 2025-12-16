import day5 as d5

def test_read_input():
    sample_data = ['3-5', '10-14', '16-20', '12-18', '', '1', '5', '8', '11', '17', '32']
    assert d5.read_input("data/day5_sample") == sample_data

def test_split_input_list():
    sample_data = ['3-5', '10-14', '16-20', '12-18', '', '1', '5', '8', '11', '17', '32']
    expected_range = [range(3, 5+1), range(10, 14+1), range(16, 20+1), range(12, 18+1)]
    expected_ingredients = [1, 5, 8, 11, 17, 32]
    assert d5.split_input_list(sample_data) == (expected_range, expected_ingredients)

def test_find_ingredient_in_fresh_list():
    fresh_ranges = [range(3, 5+1), range(10, 14+1), range(16, 20+1), range(12, 18+1)]

    assert not d5.find_ingredient_in_fresh_list(1, fresh_ranges)
    assert d5.find_ingredient_in_fresh_list(5, fresh_ranges)
    assert not d5.find_ingredient_in_fresh_list(8, fresh_ranges)
    assert d5.find_ingredient_in_fresh_list(11, fresh_ranges)
    assert d5.find_ingredient_in_fresh_list(17, fresh_ranges)
    assert not d5.find_ingredient_in_fresh_list(32, fresh_ranges)

def test_d5_solve1():
    assert d5.solve1('data/day5_sample') == 3

def test_d5_solve2():
    assert d5.solve2('data/day5_sample') == 14