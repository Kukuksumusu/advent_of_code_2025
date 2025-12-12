def solve(input_data: str) -> int:
    rotations = input_data.strip().splitlines()
    num = 50
    res = 0
    for rotation in rotations:
        direction = rotation[0]
        steps = int(rotation[1:])
        res += steps // 100
        steps %= 100
        if steps == 0:
            continue
        if direction == "L":
            new_number = (num - steps) % 100
            if num != 0 and (num < new_number or new_number == 0):
                res += 1
            num = new_number
        else:
            new_number = (num + steps) % 100
            if num != 0 and (num > new_number or new_number == 0):
                res += 1
            num = new_number
    return res
