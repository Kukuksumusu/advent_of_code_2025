def parse_input(input_data: str):
    return [tuple(map(int, r.split("-"))) for r in input_data.split(",")]


def is_invalid(number: int) -> bool:
    # this works because we can imagine the number as a "loop"
    # repeating the number twice adds the "pattern" at least twice again
    # so removing the first and last character removes at most 2 instances of the pattern
    # and the original number is still present (at least once)

    # if the number is not made of patterns removing the first and last character
    # will remove at least one number that was necessary to form the "single pattern"
    # of which the number is made of
    s = str(number)
    return s in (s + s)[1:-1]

    # this was my original "brute force" solution
    for seq_len in range(1, len(str(number)) // 2 + 1):
        seq = str(number)[:seq_len]
        for i in range(seq_len, len(str(number)), seq_len):
            if str(number)[i : i + seq_len] != seq:
                break
        else:
            return True
    return False


def solve(input_data: str) -> int:
    ranges = parse_input(input_data)
    res = 0
    for start, end in ranges:
        for i in range(start, end + 1):
            if is_invalid(i):
                res += i
    return res
