from itertools import combinations


def solve(input_data: str) -> int:
    tiles = [tuple(int(x) for x in line.split(",")) for line in input_data.strip().splitlines()]
    largest_rectangle = 1
    for tile1, tile2 in combinations(tiles, 2):
        largest_rectangle = max((abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1), largest_rectangle)
    return largest_rectangle
