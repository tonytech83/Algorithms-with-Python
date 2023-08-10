"""
exam: 01. Numbers
judge: https://judge.softuni.org/Contests/Practice/Index/3623#0
"""


def find_sum_combinations(target_sum, current_sum, combination, current_num, results):
    if current_sum == target_sum:
        results.append(combination[:])
        return

    for num in range(current_num, 0, -1):
        if current_sum + num <= target_sum:
            combination.append(num)
            find_sum_combinations(target_sum, current_sum + num, combination, num, results)
            combination.pop()


n = int(input())
results = []
find_sum_combinations(n, 0, [], n, results)
[print(' + '.join(map(str, result))) for result in results]
