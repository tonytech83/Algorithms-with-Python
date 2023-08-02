def found_paths_count(row, col, rows, cols):
    if row >= rows or col >= cols:
        return 0

    if row == rows - 1 and col == cols - 1:
        return 1

    result = 0

    result += found_paths_count(row + 1, col, rows, cols)  # down
    result += found_paths_count(row, col + 1, rows, cols)  # right

    return result


rows = int(input())
cols = int(input())

print(found_paths_count(0, 0, rows, cols))
