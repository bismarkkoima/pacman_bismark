# map.py
import pygame

TILE_SIZE = 32

# Example map grid (use 1, 2, 3... for different wall types, " " for open space)
tile_map = [
    "111111111111",
    "1          1",
    "1 22332233 1",
    "1          1",
    "111111111111"
]

# Load wall sprites
def load_wall_tiles():
    return {
        "1": pygame.image.load("assets/sprites/wall_block.png"),
        "2": pygame.image.load("assets/sprites/wall_corner.png"),
        "3": pygame.image.load("assets/sprites/wall_straight.png"),
        # add more types as needed
    }

# Draw the full map
def draw_map(screen, wall_tiles):
    for row_idx, row in enumerate(tile_map):
        for col_idx, cell in enumerate(row):
            if cell in wall_tiles:
                x = col_idx * TILE_SIZE
                y = row_idx * TILE_SIZE
                screen.blit(wall_tiles[cell], (x, y))
