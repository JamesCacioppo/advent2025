from pathlib import Path
import typer

from day1 import solve1, solve2

app = typer.Typer()

@app.command()
def day1(input_file: str) -> None:
    input_path = Path(__file__).parent / "data" / input_file
    part1_answer = solve1(input_path)
    print("Part 1:", part1_answer)

    part2_answer = part1_answer + solve2(input_path)
    print("Part 2:", part2_answer)

if __name__ == "__main__":
    app()
