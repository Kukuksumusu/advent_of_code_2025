def is_free(x: int, y: int, grid: list[str]) -> bool:
    neigbourhood = "".join([x[max(y - 1, 0) : y + 2] for x in grid[max(x - 1, 0) : x + 2]])
    return str.count(neigbourhood, "@") <= 4  # a roll is its own neighbour here...


def solve(input_data: str) -> int:
    grid = input_data.strip().splitlines()
    res = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] == ".":
                continue
            if grid[x][y] == "@":
                res += 1 if is_free(x, y, grid) else 0
    return res
