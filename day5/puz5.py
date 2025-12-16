from day1 import read_file
from pathlib import Path

def read_input(filename: str | Path) -> list[str]:
    lines = read_file(filename)

    return lines


def split_input_list(lines: list[str]) -> tuple[list[range], list[int]]:
    blank_line = lines.index('')
   
    fresh = lines[:blank_line]
    fresh_ranges = []
    for item in fresh:
        first_and_last = item.split('-')
        fresh_ranges.append(range(int(first_and_last[0]), int(first_and_last[1])+1))
    
    ingredients = lines[blank_line+1:]
    integer_ingredients = [int(item) for item in ingredients]

    return (fresh_ranges, integer_ingredients)


def find_ingredient_in_fresh_list(ingredient: int, fresh_ranges: list[range]) -> bool:
    for fresh_range in fresh_ranges:
        if ingredient in fresh_range:
            return True
    
    return False


def solve1(filename: str | Path) -> int:
    lines = read_file(filename)

    fresh_ranges, integer_ingredients = split_input_list(lines)

    counter = 0
    for ingredient in integer_ingredients:
        if find_ingredient_in_fresh_list(ingredient, fresh_ranges):
            counter += 1

    return counter


def solve2(filename: str | Path) -> int:
    lines = read_file(filename)

    fresh_ranges, integer_ingredients = split_input_list(lines)

    for id_list in fresh_ranges:

