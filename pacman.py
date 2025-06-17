import pygame

TILE_SIZE = 32

class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 2
        self.rect = pygame.Rect(x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE)
        self.color = (255, 255, 0)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

    def update(self):
        pass  # Add collision or animation later

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, TILE_SIZE // 2)
