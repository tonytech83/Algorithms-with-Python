# exam: 03. Salaries
# judge: https://judge.softuni.org/Contests/Compete/Index/3463#2

def dfs(employee, graph, salaries):
    # check if salary for current not is already founded, if not None return salary for current node
    if salaries[employee] is not None:
        return salaries[employee]

    # check if current node have children, if not return 1 as salary
    # save salary for current node in salaries array
    if len(graph[employee]) == 0:
        salaries[employee] = 1
        return 1

    # current employee salary when have childs
    salary = 0
    for child in graph[employee]:
        salary += dfs(child, graph, salaries)

    # add current salary to salaries array and return salary
    salaries[employee] = salary
    return salary


employees_count = int(input())
graph = []

for _ in range(employees_count):
    line = input()
    children = []
    for idx, state in enumerate(line):
        if state == 'Y':
            children.append(idx)

    graph.append(children)

# cache the salary for already calculated employees
salaries = [None] * employees_count
total_salary = 0

for employee in range(employees_count):
    current_salary = dfs(employee, graph, salaries)
    total_salary += current_salary

print(total_salary)
