from math import prod  # Import the prod function

def find_full_number(grid, row, col, direction):
    # Extracts the full number starting from a specific digit in a given direction (horizontal or vertical)
    number_str = ""
    if direction == "horizontal":
        left_col = col
        while left_col >= 0 and grid[row][left_col].isdigit():
            number_str = grid[row][left_col] + number_str
            left_col -= 1

        right_col = col + 1
        while right_col < len(grid[0]) and grid[row][right_col].isdigit():
            number_str += grid[row][right_col]
            right_col += 1

    elif direction == "vertical":
        up_row = row
        while up_row >= 0 and grid[up_row][col].isdigit():
            number_str = grid[up_row][col] + number_str
            up_row -= 1

        down_row = row + 1
        while down_row < len(grid) and grid[down_row][col].isdigit():
            number_str += grid[down_row][col]
            down_row += 1

    return int(number_str) if number_str else None

def is_gear(grid, row, col):
    if grid[row][col] != '*':
        return False, []

    adjacent_numbers = []
    # Check horizontally and vertically for adjacent numbers
    for dr, dc, direction in [(-1, 0, "vertical"), (1, 0, "vertical"), (0, -1, "horizontal"), (0, 1, "horizontal")]:
        adjacent_row, adjacent_col = row + dr, col + dc
        if 0 <= adjacent_row < len(grid) and 0 <= adjacent_col < len(grid[0]) and grid[adjacent_row][adjacent_col].isdigit():
            number = find_full_number(grid, adjacent_row, adjacent_col, direction)
            if number is not None:
                adjacent_numbers.append(number)

    # A gear must be adjacent to exactly two unique numbers
    return len(set(adjacent_numbers)) == 2, set(adjacent_numbers)

def sum_gear_ratios(grid):
    total_sum = 0
    visited_gears = set()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) not in visited_gears and grid[row][col] == '*':
                is_gear_result, numbers = is_gear(grid, row, col)
                if is_gear_result:
                    total_sum += numbers.pop() * numbers.pop()
                    visited_gears.add((row, col))

    return total_sum

def main():
    # Read the schematic from a file and process it
    with open("input01.txt", "r") as file:
        schematic = file.read().splitlines()
        grid = [list(row) for row in schematic]

    result = sum_gear_ratios(grid)
    print(result)

if __name__ == "__main__":
    main()
