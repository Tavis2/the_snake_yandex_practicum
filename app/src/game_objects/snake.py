"""Snake game object."""

import pygame
from game_objects.game_object import GameObject
from globals import CELL_SIZE, COLORS, HEIGHT, WIDTH


class Snake(GameObject):
    """Snake player."""

    color = COLORS['snake']

    _OPPOSITE_DIRECTION = {
        'left': 'right',
        'right': 'left',
        'up': 'down',
        'down': 'up',
    }

    def __init__(
        self,
        x: int,
        y: int,
        screen,
        body_cell_amount: int,
    ) -> None:
        """Initialize snake."""
        super().__init__(x, y, screen)

        self.direction = 'up'
        self.body_cells: list[dict[str, int]] = []

        for i in range(1, body_cell_amount):
            self.body_cells.append(
                {
                    'x': (x + i) * CELL_SIZE,
                    'y': y * CELL_SIZE,
                }
            )

    def move(self) -> None:
        """Move snake."""
        self.body_cells.pop()
        self.body_cells.insert(
            0,
            {
                'x': self.position_x,
                'y': self.position_y,
            },
        )

        if self.direction == 'up':
            self.position_y = (
                self.position_y + CELL_SIZE
                if self.position_y + CELL_SIZE < HEIGHT
                else 0
            )
        elif self.direction == 'down':
            self.position_y = (
                self.position_y - CELL_SIZE
                if self.position_y - CELL_SIZE >= 0
                else HEIGHT
            )
        elif self.direction == 'left':
            self.position_x = (
                self.position_x - CELL_SIZE
                if self.position_x - CELL_SIZE >= 0
                else WIDTH
            )
        elif self.direction == 'right':
            self.position_x = (
                self.position_x + CELL_SIZE
                if self.position_x + CELL_SIZE < WIDTH
                else 0
            )

    def set_direction(self, direction: str) -> None:
        """Set snake direction."""
        if self._OPPOSITE_DIRECTION[self.direction] != direction:
            self.direction = direction

    def draw(self) -> None:
        """Draw snake."""
        super().draw()
        for cell in self.body_cells:
            pygame.draw.rect(
                self.screen,
                self.color,
                (cell['x'], cell['y'], self.size, self.size),
            )

    def eat_apple(self) -> None:
        """Increase snake length."""
        self.body_cells.insert(
            0,
            {
                'x': self.position_x,
                'y': self.position_y,
            },
        )

    def is_self_encountered(self) -> bool:
        """Check self collision."""
        head_x, head_y = self.get_head_position()
        return any(
            cell['x'] == head_x and cell['y'] == head_y
            for cell in self.body_cells[1:]
        )

    def get_head_position(self) -> tuple[int, int]:
        """Return head position."""
        return super().get_position()

    def get_position(self) -> list[dict[str, int]]:
        """Return all snake cells."""
        head_x, head_y = self.get_head_position()
        return [{'x': head_x, 'y': head_y}, *self.body_cells]
