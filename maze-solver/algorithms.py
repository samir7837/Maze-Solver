from heapq import heappush, heappop

def get_neighbors(node, maze):
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    neighbors = []
    for dx, dy in directions:
        x, y = node[0]+dx, node[1]+dy
        if 0 <= x < maze.shape[0] and 0 <= y < maze.shape[1] and maze[x,y] == 0:
            neighbors.append((x,y))
    return neighbors


def bfs(maze, start, goal):
    from collections import deque
    queue = deque([start])
    came_from = {start: None}
    while queue:
        current = queue.popleft()
        if current == goal:
            break
        for n in get_neighbors(current, maze):
            if n not in came_from:
                queue.append(n)
                came_from[n] = current
    return reconstruct_path(came_from, start, goal)


def dfs(maze, start, goal):
    stack = [start]
    came_from = {start: None}
    while stack:
        current = stack.pop()
        if current == goal:
            break
        for n in get_neighbors(current, maze):
            if n not in came_from:
                stack.append(n)
                came_from[n] = current
    return reconstruct_path(came_from, start, goal)


def best_first(maze, start, goal):
    pq = []
    heappush(pq, (heuristic(start, goal), start))
    came_from = {start: None}
    while pq:
        _, current = heappop(pq)
        if current == goal:
            break
        for n in get_neighbors(current, maze):
            if n not in came_from:
                heappush(pq, (heuristic(n, goal), n))
                came_from[n] = current
    return reconstruct_path(came_from, start, goal)


def a_star(maze, start, goal):
    pq = []
    g_score = {start: 0}
    heappush(pq, (heuristic(start, goal), start))
    came_from = {start: None}
    while pq:
        _, current = heappop(pq)
        if current == goal:
            break
        for n in get_neighbors(current, maze):
            tentative_g = g_score[current] + 1
            if n not in g_score or tentative_g < g_score[n]:
                g_score[n] = tentative_g
                f_score = tentative_g + heuristic(n, goal)
                heappush(pq, (f_score, n))
                came_from[n] = current
    return reconstruct_path(came_from, start, goal)


def heuristic(a, b):
    # Manhattan distance
    return abs(a[0]-b[0]) + abs(a[1]-b[1])


def reconstruct_path(came_from, start, goal):
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = came_from.get(current)
    path.reverse()
    return path