"""Apple game object."""

import random


from game_objects.game_object import GameObject
from globals import CELL_SIZE, COLORS, HEIGHT, WIDTH


class Apple(GameObject):
    """Apple object."""

    color = COLORS['apple']

    def respawn(self, player) -> None:
        """Respawn apple avoiding snake body."""
        available_x = list(range(0, WIDTH, CELL_SIZE))
        available_y = list(range(0, HEIGHT, CELL_SIZE))

        for cell in player.get_position():
            if cell['x'] in available_x:
                available_x.remove(cell['x'])
            if cell['y'] in available_y:
                available_y.remove(cell['y'])

        self.position_x = random.choice(available_x)
        self.position_y = random.choice(available_y)
