from storage import TerrainColors
from gridhandler import GridHandler


class Terrain(GridHandler):
    def __init__(self, grid_size):
        super().__init__(grid_size)

    def mountain_generation(self, tile_grid) -> dict:
        new_grid = dict()

        for tile in tile_grid.values():
            neighbour_mountain_count = 0

            if tile.color == TerrainColors.HIGH:
                neighbours = tile.get_neighbours()

                for neighbour in neighbours:
                    if neighbour is not None:
                        if tile_grid[f'{neighbour[0]}_{neighbour[1]}'].color == TerrainColors.HIGH:
                            neighbour_mountain_count += 1

            if neighbour_mountain_count > 0 or tile.color == TerrainColors.LOW:
                new_grid[f'{tile.pos_x}_{tile.pos_y}'] = tile
            else:
                new_tile = tile
                new_tile.color = TerrainColors.LOW
                new_grid[f'{tile.pos_x}_{tile.pos_y}'] = tile

        return new_grid

    def lake_generation(self, tile_grid) -> dict:
        new_grid = dict()

        for tile in tile_grid.values():
            if tile.color == TerrainColors.LOW:
                second_neighbours = second_ring_neighbors(tile_grid, tile.pos_x, tile.pos_y)
                first_neighbours = tile.get_neighbours()
                mountain_count = 0

                for first_neighbour in first_neighbours:
                    if first_neighbour is not None:
                        if tile_grid[f'{first_neighbour[0]}_{first_neighbour[1]}'].color == TerrainColors.HIGH:
                            mountain_count += 1

                for neighbour in second_neighbours:
                    if tile_grid[f'{neighbour[0]}_{neighbour[1]}'].color == TerrainColors.HIGH:
                        mountain_count += 1

                if mountain_count == 0:
                    rand_lake = randrange(0, 2)
                    if rand_lake == 0:
                        new_grid[f'{tile.pos_x}_{tile.pos_y}'] = tile
                    else:
                        tile.color = color_dict['LAKE']
                        new_grid[f'{tile.pos_x}_{tile.pos_y}'] = tile

                else:
                    new_grid[f'{tile.pos_x}_{tile.pos_y}'] = tile

            else:
                new_grid[f'{tile.pos_x}_{tile.pos_y}'] = tile

        return new_grid

