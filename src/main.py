from globals import *
from game.field import draw_field  
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

apple = Apple(60, 60, screen)
go = GameObject(30, 30, screen)
snake = Snake(390, 480, screen)

while running:
    frame_counting += 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

    draw_field(screen)

    
    go.draw()
    apple.draw()
    snake.draw()

    if frame_counting >= FPS:
        frame_counting = 0 
        snake.move(FPS, "down")

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()