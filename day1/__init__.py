"""advent2025.day1 package.

This package exposes `part1`, `part2`, and `solve` from `puz1.py` so
consumers can `from advent2025.day1 import part1, part2, solve`.
"""

from .puz1 import (
    part1,
    read_file,
    is_rotation_zero,
    solve1,
    solve2,
    number_of_full_rotations,
    pass_or_land_on_zero,
)

__all__ = [
    "part1",
    "read_file",
    "is_rotation_zero",
    "solve1",
    "solve2",
    "number_of_full_rotations",
    "pass_or_land_on_zero",
]
