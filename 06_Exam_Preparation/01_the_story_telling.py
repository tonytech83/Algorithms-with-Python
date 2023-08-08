# Topological sorting with DFS and dictionary

from collections import deque


def dfs(story, stories, visited, result):
    if story in visited:
        return

    visited.add(story)

    for post_story in stories[story]:
        dfs(post_story, stories, visited, result)

    result.appendleft(story)


stories = {}

while True:
    story_data = input()
    if story_data == 'End':
        break

    pre_story, post_stories = story_data.split(' ->')
    if pre_story not in stories:
        stories[pre_story] = []

    stories[pre_story] = post_stories.lstrip().split()

visited = set()
result = deque()

for story in stories:
    dfs(story, stories, visited, result)

print(*result, sep=' ')
