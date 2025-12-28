"""Entry point for the Snake game."""

import pygame

from game.game import Game
from game_objects.apple import Apple
from game_objects.snake import Snake
from globals import HEIGHT, WIDTH


def main() -> None:
    """Run the Snake game."""
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Snake')

    clock = pygame.time.Clock()
    fps = 60

    apple = Apple(8, 12, screen)
    snake = Snake(8, 9, screen, body_cell_amount=10)

    game = Game(screen, snake, apple, fps)
    game.add_game_object(apple, snake)
    game.start()

    while game.running:
        pygame.display.flip()
        time_delta = clock.tick(fps) / 1000
        game.tick(time_delta)

    pygame.quit()


if __name__ == '__main__':
    main()
