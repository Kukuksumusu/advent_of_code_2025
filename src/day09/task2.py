from itertools import combinations

from shapely import Polygon


def solve(input_data: str) -> int:
    tiles = [tuple(int(x) for x in line.split(",")) for line in input_data.strip().splitlines()]
    polygon = Polygon(tiles)
    largest_rectangle = 1
    for tile1, tile2 in combinations(tiles, 2):
        current_rectangle = (abs(tile1[0] - tile2[0]) + 1) * (abs(tile1[1] - tile2[1]) + 1)
        if current_rectangle < largest_rectangle:
            continue

        if polygon.covers(Polygon([tile1, (tile1[0], tile2[1]), tile2, (tile2[0], tile1[1])])):
            largest_rectangle = current_rectangle
    return largest_rectangle
