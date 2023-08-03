# exam: 01. Recursive Array Sum
# judge: https://judge.softuni.org/Contests/Compete/Index/3459#0

def calc_sum(numbers, idx):
    # BASE CASE - Check is this is the bottom of our array
    if idx == len(numbers) - 1:
        # if True, then return sum of last element of the array
        return numbers[idx]
    # sums the current element of the array with the sum of rest of the numbers in the array
    return numbers[idx] + calc_sum(numbers, idx + 1)


# Define the array ( example: [1, 2, 3, 4] )
numbers = [int(x) for x in input().split()]
print(calc_sum(numbers, 0))
