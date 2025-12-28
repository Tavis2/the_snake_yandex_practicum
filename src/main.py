from globals import *
from game.game import Game  
from game_objects.game_object import  GameObject
from game_objects.apple import Apple
from game_objects.snake import Snake


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("")
clock = pygame.time.Clock()

FPS = 60
running = True
frame_counting = 0

apple = Apple(8, 12, screen)
go = GameObject(1, 1, screen)
snake = Snake(8, 9, screen, 10)

game = Game(screen, snake, apple, FPS)
game.start()

game.add_game_object(apple, go, snake)

while game.running:

    pygame.display.update()
    pygame.display.flip()

    time_delta = clock.tick(FPS) / 1000 
    game.tick(time_delta)

time.sleep(1)
pygame.quit()