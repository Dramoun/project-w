import pygame
from storage import TerrainColors
from gridhandler import GridHandler
from math import sin, cos, pi
from terrain import Terrain


class Game:
    def __init__(self):
        self._w = 1000
        self._h = 1000
        self._vertex_count = 6
        self._width = 1
        self._radio = 8
        self._grid_size = 30

        self._grid_handler = GridHandler(grid_size=self._grid_size)
        self._terrain = Terrain(grid_handler=self._grid_handler)

    @staticmethod
    def _draw_regular_polygon(surface, color, ver_count, radius, position):
        n, r = ver_count, radius
        x, y = position
        pygame.draw.polygon(surface, color,
                            [(x + r * sin(2 * pi * i / n), y + r * cos(2 * pi * i / n)) for i in range(n)])

    def _draw_grid(self, grid_dct, root):
        padding_w = self._w / 2
        padding_h = self._h / 2
        tile_ratio = self._radio * 2
        offset = self._radio

        for tile_cords, tile_obj in grid_dct.items():
            pos_x, pos_y = [int(num) for num in tile_cords.split('_')]
            if pos_y % 2 == 0:
                cord_x = pos_x * tile_ratio + offset
            else:
                cord_x = pos_x * tile_ratio
            cord_y = pos_y * tile_ratio

            self._draw_regular_polygon(root, tile_obj.color, self._vertex_count, self._radio,
                                       (cord_x + padding_w, cord_y + padding_h))

    def run(self):
        pygame.init()

        root = pygame.display.set_mode((self._w, self._h))
        root.fill(TerrainColors.BACKGROUND)

        grid_cord_dict = (self._terrain.update(self._grid_handler.gen_grid_cords_dict()))

        self._draw_grid(grid_cord_dict, root)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            pygame.display.flip()


if __name__ == "__main__":
    print("Running game module")
    game_one = Game()
    game_one.run()
