TARGET_LEN = 12


def find_highest_digit(bank: str) -> tuple[int, int]:
    highest_index = 0
    highest_digit = 0
    for i in range(len(bank)):
        if int(bank[i]) > highest_digit:
            highest_digit = int(bank[i])
            highest_index = i
    return highest_digit, highest_index


def get_joltage(bank: str) -> int:
    res = 0
    for i in range(TARGET_LEN):
        end_index = -TARGET_LEN + i + 1
        highest_digit, highest_index = find_highest_digit(bank[:end_index] if end_index < 0 else bank)
        res += highest_digit * 10 ** (-end_index)
        bank = bank[highest_index + 1 :]
    return res


def solve(input_data: str) -> int:
    banks = input_data.strip().splitlines()
    res = 0
    for bank in banks:
        res += get_joltage(bank)
    return res
