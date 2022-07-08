def draw(n):
    if n == 0:
        return
    print("*" * n)
    draw(n - 1)
    print("#" * n)


n = int(input())
draw(n)
