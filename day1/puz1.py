from __future__ import annotations
from typing import Tuple
from pathlib import Path


def read_file(filename: str | Path) -> list[str]:
    with open(filename, "r") as f:
        lines = f.read().splitlines()
    return lines


def is_rotation_zero(s: str, starting_position: int) -> Tuple[bool, int]:
    direction = s[0]
    steps = int(s[1:])
    if direction == "R":
        final_position = (starting_position + steps) % 100
    elif direction == "L":
        final_position = (100 - abs(starting_position - steps)) % 100
        intermediate_position = starting_position - steps
        if intermediate_position >= 0:
            final_position = intermediate_position
    else:
        raise ValueError(f"Unknown direction: {direction}")

    if final_position == 0:
        return (True, final_position)
    else:
        return (False, final_position)


def part1(data: list[str]) -> int:
    """part1: Determine number of times a rotation ends on 0."""
    zero_count = 0
    current_position = 50

    for line in data:
        zero_bool, current_position = is_rotation_zero(line, current_position)
        if zero_bool:
            zero_count += 1

    return zero_count

def solve1(filename: str | Path) -> int:
    answer = part1(read_file(filename))
    return answer