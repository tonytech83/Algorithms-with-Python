def array_sum(numbers, index):
    if index == len(numbers) - 1:  # BASE CASE - Check is this is the bottom of our array
        return numbers[index]  # if True, then return sum of last element of our array

    return numbers[index] + array_sum(numbers, index + 1)  # sums the current element of aur array with rest of our array


# Define the array ( example: 1 2 3 4 )
numbers = [int(x) for x in input().split()]

print(array_sum(numbers, 0))
