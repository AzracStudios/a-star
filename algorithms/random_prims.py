from utils import *
import random


def random_prims(render, clock):
    _map = generate_map("wall")

    r_x = random.randrange(0, len(_map) - 1)
    r_y = random.randrange(0, len(_map[len(_map) - 1]) - 1)
    r_c = random.randrange(0, 1)

    if r_c:
        r_y = [0, len(_map[len(_map) - 1]) - 1][random.randrange(0, 1)]
    else:
        r_x = [0, len(_map) - 1][random.randrange(0, 1)]

    frontier = get_neighbours((len(_map) - 1, len(_map) - 1), _map, ignore_type="empty")

    _map[len(_map) - 1][len(_map) - 1].update_type("empty", True)
    render(render_map=_map)

    temp = ()
    same = 0

    while len(frontier) >= 1:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()

        rand_frontier = frontier[random.randrange(0, len(frontier))]
        rand_frontier_x, rand_frontier_y = rand_frontier.position[
            0], rand_frontier.position[1]

        if temp:
            _map[temp[0]][temp[1]].update_type("empty", True)

        frontier = get_neighbours((rand_frontier_x, rand_frontier_y),
                                  _map,
                                  ignore_type="empty", ignore_self=False)


        if (rand_frontier_x, rand_frontier_y) == temp:
            same += 1
        if same > 15:
            break

        temp = (rand_frontier_x, rand_frontier_y)
        render(render_map=_map)

    return _map
