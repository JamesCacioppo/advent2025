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


def solve1(filename: str | Path) -> int:
    lines = read_file(filename)

    paper_rolls_array = []
    for line in lines:
        paper_rolls_array.append(list(line))

    total_accessible_rolls = 0
    number_of_rows = len(paper_rolls_array)
    number_of_columns = len(paper_rolls_array[0])

    for row in range(number_of_rows):
        for column in range(number_of_columns):
            if paper_rolls_array[row][column] == "@":
                if check_adjacent_places(row, column, paper_rolls_array):
                    total_accessible_rolls += 1

    return total_accessible_rolls
