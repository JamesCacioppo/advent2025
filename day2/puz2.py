from pathlib import Path


def read_file(filename: str | Path) -> list[str]:
    with open(filename, "r") as f:
        lines = f.read().split(",")
    return lines


def build_range(product_id_range: str) -> list[int]:
    """Takes a string range, eg 11-22, and produces a list of ints, eg [11, 12, ..., 22]"""
    start = int(product_id_range.split("-")[0])
    end = int(product_id_range.split("-")[1])

    product_ids = list()
    product_ids = [product_id for product_id in range(start, end + 1)]

    return product_ids


def check_product_id_for_pattern(product_id: int) -> bool:
    """Take an individual product ID and check for patterns where the first half of a string is equal to the second half.  Example: 1212"""

    product_id_string = str(product_id)
    length = len(product_id_string)

    if product_id_string[0 : length // 2] == product_id_string[length // 2 : length]:
        return True

    return False


def solve1(filename: str | Path) -> int:
    sum_ids = 0
    lines = read_file(filename)

    for line in lines:
        product_ids = build_range(line)

        for product_id in product_ids:
            if check_product_id_for_pattern(product_id):
                sum_ids += int(product_id)

    return sum_ids
