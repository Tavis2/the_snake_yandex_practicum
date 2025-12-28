from globals import pygame, CELL_SIZE, WIDTH, HEIGHT, colors
from game_objects.apple import Apple
from game_objects.snake import Snake


class Game:
    running = False
    game_objects = []

    __key_interpretation = {
        pygame.K_w: "down",
        pygame.K_s: "up",
        pygame.K_a: "left",
        pygame.K_d: "right"
    }

    def __init__(self, screen, player: Snake, apple: Apple, FPS):
        self.screen = screen
        self.FPS = FPS

        self.apple = apple
        self.player = player

        # состояние игры
        self.game_over = False
        self.collision_position = None

        # тайминг движения
        self._move_interval = 1 / 3   # 3 движения в секунду
        self._move_timer = 0.0

    # <=== логика игры ===>
    def tick(self, time_delta):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()

        # ===== INPUT =====
        if not self.game_over:
            keys = pygame.key.get_pressed()
            for key_code, direction in self.__key_interpretation.items():
                if keys[key_code]:
                    self.player.set_direction(direction)
                    break

        # ===== UPDATE =====
        if not self.game_over:
            self._move_timer += time_delta
            if self._move_timer >= self._move_interval:
                self._move_timer -= self._move_interval
                self.player.move()

                # самостолкновение — ПОСЛЕ движения
                if self.player.is_self_encountered():
                    self.collision_position = self.player.get_head_position()
                    self.game_over = True

                # яблоко
                if self.apple.get_position() == self.player.get_head_position():
                    self.player.eat_apple()
                    self.apple.respawn(self.player)

        # ===== RENDER =====
        self._draw_background()
        self._draw_game_objects()
        self._draw_collision()
        self._draw_field()
        

    # <=== методы отрисовки ===>
    def _draw_background(self):
        self.screen.fill(colors["background"])

    def _draw_field(self):
        for x in range(-1, WIDTH, CELL_SIZE):
            pygame.draw.line(self.screen, colors["lines"], (x, 1), (x, HEIGHT), 3)
        for y in range(-1, HEIGHT, CELL_SIZE):
            pygame.draw.line(self.screen, colors["lines"], (1, y), (WIDTH, y), 3)

    def _draw_game_objects(self):
        for obj in self.game_objects:
            obj.draw()

    def _draw_collision(self):
        if self.collision_position:
            x, y = self.collision_position
            pygame.draw.rect(
                self.screen,
                colors["colision"],
                (x, y, CELL_SIZE, CELL_SIZE)
            )

    # <=== методы игры ===>
    def add_game_object(self, *args):
        for arg in args:
            self.game_objects.append(arg)

    def start(self):
        self.running = True

    def stop(self):
        self.running = False
