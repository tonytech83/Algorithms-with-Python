def dfs(node, graph, founded_salaries):
    # check if salary for current not is already founded, if not None return salary for current node
    if founded_salaries[node] is not None:
        return founded_salaries[node]
    # check if current node have children, if not return 1 as salary
    # save salary for current node in founded_salaries
    if len(graph[node]) == 0:
        founded_salaries[node] = 1
        return 1

    # node salary
    salary = 0

    for child in graph[node]:
        salary += dfs(child, graph, founded_salaries)

    # add current salary to founded_salaries
    founded_salaries[node] = salary
    return salary


nodes = int(input())

graph = []

for _ in range(nodes):
    line = input()
    children = []
    for idx, state in enumerate(line):
        if state == 'Y':
            children.append(idx)
    graph.append(children)

# cache the salary for already calculated nodes
founded_salaries = [None] * nodes

total_salary = 0

for node in range(nodes):
    salary = dfs(node, graph, founded_salaries)
    total_salary += salary

print(total_salary)
