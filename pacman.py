# pacman.py
import pygame

TILE_SIZE = 32

class Pacman:
    def __init__(self, x, y):
        self.image = pygame.image.load("assets/sprites/pacman.png")
        self.rect = self.image.get_rect(topleft=(x * TILE_SIZE, y * TILE_SIZE))
        self.direction = pygame.Vector2(0, 0)
        self.speed = 2  # adjust speed as needed

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction = pygame.Vector2(0, -1)
        elif keys[pygame.K_DOWN]:
            self.direction = pygame.Vector2(0, 1)
        elif keys[pygame.K_LEFT]:
            self.direction = pygame.Vector2(-1, 0)
        elif keys[pygame.K_RIGHT]:
            self.direction = pygame.Vector2(1, 0)

    def update(self):
        self.rect.x += self.direction.x * self.speed
        self.rect.y += self.direction.y * self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
