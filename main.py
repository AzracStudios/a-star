from algorithms.astar import astar
from algorithms.random_prims import random_prims
from config import *
from utils import *


def main():
    run = True
    clock = pygame.time.Clock()

    _map = generate_map()
    _map = update_neighbours(_map)

    to_place = "wall"
    start = None
    end = None

    started = False
    cache_pos = []
    cache_check = ()
    do = False

    def full_render(render_map):
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
                    _map = update_neighbours(_map)
                    
                if event.key == pygame.K_SPACE and not started:
                    to_place = None
                    started = True

                    _map = update_neighbours(_map)
                    
                    _ = astar(lambda: full_render(_map), _map, start, end, clock)
                    
                    if _:
                        _map = _

                    started = False

                    start = None
                    end = None

                if event.key == pygame.K_RETURN and not do:
                    do = True

                else:
                    do = False

            if pygame.mouse.get_pressed()[0] and to_place:  #LMB
                pos = pygame.mouse.get_pos()
                current_cell_i = (pos[0] // MAP_RES, pos[1] // MAP_RES)
                current_cell = _map[current_cell_i[0]][current_cell_i[1]]

                if current_cell.type == "empty":
                    current_cell.update_type(to_place)
                    current_cell.update_neighbours(get_neighbours(current_cell_i, _map, ignore_type="wall"))

                if to_place == "start":
                    start = current_cell
                elif to_place == "end":
                    end = current_cell

                if start or end: to_place = "wall"

            if pygame.mouse.get_pressed()[1] and to_place:  #MMB
                pos = pygame.mouse.get_pos()
                current_cell = (pos[0] // MAP_RES, pos[1] // MAP_RES)

                _map = flood_fill(current_cell, _map)
                _map = update_neighbours(_map)


            # if event.type == pygame.MOUSEMOTION and do: #DEBUG
            #     pos = pygame.mouse.get_pos()
            #     current_cell_i = (pos[0] // MAP_RES, pos[1] // MAP_RES)

            #     for x in _map[current_cell_i[0]][current_cell_i[1]].neighbours:
            #         n = x.position
            #         _map[n[0]][n[1]].update_type("closed")
                    
            #     print(_map[current_cell_i[0]][current_cell_i[1]].neighbours)

            #     if cache_check != current_cell_i:
            #         for m in cache_pos:
            #             for y in _map[m[0]][m[1]].neighbours:
            #                 n = y.position
            #                 _map[n[0]][n[1]].update_type("empty")
                
            #     cache_pos.clear()
            #     cache_pos.append(current_cell_i)
            #     cache_check = current_cell_i
            

            if pygame.mouse.get_pressed()[2] and to_place:  #RMB
                pos = pygame.mouse.get_pos()
                current_cell = (pos[0] // MAP_RES, pos[1] // MAP_RES)

                _map[current_cell[0]][current_cell[1]].update_type("empty", by_pass=True)
                _map[current_cell[0]][current_cell[1]].neighbours = get_neighbours(current_cell_i, _map, ignore_type="wall")


        full_render(_map)

    pygame.quit()


if __name__ == "__main__":
    main()