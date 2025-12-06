import bisect


def solve(input_data: str) -> int:
    ranges_raw, _ = input_data.strip().split("\n\n")
    ranges: list[tuple[int, int]] = []

    for range_ in ranges_raw.splitlines():
        start, end = map(int, range_.split("-"))
        # print(f"{ranges}, inserting: {(start, end)}")

        next_range_index = bisect.bisect_left(ranges, start, key = lambda x: x[0])
        if next_range_index < len(ranges) and ranges[next_range_index] == (start, end):
            continue

        i = next_range_index
        while i > 0 and ranges[i-1][1] >= start:
            i -= 1
        merged_start = ranges[i][0] if i != next_range_index else start

        j = next_range_index
        while j < len(ranges) and ranges[j][0] <= end:
            j += 1
        merged_end = max(ranges[j - 1][1], end) if j > 0 else end

        ranges[i:j] = [(merged_start, merged_end)]

    # return ranges
    return sum(e - s + 1 for s,e in ranges)
