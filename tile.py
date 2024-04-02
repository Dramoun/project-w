from random import randrange
from storage import TerrainColors


class Tile:
    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = (250, 100, 0)

        self._set_color()

    def _set_color(self):
        self.color = self._gen_hex_color()

    @staticmethod
    def _gen_hex_color():
        rand_num = randrange(0, 255)

        if rand_num < 190:
            return TerrainColors.LOW
        else:
            return TerrainColors.HIGH


if __name__ == "__main__":
    print("Running tile module")
