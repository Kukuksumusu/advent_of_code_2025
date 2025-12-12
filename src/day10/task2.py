import numpy as np
import pulp  # type: ignore[import-untyped]


def solve_machine(joltage: list[int], buttons: list[tuple[int, ...]]) -> int:
    button_matrix = np.array([[1 if i in button else 0 for i in range(len(joltage))] for button in buttons]).T
    prob = pulp.LpProblem("Joltage_Problem", pulp.LpMinimize)

    x_vars = [pulp.LpVariable(f"button_{i}", lowBound=0, cat="Integer") for i in range(len(buttons))]
    prob += pulp.lpSum(x_vars)

    for i in range(len(joltage)):
        prob += pulp.lpSum(button_matrix[i, j] * x_vars[j] for j in range(len(buttons))) == joltage[i]

    prob.solve(pulp.PULP_CBC_CMD(msg=0))

    if prob.status != pulp.LpStatusOptimal:
        raise ValueError(f"No optimal solution found for joltage {joltage}")

    return sum(int(var.varValue) for var in x_vars)


def solve(input_data: str) -> int:
    lines = input_data.strip().splitlines()
    res = 0
    for machine in lines:
        _, *buttons_str, joltage_str = machine.split(" ")
        buttons = [tuple(int(x) for x in button[1:-1].split(",")) for button in buttons_str]
        joltage = [int(x) for x in joltage_str[1:-1].split(",")]
        res += solve_machine(joltage, buttons)

    return res
