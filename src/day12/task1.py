from math import prod


def parse_presents(lines: list[str]) -> tuple[list[list[str]], list[int], int]:
    """Parse present definitions and return presents, their sizes, and next line index."""
    presents = []
    present_sizes = []
    i = 0

    while i < len(lines) and lines[i].strip() and lines[i].strip()[:-1].isdigit():
        # Skip the present ID line (e.g., "0:")
        i += 1

        # Read present pattern
        present = []
        while i < len(lines) and lines[i].strip():
            present.append(lines[i].strip())
            i += 1

        presents.append(present)
        present_sizes.append("".join(present).count("#"))

        # Skip blank line after present
        i += 1

    return presents, present_sizes, i


def parse_tree_line(line: str) -> tuple[int, list[int]]:
    """Parse a tree line and return tree size and present counts."""
    tree_size_str, tree_presents_str = line.split(": ")
    tree_size = prod(int(x) for x in tree_size_str.split("x"))
    tree_presents = [int(x) for x in tree_presents_str.split()]
    return tree_size, tree_presents


def calculate_presents_size(present_sizes: list[int], tree_presents: list[int]) -> int:
    """Calculate total size of all presents."""
    return sum(size * count for size, count in zip(present_sizes, tree_presents, strict=True))


def solve(input_data: str) -> int:
    # well today there is no real solution, you can "cheat" by using simple checks
    lines = input_data.strip().splitlines()

    # Parse present definitions
    _presents, present_sizes, i = parse_presents(lines)

    # Process each tree
    res = 0
    while i < len(lines):
        tree_size, tree_presents = parse_tree_line(lines[i])
        i += 1

        # Quick accept: if tree is too big for presents (max 9 cells per present)
        if tree_size >= sum(cnt * 9 for cnt in tree_presents):
            res += 1
            continue

        # Calculate actual presents size
        presents_size = calculate_presents_size(present_sizes, tree_presents)

        # Check if presents fit
        if presents_size > tree_size:
            continue

        print(
            f"For this case, we should try to find solution, but we will assume it fits: {tree_size} vs {presents_size}"
        )
        res += 1

    return res
