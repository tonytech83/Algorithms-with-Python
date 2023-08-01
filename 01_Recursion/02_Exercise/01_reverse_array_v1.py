# exam: 01. Reverse Array
# judge: https://judge.softuni.org/Contests/Compete/Index/3460#0

def reverse_array(array, reversed_array):
    # BASE CASE
    if not array:
        print(' '.join(reversed_array))
        return

    # Pre-action
    reversed_array.append(array.pop(-1))
    # Recursive call
    reverse_array(array, reversed_array)


array = [x for x in input().split(' ')]
reverse_array(array, [])
