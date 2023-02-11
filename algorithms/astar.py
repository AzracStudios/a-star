from queue import PriorityQueue
from utils import *


def heuristic(p1, p2):
    # MANHATTAN DISTANCE
    x1, y1 = p1
    x2, y2 = p2
    return abs(x2 - x1) + abs(y2 - y1)


def astar(render, _map, start, end, clock):
    count = 0

    open_set = PriorityQueue()
    open_set.put((0, count, start))

    came_from = {}

    g_score = {cell: float("inf") for row in _map for cell in row}
    g_score[start] = 0

    f_score = {cell: float("inf") for row in _map for cell in row}
    f_score[start] = heuristic(start.position, end.position)

    open_set_hash = {start}

    while not open_set.empty():
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.get()[2]
        open_set_hash.remove(current)

        if current == end:
            reconstruct_path(came_from, current, render, clock)
            return _map

        for neighbour in current.neighbours:
            temp_g_score = g_score[current] + 1

            if temp_g_score < g_score[neighbour]:
                came_from[neighbour] = current
                
                g_score[neighbour] = temp_g_score
                f_score[neighbour] = temp_g_score + heuristic(
                    neighbour.position, end.position)

                if neighbour not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbour], count, neighbour))
                    open_set_hash.add(neighbour)
                    neighbour.update_type("open")

        render()

        if current != start:
            current.update_type("closed")

    return False
