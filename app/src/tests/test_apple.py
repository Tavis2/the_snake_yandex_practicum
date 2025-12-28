"""Tests for Apple."""

from game_objects.apple import Apple
from game_objects.snake import Snake
from globals import CELL_SIZE


class DummyScreen:
    """Mock screen object."""

    def fill(self, *_args, **_kwargs) -> None:
        """Apple function."""
        pass


def test_apple_respawn_not_on_snake() -> None:
    """Apple should not respawn on snake body."""
    screen = DummyScreen()

    snake = Snake(2, 2, screen, body_cell_amount=3)
    apple = Apple(0, 0, screen)

    apple.respawn(snake)

    apple_x, apple_y = apple.get_position()
    snake_cells = snake.get_position()

    assert {
        'x': apple_x,
        'y': apple_y,
    } not in snake_cells


def test_apple_position_multiple_of_cell_size() -> None:
    """Apple position should align to grid."""
    screen = DummyScreen()
    snake = Snake(1, 1, screen, body_cell_amount=2)
    apple = Apple(0, 0, screen)

    apple.respawn(snake)
    x, y = apple.get_position()

    assert x % CELL_SIZE == 0
    assert y % CELL_SIZE == 0
