from globals import pygame
from globals import colors, CELL_SIZE, WIDTH, HEIGHT
from game_objects.game_object import GameObject

class Snake(GameObject):
    color = colors["snake"]
    acting = False 
    direction = "up"
    
    body_cells = []

    __conter_direction ={
        "left":"right",
        "right":"left",
        "up":"down",
        "down":"up"
    }

    def __init__(self, x, y, screen, body_cell_amount):
        super().__init__(x, y, screen)
        self.body_cell_amount = body_cell_amount
        for i in range(1, body_cell_amount):
            self.body_cells.append({
                "x" : (x+i)*CELL_SIZE,
                "y" : y *CELL_SIZE
            })

    def move(self,):
        self.body_cells.pop()
        self.body_cells.insert(0, {
            "x" : self.position_x,
            "y" : self.position_y
        })
        match self.direction:
            case "up":
                if self.position_y + CELL_SIZE < HEIGHT: 
                    self.position_y += CELL_SIZE
                else: 
                    self.position_y = 0
                print("подвинулся ВВЕРХ", self.position_y)
            case "down":
                if self.position_y - CELL_SIZE >= 0: 
                    self.position_y -= CELL_SIZE
                else: 
                    self.position_y = HEIGHT
                print("подвинулся ВНИЗ", self.position_y)
            case "left":
                if self.position_x - CELL_SIZE >= 0: 
                    self.position_x -= CELL_SIZE
                else: 
                    self.position_x = WIDTH
                print("подвинулся ВЛЕВО",self.position_x)
            case "right":
                if self.position_x + CELL_SIZE < WIDTH: 
                    self.position_x += CELL_SIZE
                else: 
                    self.position_x = 0
                print("подвинулся ВПРАВО", self.position_x)
            case _:
                self.position_y += CELL_SIZE
                print("подвинулся")
        
    def set_direction(self, direction):
        if not self.__conter_direction[self.direction] == direction:
            self.direction = direction
    
    def draw(self,):
        super().draw()
        for cell in self.body_cells:
            pygame.draw.rect(
            self.screen,
            self.color,
            (cell["x"], cell["y"], self.size, self.size)
        )
    
    def eat_apple(self, ):
        
        self.body_cells.insert(0, {
            "x" : self.position_x,
            "y" : self.position_y
        })
    
    def is_self_encountered(self):
        head_x, head_y = self.get_head_position()

        for cell in self.body_cells[1:]:
            if cell["x"] == head_x and cell["y"] == head_y:
                return True

        return False

    
    def get_head_position(self,):
        return super().get_position()

    def get_position(self):
        head_position = super().get_position()
        cells = [{
            "x":head_position[0],
            "y":head_position[1]
        }]

        for cell in self.body_cells:
            cells.append(cell)
        
        return cells