import pygame

TILE_SIZE = 32

def load_wall_tiles():
    wall_image = pygame.image.load("assets/sprites/wall_block.png")
    return {"1": wall_image}

def draw_map(screen, wall_tiles):
    # Simple map: 1s are walls
    map_data = [
        "1111111111",
        "1000000001",
        "1000000001",
        "1111111111"
    ]
    for row_idx, row in enumerate(map_data):
        for col_idx, tile in enumerate(row):
            if tile == "1":
                screen.blit(wall_tiles["1"], (col_idx * TILE_SIZE, row_idx * TILE_SIZE))
