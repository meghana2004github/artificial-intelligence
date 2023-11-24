import heapq

class Node:
    def _init_(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def _lt_(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar(start, goal, neighbors, cost_func, heuristic_func):
    open_set = []
    closed_set = set()

    start_node = Node(state=start, cost=0, heuristic=heuristic_func(start, goal))
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal:
            path = []
            while current_node:
                path.insert(0, current_node.state)
                current_node = current_node.parent
            return path

        closed_set.add(current_node.state)

        for neighbor in neighbors(current_node.state):
            if neighbor in closed_set:
                co0ntinue

            cost_to_neighbor = current_node.cost + cost_func(current_node.state, neighbor)
            heuristic_to_goal = heuristic_func(neighbor, goal)
            total_cost = cost_to_neighbor + heuristic_to_goal

            neighbor_node = Node(state=neighbor, parent=current_node, cost=cost_to_neighbor, heuristic=heuristic_to_goal)

            if neighbor not in (node.state for node in open_set):
                heapq.heappush(open_set, neighbor_node)
            elif cost_to_neighbor < [node.cost for node in open_set if node.state == neighbor][0]:
                open_set.remove([node for node in open_set if node.state == neighbor][0])
                heapq.heappush(open_set, neighbor_node)

    return None  # If no path is found

# Example usage with user input:
def euclidean_distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def input_coordinates(prompt):
    x, y = map(float, input(prompt).split())
    return x, y

# Input start and goal coordinates
start = input_coordinates("Enter the start coordinates (x y): ")
goal = input_coordinates("Enter the goal coordinates (x y): ")

# Example neighbors function (move up, down, left, right)
def neighbors(state):
    x, y = state
    return [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

path = astar(start, goal, neighbors, euclidean_distance, euclidean_distance)

if path:
    print("A* Path:", path)
else:
    print("No path found.")
