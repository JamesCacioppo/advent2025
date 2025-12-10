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
