def binary_search(numbers, target_num):
    # pointers where we are searching
    left = 0
    right = len(numbers) - 1

    # search while pointers are on same index -> we have only one element
    # or left and right pointers switched -> we don't have more elements
    while left <= right:
        middle_idx = (left + right) // 2
        middle_element = numbers[middle_idx]

        # if we found the searched number -> return the index of element
        if middle_element == target_num:
            return middle_idx

        if target_num > middle_element:
            left = middle_idx + 1

        else:
            right = middle_idx - 1

    return -1


numbers = [int(x) for x in input().split()]
target_num = int(input())

print(binary_search(numbers, target_num))
