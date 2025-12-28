"""Tests for Snake."""

from game_objects.snake import Snake


class DummyScreen:
    """Mock screen object."""

    def fill(self, *_args, **_kwargs) -> None:
        """Snake method."""
        pass


def test_snake_initial_length() -> None:
    """Snake should initialize with correct body length."""
    screen = DummyScreen()
    snake = Snake(5, 5, screen, body_cell_amount=4)

    assert len(snake.body_cells) == 3


def test_snake_direction_change() -> None:
    """Snake should not be able to reverse direction."""
    screen = DummyScreen()
    snake = Snake(5, 5, screen, body_cell_amount=3)

    # разрешённый поворот
    snake.set_direction('left')
    assert snake.direction == 'left'

    # запрещённый разворот
    snake.set_direction('right')
    assert snake.direction == 'left'


def test_snake_eat_apple() -> None:
    """Eating apple increases snake length."""
    screen = DummyScreen()
    snake = Snake(5, 5, screen, body_cell_amount=3)

    initial_length = len(snake.body_cells)
    snake.eat_apple()

    assert len(snake.body_cells) == initial_length + 1
