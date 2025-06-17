# utils.py
import pygame

TILE_SIZE = 32

class Pellet:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/sprites/pellet.png")
        self.rect = self.image.get_rect(center=(x * TILE_SIZE + TILE_SIZE // 2, y * TILE_SIZE + TILE_SIZE // 2))
        self.eaten = False

    def draw(self, screen):
        if not self.eaten:
            screen.blit(self.image, self.rect.topleft)
