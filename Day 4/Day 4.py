from typing import List

def get_grid_char(grid: List[List[str]], row: int, col: int) -> str:
    """Fetches the character from the grid at the specified position, or returns an empty string if out of bounds."""
    height, width = len(grid), len(grid[0])
    if 0 <= row < height and 0 <= col < width:
        return grid[row][col]
    return ''

def count_xmas_patterns(grid: List[List[str]], row: int, col: int) -> int:
    """Counts the occurrences of 'XMAS' patterns starting from the given cell."""
    if grid[row][col] != 'X':
        return 0

    directions = [
        (0, 1), (0, -1), (1, 0), (-1, 0), 
        (1, 1), (1, -1), (-1, 1), (-1, -1)
    ]
    pattern_count = 0

    for delta_row, delta_col in directions:
        current_row, current_col = row, col
        for i in range(3):
            current_row += delta_row
            current_col += delta_col
            if get_grid_char(grid, current_row, current_col) != 'MAS'[i]:
                break
        else:  # Executes if no break occurs
            pattern_count += 1

    return pattern_count

def is_xmas_cross(grid: List[List[str]], row: int, col: int) -> bool:
    """Checks if the specified cell is the center of an 'X-MAS' cross pattern."""
    if grid[row][col] != 'A':
        return False

    diag1 = get_grid_char(grid, row - 1, col - 1) + get_grid_char(grid, row + 1, col + 1)
    if diag1 not in {'MS', 'SM'}:
        return False

    diag2 = get_grid_char(grid, row + 1, col - 1) + get_grid_char(grid, row - 1, col + 1)
    if diag2 not in {'MS', 'SM'}:
        return False

    return True


def count_xmas_patterns_in_grid(grid: List[List[str]]) -> None:
    """Counts and prints the total occurrences of 'XMAS' and 'X-MAS' patterns in the grid."""
    height, width = len(grid), len(grid[0])

    # Part 1: Count "XMAS" patterns
    xmas_count = sum(
        count_xmas_patterns(grid, row, col) 
        for row in range(height) 
        for col in range(width)
    )
    print('Part 1: Total XMAS patterns:', xmas_count)

    # Part 2: Count "X-MAS" cross patterns
    xmas_cross_count = sum(
        is_xmas_cross(grid, row, col) 
        for row in range(1, height - 1) 
        for col in range(1, width - 1)
    )
    print('Part 2: Total X-MAS cross patterns:', xmas_cross_count)

def read_grid_from_file(file_path: str) -> List[List[str]]:
    """Reads the grid from a file."""
    with open(file_path, 'r') as file:
        return [list(line.strip()) for line in file]

if __name__ == '__main__':
    input_file_path = "Day 4\\input.txt"
    grid_data = read_grid_from_file(input_file_path)
    count_xmas_patterns_in_grid(grid_data)