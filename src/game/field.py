from globals import pygame, CELL_SIZE, WIDTH, HEIGHT, colors

def draw_field(screen):
    screen.fill(colors["background"])

    for x in range(-1, WIDTH, CELL_SIZE):
        pygame.draw.line(screen, colors["lines"], (x, 1), (x, HEIGHT), 3)
    for y in range(-1, HEIGHT, CELL_SIZE):
        pygame.draw.line(screen, colors["lines"], (1, y), (WIDTH, y), 3)