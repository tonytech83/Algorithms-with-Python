# exam: 01. Reverse Array
# judge: https://judge.softuni.org/Contests/Compete/Index/3460#0

def reverse_array(idx, array):
    # BASE CASE
    if idx == len(array) // 2:
        return print(' '.join(array))

    # Pre-action
    array[idx], array[-idx - 1] = array[-idx - 1], array[idx]
    # Recursive call
    reverse_array(idx + 1, array)


array = [x for x in input().split(' ')]
reverse_array(0, array)
