from day1 import read_file
from pathlib import Path

def check_adjacent_places(row: int, column: int) -> bool:
    """Given a position, check all adjacent positions and return True if less than four are an @."""
    
    return True

def solve1(filename: str | Path) -> int:
    lines = read_file(filename)

    paper_rolls_array = []
    for line in lines:
        paper_rolls_array.append(list(line))

    total_accessible_rolls = 0
    for row in paper_rolls_array:
        for column in row:
            if paper_rolls_array[row][column] == "@":
                if check_adjacent_places(row, column):
                    total_accessible_rolls += 1
    
    return total_accessible_rolls