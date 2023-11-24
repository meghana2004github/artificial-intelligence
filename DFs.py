graph = {
    '5': ['3', '7'],
    '3': ['2', '4'],
    '7': ['8'],
    '2': [],
    '4': ['8'],
    '8': []
}

def dfs_with_goal(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = []

    visited.add(start)
    path.append(start)

    if start == goal:
        print(f"Goal state {goal} reached!")
        print("Path:", path)
        return

    for neighbour in graph[start]:
        if neighbour not in visited:
            dfs_with_goal(graph, neighbour, goal, visited, path)

    path.pop()

# Driver Code
start_state = '5'
goal_state = '7'
print(f"DFS from {start_state} to {goal_state}:")
dfs_with_goal(graph, start_state, goal_state)
