from collections import deque


goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  


moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_blank(state):
    """Find the position (i, j) of the blank (0)."""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_goal(state):
    """Check if the state is the goal."""
    return state == goal_state

def get_neighbors(state):
    """Generate all possible neighbor states."""
    neighbors = []
    x, y = find_blank(state)
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def dls(state, depth, visited):
    """Depth-Limited Search."""
    if is_goal(state):
        return [state]
    if depth == 0:
        return None

    visited.add(tuple(map(tuple, state)))

    for neighbor in get_neighbors(state):
        neighbor_key = tuple(map(tuple, neighbor))
        if neighbor_key not in visited:
            path = dls(neighbor, depth - 1, visited)
            if path:
                return [state] + path
    return None

def ids(start):
    """Iterative Deepening Search."""
    depth = 0
    while True:
        visited = set()
        path = dls(start, depth, visited)
        if path:
            return path
        depth += 1

def dfs(state, visited=None):
    """Depth-First Search."""
    if visited is None:
        visited = set()
    if is_goal(state):
        return [state]
    visited.add(tuple(map(tuple, state)))
    for neighbor in get_neighbors(state):
        neighbor_key = tuple(map(tuple, neighbor))
        if neighbor_key not in visited:
            path = dfs(neighbor, visited)
            if path:
                return [state] + path
    return None


# --- Start state ---
start_state = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

# --- Run DFS ---
print("=== DFS Solution Path ===")
solution = dfs(start_state)
if solution:
    for step in solution:
        for row in step:
            print(row)
        print("------")
else:
    print("No solution found using DFS.")

# --- Run IDS ---
print("\n=== IDS Solution Path ===")
solution = ids(start_state)
if solution:
    for step in solution:
        for row in step:
            print(row)
        print("------")
else:
    print("No solution found using IDS.")
