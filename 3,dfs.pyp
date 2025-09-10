
from collections import deque

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]] 

moves = [(-1,0),(1,0),(0,-1),(0,1)]

def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_goal(state):
    return state == goal_state

def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def dfs(start, visited=set()):
    if is_goal(start):
        return [start]

    visited.add(str(start))

    for neighbor in get_neighbors(start):
        if str(neighbor) not in visited:
            path = dfs(neighbor, visited)
            if path:
                return [start] + path
    return None
start_state = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

print("DFS Solution Path:")
solution = dfs(start_state, set())
if solution:
    for step in solution:
        for row in step:
            print(row)
        print("------")
else:
    print("No solution found")
