def gen_loop(idx, vector):
    if idx >= len(vector):
        print(*vector, sep=" ")
        return
    for num in range(1, n + 1):
        vector[idx] = num
        gen_loop(idx + 1, vector)


n = int(input())
vector = [0] * n

gen_loop(0, vector)
