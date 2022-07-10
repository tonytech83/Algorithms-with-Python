def count_all_paths(row, col, rows, cols):
    # base case
    if row > rows - 1 or col > cols - 1:
        return 0
    if row == rows - 1 or col == cols - 1:
        return 1

    counter = 0
    counter += count_all_paths(row, col + 1, rows, cols)  # right
    counter += count_all_paths(row + 1, col, rows, cols)  # down

    return counter


rows = int(input())
cols = int(input())

print(count_all_paths(0, 0, rows, cols))
