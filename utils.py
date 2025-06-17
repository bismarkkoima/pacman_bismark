import pygame

TILE_SIZE = 32

class Pellet:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x * TILE_SIZE + 12, y * TILE_SIZE + 12, 8, 8)
        self.eaten = False

    def draw(self, screen):
        if not self.eaten:
            pygame.draw.circle(screen, (255, 255, 255), self.rect.center, 4)
