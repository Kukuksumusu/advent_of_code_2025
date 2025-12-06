#!/usr/bin/env python3
"""Update the default day and task in launch.json."""

import json
import sys
from pathlib import Path


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: update_launch_default.py <day> [task]")
        print("  day:  Day number (e.g., 1, 03)")
        print("  task: Task number, 1 or 2 (default: 1)")
        sys.exit(1)

    day = sys.argv[1]
    task = sys.argv[2] if len(sys.argv) == 3 else "1"

    if task not in ("1", "2"):
        print(f"Error: Task must be 1 or 2, got '{task}'")
        sys.exit(1)

    launch_json_path = Path(".vscode/launch.json")

    if not launch_json_path.exists():
        print(f"Warning: {launch_json_path} not found, skipping")
        return

    with open(launch_json_path) as f:
        data = json.load(f)

    for inp in data.get("inputs", []):
        if inp.get("id") == "day":
            inp["default"] = day
        if inp.get("id") == "task":
            inp["default"] = task

    with open(launch_json_path, "w") as f:
        json.dump(data, f, indent=4)
        f.write("\n")

    print(f"Debug defaults set to day {day}, task {task}")


if __name__ == "__main__":
    main()
