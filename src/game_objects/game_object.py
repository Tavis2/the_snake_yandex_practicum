from globals import pygame, CELL_SIZE

class GameObject:
    color = (50,50,50)
    size = CELL_SIZE

    def __init__(self, cell_position_x, cell_position_y, screen):
        self.position_x = cell_position_x * CELL_SIZE
        self.position_y = cell_position_y *CELL_SIZE
        self.screen = screen

    def draw(self):
        pygame.draw.rect(
            self.screen,
            self.color,
            (self.position_x, self.position_y, self.size, self.size)
        )

    def get_position(self, ):
        return (self.position_x, self.position_y)
