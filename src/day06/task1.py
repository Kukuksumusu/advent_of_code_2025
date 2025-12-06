from math import prod


def solve(input_data: str) -> int:
    lines_raw = input_data.strip().splitlines()
    numbers = [list(map(int, " ".join(x.split()).split(" "))) for x in lines_raw[:-1]]
    operations = " ".join(lines_raw[-1].split()).split(" ")

    res = 0
    for col in range(len(numbers[0])):
        if operations[col] == "+":
            res += sum(numbers[row][col] for row in range(len(numbers)))
        elif operations[col] == "*":
            res += prod(numbers[row][col] for row in range(len(numbers)))
    return res
