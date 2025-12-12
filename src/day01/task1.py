def solve(input_data: str) -> int:
    rotations = input_data.strip().splitlines()
    num = 50
    res = 0
    for rotation in rotations:
        direction = rotation[0]
        steps = int(rotation[1:])
        num = (num - steps) % 100 if direction == "L" else (num + steps) % 100
        if num == 0:
            res += 1
    return res
