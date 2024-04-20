from heapq import heappop, heappush
from .functions.heurestic_function import heurestic_function
from .functions.height_mapping_function import height_mapping_function


class Node:
    def __init__(self):
        self.parent = None
        self.fedges = []

        self.f = float('inf')
        self.g = float('inf')
        self.h = 0

    def init_edges(self, grid, pos, size):
        x = pos // size
        y = pos % size
        for i in range(3):
            for j in range(3):
                new_x = x + i - 1
                new_y = y + j - 1
                if 0 <= new_x < size and 0 <= new_y < size and not (i == 1 and j == 1):
                    if i - 1 != 0 and j - 1 != 0:
                        edge = height_mapping_function(
                            grid[new_x][new_y] - grid[x][y], len(grid)) * 1.42
                    else:
                        edge = height_mapping_function(
                            grid[new_x][new_y] - grid[x][y], len(grid))
                    self.fedges.append((edge, new_x * size + new_y))
        self.fedges = sorted(self.fedges)


def find_path(goal, nodes, size):
    path = [(goal//size, goal % size)]
    parent = nodes[goal].parent
    while parent != None:
        path.append((parent//size, parent % size))
        parent = nodes[parent].parent

    cost = 0

    for i in range(len(path)):
        node = path[i][0] * size + path[i][1]
        for edge in nodes[node].fedges:
            if i + 1 < len(path) and path[i+1][0]*size + path[i+1][1] == edge[1]:
                cost += edge[0]

    return {'path': path, 'cost': cost}


def a_star(start_cord, goal_cord, grid, h_func=heurestic_function):
    size = len(grid)
    start = start_cord[0]*size + start_cord[1]
    goal = goal_cord[0] * size + goal_cord[1]
    closed_list = [False for i in range(size ** 2)]
    open_list = []
    nodes = [Node()
             for i in range(size ** 2)]

    nodes[start].g = 0
    heappush(open_list, (0, start))
    while len(open_list) != 0:
        _, p = heappop(open_list)
        nodes[p].init_edges(grid, p, size)
        g = nodes[p].g
        closed_list[p] = nodes[p].g + 1

        if goal == p:
            result = find_path(goal, nodes, size)
            result['closed'] = closed_list
            return result

        for edge in nodes[p].fedges:
            cost, np = edge
            if not closed_list[np]:
                new_g = cost + g
                h = h_func(grid, np, goal)
                new_f = h + new_g
                if nodes[np].f == float('inf') or nodes[np].f > new_f:
                    heappush(open_list, (new_f, np))
                    nodes[np].f = new_f
                    nodes[np].g = new_g
                    nodes[np].parent = p
    return False