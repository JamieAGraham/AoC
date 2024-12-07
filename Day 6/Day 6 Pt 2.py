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

def simulate(grid, rows, cols, obstruction=None):
    guard_pos, direction = find_guard_position(grid)
    visited_states = set()
    visited_states.add((guard_pos[0], guard_pos[1], direction))

    while True:
        r, c = guard_pos
        dr, dc = directions[direction]
        new_r, new_c = r + dr, c + dc

        # Check bounds
        if new_r < 0 or new_c < 0 or new_r >= rows or new_c >= cols:
            return False  # Guard leaves the map

        # Apply obstruction if placed
        if obstruction and (new_r, new_c) == obstruction:
            grid[new_r][new_c] = '#'

        # Check for obstacle
        if grid[new_r][new_c] == '#':
            direction = (direction + 1) % 4  # Turn right
        else:
            guard_pos = (new_r, new_c)
            if (new_r, new_c, direction) in visited_states:
                return True  # Loop detected
            visited_states.add((new_r, new_c, direction))

def count_valid_obstructions(grid):
    rows, cols = len(grid), len(grid[0])
    original_grid = deepcopy(grid)
    valid_positions = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '.' or (r, c) == find_guard_position(grid)[0]:
                continue  # Skip non-empty cells and guard's starting position

            # Place an obstruction and test
            if simulate(deepcopy(original_grid), rows, cols, obstruction=(r, c)):
                valid_positions += 1

    return valid_positions

# Input reading
with open('Day 6\\input.txt', 'r') as f:
    inp = [list(line.strip()) for line in f]

# Count valid obstruction positions
print("Valid obstruction positions:", count_valid_obstructions(inp))
