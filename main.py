import pygame
from map import draw_map, load_wall_tiles
from pacman import Pacman
from utils import Pellet

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man Bismark")

clock = pygame.time.Clock()

wall_tiles = load_wall_tiles()
pellets = [Pellet(3, 2), Pellet(4, 2), Pellet(5, 2)]
player = Pacman(1, 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player.handle_input()
    player.update()

    screen.fill((0, 0, 0))
    draw_map(screen, wall_tiles)

    for pellet in pellets:
        if player.rect.colliderect(pellet.rect) and not pellet.eaten:
            pellet.eaten = True
        pellet.draw(screen)

    player.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
