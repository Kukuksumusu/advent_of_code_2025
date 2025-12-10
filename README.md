# Advent of Code 2025

My solutions for [Advent of Code 2025](https://adventofcode.com/2025) written in Python.

## Setup

This project uses [uv](https://docs.astral.sh/uv/) for dependency management and [just](https://github.com/casey/just) as a command runner.

```bash
uv sync
```

## Project Structure

```
src/
├── day01/
│   ├── task1.py          # Solution for part 1
│   ├── task2.py          # Solution for part 2
│   ├── task.txt          # Problem description
│   ├── input.txt         # Real puzzle input
│   ├── input_test.txt    # Test input from problem
│   └── expected_results.txt  # Expected results for test input
├── day02/
│   └── ...
└── ...
```

Each solution file must implement a `solve` function:

```python
def solve(input_data: str) -> int:
    ...
```

Optionally, the function can accept an `is_test` parameter to differentiate between test and real input:

```python
def solve(input_data: str, is_test: bool = False) -> int:
    if is_test:
        # Different behavior for test input
        ...
    ...
```

## Usage

### Running Solutions

```bash
just run <day> <task>
```

For example, to run Day 1, Part 2:
```bash
just run 1 2
```

The runner will:
1. Execute the solution against the test input
2. Validate the result against `expected_results.txt`
3. If the test passes, run against the real input

### Creating a New Day

```bash
just create <day>
```

This creates the full directory structure with template files for the specified day.

### Linting

```bash
just fix      # Auto-fix linting issues
```

### Setting Debug Defaults

```bash
just debug <day> <task>
```

Updates the VS Code launch configuration to default to the specified day and task.

## Expected Results Format

The `expected_results.txt` file uses a simple format:

```
# Comments start with #
task1=expected_value
task2=expected_value
```
