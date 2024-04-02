from tile import Tile


class GridHandler:
    def __init__(self, grid_size):
        self.grid_size = grid_size

    def gen_grid_cords_dict(self) -> dict:
        cords_dict = {}

        for tx in range(-self.grid_size, self.grid_size + 1):
            for ty in range(-self.grid_size, self.grid_size + 1):
                if self._in_map((tx, ty)):
                    tile = Tile(tx, ty)
                    cords_dict[f'{tx}_{ty}'] = tile

        return cords_dict

    def _in_map(self, hexs: tuple):
        cube = self._even_row_to_cube(hexs)
        if (self.grid_size >= cube[0] >= -self.grid_size
                and self.grid_size >= cube[1] >= -self.grid_size
                and self.grid_size >= cube[2] >= -self.grid_size):
            return True
        return False

    @staticmethod
    def _even_row_to_cube(position: tuple):
        q = position[0] - (position[1] + (position[1] & 1)) / 2
        r = position[1]
        return q, r, -q - r

    def second_ring_neighbors(self, original_tile: tuple) -> list:
        original_neighbours = self.get_neighbours(original_tile)
        original_tiles_list = original_neighbours + [original_tile]

        second_ring_neighbors_list = []

        for tile in original_neighbours:
            if tile is not None:
                tile_neighbours = self.get_neighbours(tile)

                for neighbour in tile_neighbours:
                    if neighbour is not None and neighbour not in original_tiles_list:
                        second_ring_neighbors_list.append(neighbour)

        return second_ring_neighbors_list

    def get_neighbours(self, tile: tuple) -> list:
        neighbours = [self._top_left_neighbour(tile),
                      self._top_right_neighbour(tile),
                      self._left_neighbour(tile),
                      self._right_neighbour(tile),
                      self._bot_left_neighbour(tile),
                      self._bot_right_neighbour(tile)]

        return neighbours

    def _top_left_neighbour(self, tile: tuple):
        pos_x, pos_y = tile

        if pos_y % 2 == 0:
            neighbour_pos = (pos_x, pos_y - 1)
        else:
            neighbour_pos = (pos_x - 1, pos_y - 1)

        if self._in_map(neighbour_pos):
            return neighbour_pos
        return None

    def _top_right_neighbour(self, tile: tuple):
        pos_x, pos_y = tile

        if pos_y % 2 == 0:
            neighbour_pos = (pos_x + 1, pos_y - 1)
        else:
            neighbour_pos = (pos_x, pos_y - 1)

        if self._in_map(neighbour_pos):
            return neighbour_pos
        return None

    def _left_neighbour(self, tile: tuple):
        pos_x, pos_y = tile
        neighbour_pos = (pos_x - 1, pos_y)

        if self._in_map(neighbour_pos):
            return neighbour_pos
        return None

    def _right_neighbour(self, tile: tuple):
        pos_x, pos_y = tile
        neighbour_pos = (pos_x + 1, pos_y)

        if self._in_map(neighbour_pos):
            return neighbour_pos
        return None

    def _bot_left_neighbour(self, tile: tuple):
        pos_x, pos_y = tile

        if pos_y % 2 == 0:
            neighbour_pos = (pos_x, pos_y + 1)
        else:
            neighbour_pos = (pos_x - 1, pos_y + 1)

        if self._in_map(neighbour_pos):
            return neighbour_pos
        return None

    def _bot_right_neighbour(self, tile: tuple):
        pos_x, pos_y = tile

        if pos_y % 2 == 0:
            neighbour_pos = (pos_x + 1, pos_y + 1)
        else:
            neighbour_pos = (pos_x, pos_y + 1)

        if self._in_map(neighbour_pos):
            return neighbour_pos
        return None


if __name__ == "__main__":
    print("Running grid handler module")
