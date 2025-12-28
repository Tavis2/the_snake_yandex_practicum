"""Global constants for the Snake game."""

CELL_SIZE = 20

WIDTH = CELL_SIZE * 32
HEIGHT = CELL_SIZE * 24
LOW_PANEL_SIZE = CELL_SIZE * 6

COLORS = {
    'background': (0, 0, 0),        # чёрный фон
    'lines': (50, 50, 50),          # серые линии
    'apple': (230, 20, 20),         # красное яблоко
    'snake': (20, 230, 20),         # зелёная змейка
    'collision': (255, 130, 0),     # коллизия
}
