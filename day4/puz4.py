from day1 import read_file
from pathlib import Path


def check_adjacent_places(
    row: int, column: int, paper_rolls_array: list[list[str]]
) -> bool:
    """Given a position, check all adjacent positions and return True if less than four are an @."""
    roll_counter = 0
    y_max = len(paper_rolls_array) - 1
    x_max = len(paper_rolls_array[0]) - 1

    for y in range(
        row - 1, row + 2
    ):  # Add two to max because range stops 1 short of the second argument
        for x in range(column - 1, column + 2):
            if y < 0 or y > y_max:
                continue
            if x < 0 or x > x_max:
                continue
            if y == row and x == column:
                continue
            if paper_rolls_array[y][x] == "@":
                roll_counter += 1

    if roll_counter < 4:
        return True
    else:
        return False


def build_rolls_array(lines: list[str]) -> list[list[str]]:
    paper_rolls_array = []
    for line in lines:
        paper_rolls_array.append(list(line))

    return paper_rolls_array


def solve1(filename: str | Path) -> int:
    lines = read_file(filename)

    paper_rolls_array = build_rolls_array(lines)
    total_accessible_rolls = 0
    number_of_rows = len(paper_rolls_array)
    number_of_columns = len(paper_rolls_array[0])

    for row in range(number_of_rows):
        for column in range(number_of_columns):
            if paper_rolls_array[row][column] == "@":
                if check_adjacent_places(row, column, paper_rolls_array):
                    total_accessible_rolls += 1

    return total_accessible_rolls


def solve2(filename: str | Path) -> int:
    """Determine the total number of roles that can be removed."""

    lines = read_file(filename)

    paper_rolls_array = build_rolls_array(lines)
    total_rolls_removed = 0
    number_of_rows = len(paper_rolls_array)
    number_of_columns = len(paper_rolls_array[0])

    rolls_to_be_removed: list[tuple[int, int]] = [(1, 1)]

    while len(rolls_to_be_removed) > 0:
        rolls_to_be_removed = []
        for row in range(number_of_rows):
            for column in range(number_of_columns):
                if paper_rolls_array[row][column] == "@":
                    if check_adjacent_places(row, column, paper_rolls_array):
                        rolls_to_be_removed.append((row, column))

        total_rolls_removed += len(rolls_to_be_removed)

        for roll_to_be_removed in rolls_to_be_removed:
            row = roll_to_be_removed[0]
            column = roll_to_be_removed[1]
            paper_rolls_array[row][column] = "."

    return total_rolls_removed
