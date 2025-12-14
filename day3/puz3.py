from day1 import read_file
from pathlib import Path

"""
- find the highest number excluding the last number
- split the string after highest number
- find the highest number of the new string
"""


def find_joltage(batt_str: str) -> int:
    batt_list = list(batt_str)

    # Create a reverse sorted list after popping the last element
    # so that the first element of the sorted list is the highest
    # number excluding the last char from batt_str
    batt_list_sorted_pop_last = batt_list.copy()
    batt_list_sorted_pop_last.pop(len(batt_list) - 1)
    batt_list_sorted_pop_last.sort(reverse=True)

    highest_batt = (
        batt_list_sorted_pop_last[0],
        batt_str.find(batt_list_sorted_pop_last[0]),
    )

    remaining_batt_list = batt_list[highest_batt[1] + 1 :]
    remaining_batt_list_sorted = remaining_batt_list.copy()
    remaining_batt_list_sorted.sort(reverse=True)

    second_highest_batt = remaining_batt_list_sorted[0]

    joltage = highest_batt[0] + second_highest_batt

    return int(joltage)


def solve1(filename: str | Path) -> int:
    sum_joltages = 0
    lines = read_file(filename)

    for line in lines:
        sum_joltages += find_joltage(line)

    return sum_joltages


def find_highest_value(number_string: str) -> tuple[int, int]:
    """Accept a string of numbers and return highest number and position"""

    number_list = list(number_string)
    number_list.sort(reverse=True)

    return (int(number_list[0]), number_string.find(number_list[0]))


def find_twelve_char_joltage(number_string: str) -> int:
    """Accept a string of numbers and return highest 12 char value as an int"""

    number_list = list(number_string)

    character_count = 12
    joltage_list: list[str] = []
    while len(joltage_list) < 12:
        list_to_select_from = number_list[: len(number_list) - character_count + 1]
        ordered_list = list_to_select_from.copy()
        ordered_list.sort(reverse=True)
        joltage_list.append(ordered_list[0])

        position = list_to_select_from.index(ordered_list[0])
        number_list = number_list[position + 1 :]

        character_count -= 1

    joltage_string = ""
    joltage_string = "".join(joltage_list)

    return int(joltage_string)


def solve2(filename: str | Path) -> int:
    sum_joltages = 0
    lines = read_file(filename)

    for line in lines:
        sum_joltages += find_twelve_char_joltage(line)

    return sum_joltages
