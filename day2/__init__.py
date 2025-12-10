"""advent2025.day1 package.

This package exposes `part1`, `part2`, and `solve` from `puz1.py` so
consumers can `from advent2025.day1 import part1, part2, solve`.
"""

from .puz2 import (
    build_range,
    read_file,
    check_product_id_for_pattern,
    solve1,
    check_product_id_for_alt_pattern,
    solve2,
)

__all__ = [
    "build_range",
    "read_file",
    "check_product_id_for_pattern",
    "solve1",
    "check_product_id_for_alt_pattern",
    "solve2",
]
