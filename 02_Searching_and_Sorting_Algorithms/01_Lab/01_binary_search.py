# exam: 01. Binary Search
# judge: https://judge.softuni.org/Contests/Compete/Index/3461#0

def find_index(target, numbers):
    # Pointers
    left_idx = 0
    right_idx = len(numbers) - 1

    while True:
        # search while pointers are on same index -> we have only one element
        # or left and right pointers switched -> we don't have more elements
        if left_idx > right_idx:
            print(-1)
            return

        mid_idx = (left_idx + right_idx) // 2
        mid_el = numbers[mid_idx]

        # if we found the searched number -> return the index of element
        if target == mid_el:
            print(mid_idx)
            return

        # if target number is bigger than middle element
        # move left pointer to next element from middle element
        if target > mid_el:
            left_idx = mid_idx + 1
        # if target number is smaller than middle element
        # move right pointer to previous element from middle element
        else:
            right_idx = mid_idx - 1


collection = [int(x) for x in input().split()]
target_num = int(input())

find_index(target_num, collection)
