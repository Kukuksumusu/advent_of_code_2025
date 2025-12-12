from functools import cache


def solve(input_data: str) -> int:
    # assume the graph is acyclic
    connections = {k: v.split(" ") for line in input_data.strip().splitlines() for k, v in [line.split(": ")]}

    @cache
    def solve_node(node: str) -> int:
        if node == "out":
            return 1
        return sum(solve_node(neighbor) for neighbor in connections[node])

    return solve_node("you")
