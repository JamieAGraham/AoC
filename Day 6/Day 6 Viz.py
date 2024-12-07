import os
from copy import deepcopy

# Directions: Up, Right, Down, Left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
arrow_to_dir = {'^': 0, '>': 1, 'v': 2, '<': 3}
dir_to_arrow = {0: '^', 1: '>', 2: 'v', 3: '<'}

def find_guard_position(grid):
    for r, row in enumerate(grid):
        for c, cell in enumerate(row):
            if cell in arrow_to_dir:
                return (r, c), arrow_to_dir[cell]

def simulate(grid, rows, cols, obstruction=None, visualize=False):
    guard_pos, direction = find_guard_position(grid)
    visited_states = set()
    visited_path = set()  # To track positions in the loop for visualization
    visited_states.add((guard_pos[0], guard_pos[1], direction))

    while True:
        r, c = guard_pos
        dr, dc = directions[direction]
        new_r, new_c = r + dr, c + dc

        # Check bounds
        if new_r < 0 or new_c < 0 or new_r >= rows or new_c >= cols:
            return False, visited_path  # Guard leaves the map

        # Apply obstruction if placed
        if obstruction and (new_r, new_c) == obstruction:
            grid[new_r][new_c] = '#'

        # Check for obstacle
        if grid[new_r][new_c] == '#':
            direction = (direction + 1) % 4  # Turn right
        else:
            guard_pos = (new_r, new_c)
            if (new_r, new_c, direction) in visited_states:
                visited_path.add((new_r, new_c))  # Add to loop visualization
                return True, visited_path  # Loop detected
            visited_states.add((new_r, new_c, direction))
            visited_path.add((new_r, new_c))

def save_visualization(grid, visited_path, obstruction, file_name):
    # Create a copy of the grid to modify for visualization
    visual_grid = deepcopy(grid)
    for r, c in visited_path:
        if visual_grid[r][c] == '.':
            visual_grid[r][c] = 'X'
    if obstruction:
        ob_r, ob_c = obstruction
        visual_grid[ob_r][ob_c] = 'O'

    with open(file_name, 'w') as f:
        f.write('\n'.join(''.join(row) for row in visual_grid))

def visualize_valid_loops(grid):
    rows, cols = len(grid), len(grid[0])
    original_grid = deepcopy(grid)
    valid_positions = 0
    output_dir = "Valid_Loops"

    # Create directory for output files
    os.makedirs(output_dir, exist_ok=True)

    loop_sizes = []  # To store sizes of all loops
    loop_details = []  # To store details of loops (size, obstruction, file_name)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '.' or (r, c) == find_guard_position(grid)[0]:
                continue  # Skip non-empty cells and guard's starting position

            # Place an obstruction and test
            loop_detected, visited_path = simulate(deepcopy(original_grid), rows, cols, obstruction=(r, c), visualize=True)
            if loop_detected:
                valid_positions += 1
                loop_size = len(visited_path)
                file_name = os.path.join(output_dir, f"loop_{r}_{c}.txt")
                save_visualization(original_grid, visited_path, (r, c), file_name)
                loop_sizes.append(loop_size)
                loop_details.append((loop_size, (r, c), file_name))

    # Identify longest and shortest loops
    longest_loop = max(loop_details, key=lambda x: x[0], default=None)
    shortest_loop = min(loop_details, key=lambda x: x[0], default=None)

    print(f"Total valid obstruction positions: {valid_positions}")
    if longest_loop:
        print(f"Longest loop: Size {longest_loop[0]}, Obstruction {longest_loop[1]}, File {longest_loop[2]}")
    if shortest_loop:
        print(f"Shortest loop: Size {shortest_loop[0]}, Obstruction {shortest_loop[1]}, File {shortest_loop[2]}")

# Input reading
with open('Day 6\\input.txt', 'r') as f:
    inp = [list(line.strip()) for line in f]

# Visualize valid loops and find longest/shortest
visualize_valid_loops(inp)
