def is_adjacent_to_symbols(grid, row, col, symbols):
    offsets = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dr, dc in offsets:
        adjacent_row, adjacent_col = row + dr, col + dc
        if 0 <= adjacent_row < len(grid) and 0 <= adjacent_col < len(grid[0]):
            if grid[adjacent_row][adjacent_col] in symbols:
                return True

    return False


def find_full_number(grid, row, col):
    number_str = grid[row][col]

    left_col = col
    while left_col > 0 and grid[row][left_col - 1].isdigit():
        left_col -= 1
        number_str = grid[row][left_col] + number_str

    right_col = col
    while right_col < len(grid[0]) - 1 and grid[row][right_col + 1].isdigit():
        right_col += 1
        number_str += grid[row][right_col]

    return int(number_str), left_col, right_col


def sum_adjacent_to_symbols(grid):
    total_sum = 0
    symbols = set()

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if not grid[row][col].isdigit() and grid[row][col] != ".":
                symbols.add(grid[row][col])

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col].isdigit() and is_adjacent_to_symbols(
                grid, row, col, symbols
            ):
                number, start_col, end_col = find_full_number(grid, row, col)
                total_sum += number
                for i in range(start_col, end_col + 1):
                    grid[row][i] = "."

    return total_sum


def main():
    with open("input01.txt", "r") as file:
        schematic = file.read().splitlines()
        grid = [list(row) for row in schematic]

    result = sum_adjacent_to_symbols(grid)
    print(result)


if __name__ == "__main__":
    main()
