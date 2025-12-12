def handle_row(field: list[list[str]]) -> tuple[list[list[str]], int]:
    """Process the top row of the field and propagate 'S' (ray) markers downward and count the splits.

    Args:
        field: A 2D grid represented as a list of lists of single-character
            strings. Must have at least 2 rows.

    Returns:
        A tuple containing:
            - The field with the first row removed (field[1:]).
            - The number of splits encountered (count of '^' cells below 'S').
    """
    width = len(field[0])
    split_count = 0
    for i in range(width):
        if field[0][i] == "S":
            if field[1][i] == "^":
                split_count += 1
                if i > 0 and field[1][i - 1] == ".":
                    field[1][i - 1] = "S"
                if i < width - 1 and field[1][i + 1] == ".":
                    field[1][i + 1] = "S"
            elif field[1][i] == ".":
                field[1][i] = "S"
    return field[1:], split_count


def solve(input_data: str) -> int:
    field = [list(x) for x in input_data.strip().splitlines()]
    res = 0
    while len(field) > 1:
        field, splits = handle_row(field)
        # print(splits)
        res += splits
        # for i in field:
        #     print(i)
        # print("-----")
    return res
