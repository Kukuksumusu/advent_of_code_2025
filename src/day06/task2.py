from math import prod


def solve(input_data: str) -> int:
    lines_raw = input_data.strip().splitlines()
    numbers = lines_raw[:-1]
    operations = " ".join(lines_raw[-1].split()).split(" ")

    res = 0
    current_numbers: list[int] = []
    for col in range(len(numbers[0]) - 1, -1, -1):
        current_number = "".join(numbers[row][col] for row in range(len(numbers))).lstrip()
        if current_number != "":
            current_numbers.append(int(current_number))
        if current_number == "" or col == 0:
            operation = operations.pop()
            if operation == "+":
                res += sum(current_numbers)
            elif operation == "*":
                res += prod(current_numbers)
            current_numbers = []
    return res
