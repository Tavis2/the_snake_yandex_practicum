from globals import pygame
from globals import colors, CELL_SIZE    
from game_objects.game_object import GameObject

class Snake(GameObject):
    color = colors["snake"]
    acting = False 
    speed = 30

    def __init__(self, x, y, screen):
        super().__init__(x, y, screen)

    def move(self, FPS, direction):
        if FPS%self.speed == 0: 
            match direction:
                case "up":
                    print(self.position_y)
                    self.position_y += CELL_SIZE
                    print("подвинулся ВВЕРХ", self.position_y)
                case "down":
                    self.position_y -= CELL_SIZE
                    print("подвинулся ВНИЗ", self.position_y)
                case "left":
                    self.position_x -= CELL_SIZE
                    print("подвинулся ВЛЕВО",self.position_x)
                case "right":
                    self.position_x += CELL_SIZE
                    print("подвинулся ВПРАВО", self.position_x)
                case _:
                    self.position_y += CELL_SIZE
                    print("подвинулся")
        self.draw()
        