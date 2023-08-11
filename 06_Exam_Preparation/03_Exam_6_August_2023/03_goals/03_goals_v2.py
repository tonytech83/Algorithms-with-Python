"""
exam: 03. Goals
judge: https://judge.softuni.org/Contests/Practice/Index/4044#2
"""


def find_best_sequence(goals_list):
    best_sequence = [goals_list[0]]
    for match_goals in goals_list[1:]:
        if match_goals >= best_sequence[-1]:
            best_sequence.append(match_goals)

    return best_sequence


scored_goals = [int(x) for x in input().split(', ')]

matches_best_sequence = find_best_sequence(scored_goals)
print(*matches_best_sequence, sep=' ')
