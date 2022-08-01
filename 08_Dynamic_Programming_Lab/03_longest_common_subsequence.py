# Longest Common Subsequence -> LCS

first_str = input()
second_str = input()

# +1 because we add a base result for empty strings
rows = len(first_str) + 1
cols = len(second_str) + 1

# matrix generation with all base cases (all zeros)
result_matrix = []
[result_matrix.append([0] * cols) for _ in range(rows)]

for row in range(1, rows):
    for col in range(1, cols):
        # if we have coincidence, should add upper-left diagonal cell where we have the best result
        if first_str[row - 1] == second_str[col - 1]:
            result_matrix[row][col] = result_matrix[row - 1][col - 1] + 1
        # when we haven't coincidence, should check previous left or upper cell for best result
        else:
            result_matrix[row][col] = max(result_matrix[row - 1][col], result_matrix[row][col - 1])

print(result_matrix[rows - 1][cols - 1])
