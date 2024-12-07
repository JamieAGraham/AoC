with open('Day 6\\input.txt', 'r') as f:
    inp = [list(line.strip()) for line in f]

# Directions: Up, Right, Down, Left
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
arrow_to_dir = {'^': 0, '>': 1, 'v': 2, '<': 3}
dir_to_arrow = {0: '^', 1: '>', 2: 'v', 3: '<'}

# Find initial position and direction
rows, cols = len(inp), len(inp[0])
for r in range(rows):
    for c in range(cols):
        if inp[r][c] in arrow_to_dir:
            guard_pos = (r, c)
            direction = arrow_to_dir[inp[r][c]]

# Tracking visited positions
visited = set()
visited.add(guard_pos)

# Simulate guard movement
while True:
    r, c = guard_pos
    dr, dc = directions[direction]
    new_r, new_c = r + dr, c + dc

    if new_r < 0 or new_c < 0 or new_r >= rows or new_c >= cols:  # Out of bounds
        break

    if inp[new_r][new_c] == '#':  # Obstacle
        direction = (direction + 1) % 4  # Turn right
    else:  # Move forward
        guard_pos = (new_r, new_c)
        visited.add(guard_pos)

# Count distinct positions visited
print("Distinct positions visited:", len(visited))

# Generate final map
for r, c in visited:
    inp[r][c] = 'X'

with open('Day 6\\output.txt', 'w') as f:
    f.write('\n'.join(''.join(row) for row in inp))