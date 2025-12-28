"""Tests for global constants."""

from globals import CELL_SIZE, HEIGHT, WIDTH


def test_cell_size_positive() -> None:
    """CELL_SIZE should be positive."""
    assert CELL_SIZE > 0


def test_screen_dimensions() -> None:
    """Screen dimensions should be multiples of CELL_SIZE."""
    assert WIDTH % CELL_SIZE == 0
    assert HEIGHT % CELL_SIZE == 0
