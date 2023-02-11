from algorithms.astar import astar
from algorithms.random_prims import random_prims
from config import *
from utils import *


def main():
    run = True
    clock = pygame.time.Clock()

    _map = generate_map()

    to_place = "wall"
    start = None
    end = None

    started = False

    def full_render(render_map=_map):
        SCREEN.fill(GRID_COLOR)
        render_frame(render_map)
        pygame.display.update()

    while run:
        clock.tick(240)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: run = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    _map = generate_map()
                    start = None
                    end = None

                if event.key == pygame.K_s:
                    if not start:
                        to_place = "start"

                if event.key == pygame.K_e:
                    if not end:
                        to_place = "end"

                if event.key == pygame.K_r:
                    _map = random_prims(full_render, clock)
                    update_neighbours(_map)
                    
                if event.key == pygame.K_SPACE and not started:
                    to_place = None
                    started = True

                    update_neighbours(_map)
                    
                    _map = astar(lambda: full_render(_map), _map, start, end, clock)
                    started = False
                    start = None
                    end = None

            if pygame.mouse.get_pressed()[0] and to_place:  #LMB
                pos = pygame.mouse.get_pos()
                current_cell_i = (pos[0] // MAP_RES, pos[1] // MAP_RES)
                current_cell = _map[current_cell_i[0]][current_cell_i[1]]

                if current_cell.type == "empty":
                    current_cell.update_type(to_place)

                if to_place == "start":
                    start = current_cell
                elif to_place == "end":
                    end = current_cell

                if start or end: to_place = "wall"

            if pygame.mouse.get_pressed()[1] and to_place:  #MMB
                pos = pygame.mouse.get_pos()
                current_cell = (pos[0] // MAP_RES, pos[1] // MAP_RES)

                _map = flood_fill(current_cell, _map)

            if pygame.mouse.get_pressed()[2] and to_place:  #RMB
                pos = pygame.mouse.get_pos()
                current_cell = (pos[0] // MAP_RES, pos[1] // MAP_RES)

                _map[current_cell[0]][current_cell[1]].update_type("empty", by_pass=True)

        full_render(_map)

    pygame.quit()


if __name__ == "__main__":
    main()