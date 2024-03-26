def draw_regular_polygon(surface, color, ver_count, radius, position):
    n, r = ver_count, radius
    x, y = position
    pygame.draw.polygon(surface, color, [(x + r * sin(2 * pi * i / n), y + r * cos(2 * pi * i / n)) for i in range(n)])


root.fill(color_dict['BACKGROUND'])
# specific_tile = rand_tile_in_grid()
# #print(specific_tile)
grid_cord_dict = (terrain_update(gen_grid_cords_dict()))
# print_neighbour_tiles(grid_cord_dict, specific_tile[0], specific_tile[1])

draw_grid(grid_cord_dict)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    pygame.display.flip()

from math import sin, cos, pi
from random import randrange
import pygame









w, h = 800, 800
vertex_count = 6
width = 1

radio = 8

pygame.init()
root = pygame.display.set_mode((w, h))


def draw_grid(grid_dct):
    padding_w = w / 2
    padding_h = h / 2
    tile_ratio = radio * 2
    offset = radio

    for tile_cords, tile_obj in grid_dct.items():
        pos_x, pos_y = [int(num) for num in tile_cords.split('_')]
        if pos_y % 2 == 0:
            cord_x = pos_x * tile_ratio + offset
        else:
            cord_x = pos_x * tile_ratio
        cord_y = pos_y * tile_ratio

        draw_regular_polygon(root, tile_obj.color, vertex_count, radio,
                             (cord_x + padding_w, cord_y + padding_h))


''' draw specific random tile
def print_neighbour_tiles(tile_dict, x, y):
    sides = ('top_left', 'top_right', 'left', 'right', 'bottom_left', 'bottom_right')

    tile = tile_dict[f'{x}_{y}']
    neighbours = tile.get_neighbours()

    for en, neighbour in enumerate(neighbours):
        if neighbour is not None:
            neighbour_tile = tile_dict[f'{neighbour[0]}_{neighbour[1]}']
            print(f'Side: {sides[en]} '
                  f'X: {neighbour_tile.pos_x}  '
                  f'Y: {neighbour_tile.pos_y}  '
                  f'COLOR: {list(color_dict.keys())[list(color_dict.values()).index(neighbour_tile.color)]}')
        else:
            print(f'Side: {sides[en]} not in grid')


def rand_tile_in_grid() -> tuple:
    rand_tile = (randrange(-gridSize, gridSize), randrange(-gridSize, gridSize))
    while not in_map(rand_tile):
        rand_tile = (randrange(-gridSize, gridSize), randrange(-gridSize, gridSize))
    return rand_tile


'''

# create func for not near neighbours
# if not(any of not near neighbours are mountains) = make them lakes
## not near neighbours = get neighbours and their neighbours that are not in the neighours or tile list


