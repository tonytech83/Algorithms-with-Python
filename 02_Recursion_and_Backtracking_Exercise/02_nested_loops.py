def gen_loop(idx, array):
    # base case
    if idx >= len(array):
        print(*array, sep=" ")
        return
    for num in range(1, n + 1):
        array[idx] = num
        # recursion
        gen_loop(idx + 1, array)


n = int(input())
array = [0] * n

gen_loop(0, array)
