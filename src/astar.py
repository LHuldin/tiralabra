import heapq

def astar(start, goal, walkable_tiles):
    """
    A* pathfinding.
    start, goal: (x, y)
    walkable_tiles: set of (x, y)
    Returns: list of (x, y) positions from start to goal.
    """
    open_list = [(0, start)]
    came_from = {}
    g_score = {start: 0}

    while open_list:
        _, current = heapq.heappop(open_list)

        if current == goal:
            return build_path(came_from, current)

        for neighbor in neighbors(current, walkable_tiles):
            new_score = g_score[current] + 1
            if neighbor not in g_score or new_score < g_score[neighbor]:
                g_score[neighbor] = new_score
                priority = new_score + manhattan(neighbor, goal)
                heapq.heappush(open_list, (priority, neighbor))
                came_from[neighbor] = current

    return []

def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def neighbors(pos, walkable):
    steps = [(-1,0), (1,0), (0,-1), (0,1)]
    return [(pos[0]+dx, pos[1]+dy) for dx, dy in steps if (pos[0]+dx, pos[1]+dy) in walkable]

def build_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path