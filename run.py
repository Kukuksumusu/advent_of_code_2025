import argparse
import importlib.util
import inspect
import sys
from pathlib import Path


def parse_expected_results(file_path: Path) -> dict[str, str]:
    """Parse expected_results.txt file and return a dict mapping task names to expected values."""
    results: dict[str, str] = {}
    if not file_path.exists():
        return results

    for line in file_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()
            if value:  # Only add if value is not empty
                results[key] = value
    return results


def load_solution_module(solution_file: Path):
    """Load and return the solution module."""
    spec = importlib.util.spec_from_file_location("solution", solution_file)
    if spec is None or spec.loader is None:
        print(f"Error: Could not load module from {solution_file}")
        sys.exit(1)

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    if not hasattr(module, "solve"):
        print(f"Error: Solution file {solution_file} does not have a 'solve' function")
        sys.exit(1)

    return module


def run_solution(module, input_data: str, label: str, is_test: bool) -> str:
    """Run the solution and return the result as a string."""
    print(f"Running with {label} input...")

    # Check if solve accepts is_test parameter for backward compatibility
    sig = inspect.signature(module.solve)
    if "is_test" in sig.parameters:
        result = module.solve(input_data, is_test=is_test)
    else:
        result = module.solve(input_data)

    print(f"Result: {result}")
    return str(result)


def main():
    parser = argparse.ArgumentParser(description="Run Advent of Code solutions")
    parser.add_argument("day", type=int, help="Day number (1-25)")
    parser.add_argument("task", type=int, choices=[1, 2], help="Task number (1 or 2)")
    parser.add_argument(
        "-t", "--test-only", action="store_true", help="Run only test input, skip real input"
    )
    args = parser.parse_args()

    day_str = f"{args.day:02d}"
    day_dir = Path(f"src/day{day_str}")

    if not day_dir.exists():
        print(f"Error: Day {args.day} directory not found at {day_dir}")
        sys.exit(1)

    solution_file = day_dir / f"task{args.task}.py"
    if not solution_file.exists():
        print(f"Error: Solution file not found at {solution_file}")
        sys.exit(1)

    # Look for task-specific test input first, fallback to generic test input
    task_specific_test = day_dir / f"input_test{args.task}.txt"
    generic_test = day_dir / "input_test.txt"
    test_input_file = task_specific_test if task_specific_test.exists() else generic_test
    
    real_input_file = day_dir / "input.txt"
    expected_file = day_dir / "expected_results.txt"

    # Load the solution module
    module = load_solution_module(solution_file)

    print(f"Day {args.day}, Task {args.task}")
    print("=" * 40)

    # Step 1: Run with test input
    if not test_input_file.exists():
        print(f"Error: Test input file not found at {test_input_file}")
        sys.exit(1)

    test_input = test_input_file.read_text()
    test_result = run_solution(module, test_input, "test", is_test=True)

    # Step 2: Check against expected result
    expected_results = parse_expected_results(expected_file)
    task_key = f"task{args.task}"

    if task_key not in expected_results:
        print(f"\n⚠️  No expected result defined for {task_key} in {expected_file}")
        print("Skipping real input run. Please add expected result to continue.")
        sys.exit(0)

    expected_value = expected_results[task_key]

    if test_result != expected_value:
        print("\n❌ Test FAILED!")
        print(f"   Expected: {expected_value}")
        print(f"   Got:      {test_result}")
        print("\nSkipping real input run due to test failure.")
        sys.exit(1)

    print(f"\n✅ Test PASSED! (expected {expected_value})")

    if args.test_only:
        sys.exit(0)

    print("-" * 40)

    # Step 3: Run with real input
    if not real_input_file.exists():
        print(f"Error: Real input file not found at {real_input_file}")
        sys.exit(1)

    real_input = real_input_file.read_text()
    run_solution(module, real_input, "real", is_test=False)


if __name__ == "__main__":
    main()
