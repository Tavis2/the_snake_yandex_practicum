from globals import pygame, CELL_SIZE

class GameObject:
    color = (50,50,50)
    size = CELL_SIZE

    def __init__(self, x, y, screen):
        self.position_x = x
        self.position_y = y
        self.screen = screen

    def draw(self):
        pygame.draw.rect(
            self.screen,
            self.color,
            (self.position_x, self.position_y, self.size, self.size)
        )

