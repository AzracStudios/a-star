from config import *

class Cell:
    def __init__(self, type, position):
        self.type = type
        self.position = position

        self.tile_color = ()
        self.tile = None

        self.update_type(self.type)
        self.update_tile()

        self.neighbours = []

    def __repr__(self):
        return self.type

    def update_tile(self):
        self.tile = pygame.Rect(
            self.position[0] * MAP_RES + 2 * GRID_LINE_WIDTH,
            self.position[1] * MAP_RES + 2 * GRID_LINE_WIDTH,
            MAP_RES - GRID_LINE_WIDTH, MAP_RES - GRID_LINE_WIDTH)

    def update_type(self, type, by_pass=False):
        if by_pass or self.type == "empty" or self.type == "open" or self.type == "closed":
            self.type = type 

            if type == "empty":
                self.tile_color = (255, 255, 255)

            elif type == "wall":
                self.tile_color = (20, 20, 20)

            elif type == "start":
                self.tile_color = (237, 153, 57)

            elif type == "end":
                self.tile_color = (57, 237, 222)

            elif type == "open":
                self.tile_color = (137, 237, 57)

            elif type == "closed":
                self.tile_color = (237, 57, 84)

            elif type == "path":
                self.tile_color = (219, 57, 237)

