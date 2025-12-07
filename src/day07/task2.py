def handle_row(field: list[list[int]]) -> list[list[int]]:
    """Process the top row of the field and propagate timeline counts downward.

    Args:
        field: A 2D grid where 0=empty, -1=splitter, and positive values
            represent the number of timelines passing through that cell.
            Must have at least 2 rows.

    Returns:
        The field with the first row removed and timeline counts propagated.
    """
    width = len(field[0])
    for i in range(width):
        current_value = field[0][i]
        if current_value >= 1:
            if field[1][i] == -1:
                if i > 0:
                    field[1][i-1] += current_value
                if i < width - 1:
                    field[1][i+1] += current_value
            else:
                field[1][i] += current_value
    return field[1:]

def solve(input_data: str) -> int:
    field = [[0 if i == "." else 1 if i == "S" else -1 for i in x] for x in input_data.strip().splitlines()]
    while len(field) > 1:
        field = handle_row(field)
        # for i in field:
        #     print("".join([str(x) if x != -1 else "^" for x in i]))
        # print("-----")
    return sum(field[0])
