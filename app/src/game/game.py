"""Game logic controller."""

import pygame
from game_objects.apple import Apple
from game_objects.snake import Snake
from globals import CELL_SIZE, COLORS, HEIGHT, WIDTH


class Game:
    """Main game controller."""

    _KEY_MAP = {
        pygame.K_w: 'down',
        pygame.K_s: 'up',
        pygame.K_a: 'left',
        pygame.K_d: 'right',
    }

    def __init__(
        self,
        screen,
        player: Snake,
        apple: Apple,
        fps: int,
    ) -> None:
        """Initialize game state."""
        self.screen = screen
        self.player = player
        self.apple = apple
        self.fps = fps

        self.game_objects: list = []
        self.running = False
        self.game_over = False
        self.collision_position: tuple[int, int] | None = None

        self._move_interval = 1 / 3
        self._move_timer = 0.0

    def tick(self, time_delta: float) -> None:
        """Process one game tick."""
        self._handle_events()
        self._handle_input()
        self._update(time_delta)
        self._render()

    def _handle_events(self) -> None:
        """Handle pygame events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()

    def _handle_input(self) -> None:
        """Handle keyboard input."""
        if self.game_over:
            return

        keys = pygame.key.get_pressed()
        for key, direction in self._KEY_MAP.items():
            if keys[key]:
                self.player.set_direction(direction)
                break

    def _update(self, time_delta: float) -> None:
        """Update game state."""
        if self.game_over:
            return

        self._move_timer += time_delta
        if self._move_timer < self._move_interval:
            return

        self._move_timer -= self._move_interval
        self.player.move()

        if self.player.is_self_encountered():
            self.collision_position = self.player.get_head_position()
            self.game_over = True

        if self.apple.get_position() == self.player.get_head_position():
            self.player.eat_apple()
            self.apple.respawn(self.player)

    def _render(self) -> None:
        """Render game frame."""
        self._draw_background()
        self._draw_game_objects()
        self._draw_collision()
        self._draw_field()

    def _draw_background(self) -> None:
        """Draw background."""
        self.screen.fill(COLORS['background'])

    def _draw_field(self) -> None:
        """Draw grid."""
        for x in range(0, WIDTH, CELL_SIZE):
            pygame.draw.line(
                self.screen,
                COLORS['lines'],
                (x, 0),
                (x, HEIGHT),
            )
        for y in range(0, HEIGHT, CELL_SIZE):
            pygame.draw.line(
                self.screen,
                COLORS['lines'],
                (0, y),
                (WIDTH, y),
            )

    def _draw_game_objects(self) -> None:
        """Draw all game objects."""
        for obj in self.game_objects:
            obj.draw()

    def _draw_collision(self) -> None:
        """Draw collision cell."""
        if not self.collision_position:
            return

        x, y = self.collision_position
        pygame.draw.rect(
            self.screen,
            COLORS['collision'],
            (x, y, CELL_SIZE, CELL_SIZE),
        )

    def add_game_object(self, *objects) -> None:
        """Register drawable game objects."""
        self.game_objects.extend(objects)

    def start(self) -> None:
        """Start the game."""
        self.running = True

    def stop(self) -> None:
        """Stop the game."""
        self.running = False
