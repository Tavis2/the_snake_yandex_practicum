"""Base game object."""

import pygame

from globals import CELL_SIZE


class GameObject:
    """Base drawable game object."""

    color = (50, 50, 50)
    size = CELL_SIZE

    def __init__(self, cell_x: int, cell_y: int, screen) -> None:
        """Initialize object position."""
        self.position_x = cell_x * CELL_SIZE
        self.position_y = cell_y * CELL_SIZE
        self.screen = screen

    def draw(self) -> None:
        """Draw object on screen."""
        pygame.draw.rect(
            self.screen,
            self.color,
            (self.position_x, self.position_y, self.size, self.size),
        )

    def get_position(self) -> tuple[int, int]:
        """Return object position."""
        return self.position_x, self.position_y
