# main.py
import pygame
from moviepy.editor import VideoFileClip
# Add at top
from map import load_wall_tiles, draw_map

# After video loading
wall_tiles = load_wall_tiles()

# In game loop, after drawing the background video
draw_map(screen, wall_tiles)
# At the top
from pacman import Pacman

# After loading wall tiles
pacman = Pacman(1, 1)  # start position at tile (1,1)

# Inside the game loop
pacman.handle_input()
pacman.update()
pacman.draw(screen)

from utils import Pellet

# --- Video Setup ---
clip = VideoFileClip("assets/video/bg.mp4").resize((800, 600))
video_frames = [pygame.image.frombuffer(frame.tobytes(), clip.size, 'RGB') 
                for frame in clip.iter_frames()]

# --- Pygame Setup ---
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man Bot Game")
clock = pygame.time.Clock()
fps = int(clip.fps)

frame_index = 0
running = True
pellets = []

# Generate pellets on open tiles (not walls)
from map import tile_map
for y, row in enumerate(tile_map):
    for x, char in enumerate(row):
        if char == " ":
            pellets.append(Pellet(x, y))

score = 0
font = pygame.font.SysFont(None, 36)

# --- Game Loop ---
while running:
    screen.blit(video_frames[frame_index], (0, 0))
    frame_index = (frame_index + 1) % len(video_frames)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()
    clock.tick(fps)

pygame.quit()
# Check for pellet collisions
for pellet in pellets:
    if not pellet.eaten and pacman.rect.colliderect(pellet.rect):
        pellet.eaten = True
        score += 10

# Draw pellets
for pellet in pellets:
    pellet.draw(screen)

# Draw score
score_text = font.render(f"Score: {score}", True, (255, 255, 0))
screen.blit(score_text, (10, 10))

