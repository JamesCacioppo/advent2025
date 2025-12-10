from day2 import build_range, read_file, check_product_id_for_pattern, solve1


def test_read_file():
    lines = read_file("data/day2_sample")
    assert lines == [
        "11-22",
        "95-115",
        "998-1012",
        "1188511880-1188511890",
        "222220-222224",
        "1698522-1698528",
        "446443-446449",
        "38593856-38593862",
        "565653-565659",
        "824824821-824824827",
        "2121212118-2121212124",
    ]


def test_build_range():
    range = build_range("11-22")
    assert range == [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]


def test_check_product_id_for_pattern():
    assert check_product_id_for_pattern(11)
    assert check_product_id_for_pattern(22)
    assert check_product_id_for_pattern(99)
    assert check_product_id_for_pattern(1010)
    assert check_product_id_for_pattern(1188511885)
    assert check_product_id_for_pattern(222222)
    assert check_product_id_for_pattern(446446)
    assert check_product_id_for_pattern(38593859)

    for i in range(12, 22):
        assert not check_product_id_for_pattern(i)

    for i in range(100, 116):
        assert not check_product_id_for_pattern(i)


def test_solve1():
    assert solve1("data/day2_sample") == 1227775554
