from itertools import combinations


def solve_machine(lights: list[bool], buttons: list[tuple[int, ...]]) -> int:
    for i in range(1, len(buttons) + 1):
        # pressing the same button twice is pointless (it cancels out)
        # so we can just try all combinations (without repetition)
        for pressed_buttons in combinations(buttons, i):
            new_lights = lights[:]
            for button in pressed_buttons:
                for light in button:
                    new_lights[light] = not new_lights[light]
            if all(new_lights):
                return i
    raise ValueError("No solution found")


def solve(input_data: str) -> int:
    lines = input_data.strip().splitlines()
    res = 0
    for machine in lines:
        lights_str, *buttons_str, _ = machine.split(" ")
        lights = [x == "." for x in lights_str[1:-1]]
        buttons = [tuple(int(x) for x in button[1:-1].split(",")) for button in buttons_str]
        res += solve_machine(lights, buttons)

    return res