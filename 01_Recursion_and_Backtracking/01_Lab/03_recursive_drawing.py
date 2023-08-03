# exam: 03. Recursive Drawing
# judge: https://judge.softuni.org/Contests/Compete/Index/3459#2

def draw(n):
    # BASE CASE - where recursive calls should stop
    if n == 0:
        return

    # Pre-action: print n asteriks
    print('*' * n)

    # Recursive call
    draw(n - 1)

    # Post-action: print n hashtags
    print('#' * n)


draw(int(input()))
