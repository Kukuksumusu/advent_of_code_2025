run day task *args:
    @uv run run.py {{day}} {{task}} {{args}}

# Run only test input (e.g., just test-run 7 1)
test-run day task:
    @uv run run.py {{day}} {{task}} --test-only

fix *args:
    @uv run ruff check src --fix {{args}}
    @uv run ruff format src

check:
    @uv run ruff check src
    @uv run mypy src --explicit-package-bases

# Create a new day structure (e.g., just create 03)
create day:
    #!/usr/bin/env bash
    set -euo pipefail
    
    # Pad day number to 2 digits
    day_padded=$(printf "%02d" {{day}})
    day_dir="src/day${day_padded}"
    
    if [ -d "$day_dir" ]; then
        echo "Error: Directory $day_dir already exists"
        exit 1
    fi
    
    mkdir -p "$day_dir"
    
    # Create task1.py
    echo 'def solve(input_data: str) -> int:' > "$day_dir/task1.py"
    echo '    # TODO: Implement solution' >> "$day_dir/task1.py"
    echo '    raise NotImplementedError("Solution not yet implemented")' >> "$day_dir/task1.py"
    
    # Create task2.py
    echo 'def solve(input_data: str) -> int:' > "$day_dir/task2.py"
    echo '    # TODO: Implement solution' >> "$day_dir/task2.py"
    echo '    raise NotImplementedError("Solution not yet implemented")' >> "$day_dir/task2.py"
    
    # Create empty files
    touch "$day_dir/task.txt"
    touch "$day_dir/input.txt"
    touch "$day_dir/input_test.txt"
    
    # Create expected_results.txt with template
    echo '# Expected results for test input' > "$day_dir/expected_results.txt"
    echo '# Format: task1=VALUE, task2=VALUE (one per line, or both on same line)' >> "$day_dir/expected_results.txt"
    echo 'task1=' >> "$day_dir/expected_results.txt"
    echo 'task2=' >> "$day_dir/expected_results.txt"
    
    echo "Created day $day_padded structure at $day_dir"
    
    # Update debug defaults
    just debug {{day}}

# Set debug defaults (e.g., just debug 03 2)
debug day task="1":
    @python3 scripts/update_launch_default.py {{day}} {{task}}
