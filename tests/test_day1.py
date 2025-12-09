from day1 import (
    part1,
    read_file,
    is_rotation_zero,
    number_of_full_rotations,
    pass_or_land_on_zero,
)


def test_read_file():
    lines = read_file("data/day1_part1_sample")
    assert lines == ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]


def test_is_rotation_zero():
    zero_bool, final_pos = is_rotation_zero("L68", 50)
    assert zero_bool is False
    assert final_pos == 82
    zero_bool, final_pos = is_rotation_zero("L30", 82)
    assert zero_bool is False
    assert final_pos == 52
    zero_bool, final_pos = is_rotation_zero("R48", 52)
    assert zero_bool is True
    assert final_pos == 0
    zero_bool, final_pos = is_rotation_zero("L5", 0)
    assert zero_bool is False
    assert final_pos == 95
    zero_bool, final_pos = is_rotation_zero("R60", 95)
    assert zero_bool is False
    assert final_pos == 55
    zero_bool, final_pos = is_rotation_zero("L55", 55)
    assert zero_bool is True
    assert final_pos == 0
    zero_bool, final_pos = is_rotation_zero("L1", 0)
    assert zero_bool is False
    assert final_pos == 99
    zero_bool, final_pos = is_rotation_zero("L99", 99)
    assert zero_bool is True
    assert final_pos == 0
    zero_bool, final_pos = is_rotation_zero("R14", 0)
    assert zero_bool is False
    assert final_pos == 14
    zero_bool, final_pos = is_rotation_zero("L82", 14)
    assert zero_bool is False
    assert final_pos == 32

    zero_bool, final_pos = is_rotation_zero("L799", 99)
    assert zero_bool is True
    assert final_pos == 0


def test_part1():
    lines = read_file("data/day1_part1_sample")
    result = part1(lines)
    assert result == 3


def test_number_of_full_rotations():
    assert number_of_full_rotations("R100") == 1
    assert number_of_full_rotations("R141") == 1
    assert number_of_full_rotations("L131") == 1
    assert number_of_full_rotations("L7996") == 79
    assert number_of_full_rotations("R60") == 0


def test_pass_or_land_on_zero():
    assert pass_or_land_on_zero("L68", 50)
    assert not pass_or_land_on_zero("L30", 82)
    assert pass_or_land_on_zero("R48", 52)
    assert not pass_or_land_on_zero("L5", 0)
    assert pass_or_land_on_zero("R60", 95)
    assert pass_or_land_on_zero("L55", 55)
    assert not pass_or_land_on_zero("L1", 0)
    assert pass_or_land_on_zero("L99", 99)
    assert not pass_or_land_on_zero("R14", 0)
    assert pass_or_land_on_zero("L82", 14)
    assert not pass_or_land_on_zero(
        "L100", 0
    )  # Weird edge case. See comments in function.
    assert not pass_or_land_on_zero("L1000", 0)
