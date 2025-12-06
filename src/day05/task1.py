def solve(input_data: str) -> int:
    ranges_raw, items_raw = input_data.strip().split("\n\n")
    ranges = [tuple(map(int, r.split("-"))) for r in ranges_raw.splitlines()]
    items = [int(i) for i in items_raw.splitlines()]

    res = 0
    for item in items:
        if any(r[0] <= item <= r[1] for r in ranges):
            res += 1
    return res
