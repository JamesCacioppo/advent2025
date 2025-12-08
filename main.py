from pathlib import Path

from day1 import solve1


def main() -> None:
    input_path = Path(__file__).parent / "data" / "day1.txt"
    part1_answer = solve1(input_path)
    print("Part 1:", part1_answer)


if __name__ == "__main__":
    main()
