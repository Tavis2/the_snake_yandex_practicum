from globals import pygame, random
from globals import colors, WIDTH, HEIGHT, CELL_SIZE    
from game_objects.game_object import GameObject

class Apple(GameObject):
    color = colors["apple"]

    def respawn(self,):
        x = random.randrange(0, WIDTH, CELL_SIZE)
        y = random.randrange(0, HEIGHT, CELL_SIZE)
        self.position_x = x
        self.position_y = y
        self.draw()

