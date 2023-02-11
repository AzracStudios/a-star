from utils import *
import random


def random_prims(render, clock):
    _map = generate_map("wall")

    _map[len(_map) - 1][len(_map[len(_map) - 1]) - 1].update_type(
        "empty", True)

    render(render_map=_map)

    frontier = get_neighbours((len(_map) - 1, len(_map[len(_map) - 1]) - 1),
                              _map,
                              ignore_type="empty")

    temp = ()
    same = 0

    while len(frontier) >= 1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()

        rand_frontier = frontier[random.randrange(0, len(frontier))]
        rand_frontier_x, rand_frontier_y = rand_frontier.position[
            0], rand_frontier.position[1]

        _map[rand_frontier_x][rand_frontier_y].update_type("closed", True)

        if temp:
            _map[temp[0]][temp[1]].update_type("empty", True)

        frontier = get_neighbours((rand_frontier_x, rand_frontier_y),
                                  _map,
                                  ignore_type="empty")

        if (rand_frontier_x, rand_frontier_y) == temp:
            same += 1
        if same > 5:
            break

        temp = (rand_frontier_x, rand_frontier_y)
        render(render_map=_map)

    return _map
