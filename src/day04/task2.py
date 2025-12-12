def is_free(x: int, y: int, grid: list[list[str]], queue: list[tuple[int, int]]) -> bool:
    neigbourhood = "".join(["".join(x_n[max(y - 1, 0) : y + 2]) for x_n in grid[max(x - 1, 0) : x + 2]])
    if res := str.count(neigbourhood, "@") <= 4:  # a roll is its own neighbour here...
        grid[x][y] = "."
        for x_n in range(max(x - 1, 0), min(x + 2, len(grid))):
            for y_n in range(max(y - 1, 0), min(y + 2, len(grid[x]))):
                if grid[x_n][y_n] == "@":
                    queue.append((x_n, y_n))
    return res


def solve(input_data: str) -> int:
    grid_raw = input_data.strip().splitlines()
    grid = [list(x) for x in grid_raw]
    queue = [(x, y) for x in range(len(grid)) for y in range(len(grid[x])) if grid[x][y] == "@"]
    res = 0
    while queue:
        x, y = queue.pop(0)
        if grid[x][y] == ".":
            continue
        if is_free(x, y, grid, queue):
            res += 1
    return res
