from globals import pygame, random
from globals import colors, WIDTH, HEIGHT, CELL_SIZE    
from game_objects.game_object import GameObject

class Apple(GameObject):
    color = colors["apple"]

    def respawn(self, player):
        available_x = list(range(0, WIDTH, CELL_SIZE))
        available_y = list(range(0, HEIGHT, CELL_SIZE))

        player_cells = player.get_position()

        for cell in player_cells:
            if cell["x"] in available_x: available_x.remove(cell["x"])
            if cell["y"] in available_y: available_y.remove(cell["y"])

        x = random.choice(available_x)
        y = random.choice(available_y)
        
        self.position_x = x
        self.position_y = y

