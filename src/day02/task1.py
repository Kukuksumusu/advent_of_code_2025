def parse_input(input_data: str):
    return [tuple(map(int, r.split("-"))) for r in input_data.split(",")]


def solve(input_data: str) -> int:
    ranges = parse_input(input_data)
    res = 0
    for r in ranges:
        for i in range(r[0], r[1] + 1):
            if len(str(i)) % 2 == 0 and str(i)[: len(str(i)) // 2] == str(i)[len(str(i)) // 2 :]:
                res += i
    return res
