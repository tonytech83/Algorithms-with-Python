# exam: 01. Binary Search
# judge: https://judge.softuni.org/Contests/Compete/Index/3461#0

def find_index(left_idx, right_idx, target, numbers):
    if left_idx > right_idx:
        return -1

    mid_idx = (left_idx + right_idx) // 2
    mid_el = numbers[mid_idx]

    if target == mid_el:
        return mid_idx

    if target > mid_el:
        return find_index(mid_idx + 1, right_idx, target, numbers)
    else:
        return find_index(left_idx, mid_idx - 1, target, numbers)


collection = [int(x) for x in input().split()]
target_num = int(input())

print(find_index(0, len(collection) - 1, target_num, collection))
