def get_joltage(bank: str) -> int:
    first_digit = 0
    second_digit = 0
    for i in range(len(bank)):
        digit = int(bank[i])
        if digit > first_digit and i < len(bank) - 1:
            first_digit = digit
            second_digit = int(bank[i + 1])
        elif digit > second_digit:
            second_digit = digit

    return first_digit * 10 + second_digit


def solve(input_data: str) -> int:
    banks = input_data.strip().splitlines()
    res = 0
    for bank in banks:
        res += get_joltage(bank)
    return res
