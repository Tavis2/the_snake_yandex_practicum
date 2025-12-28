"""Tests for GameObject."""

from game_objects.game_object import GameObject


class DummyScreen:
    """Mock screen object."""

    def fill(self, *_args, **_kwargs) -> None:
        pass


def test_game_object_position() -> None:
    """GameObject should convert cell coords to pixels."""
    screen = DummyScreen()
    obj = GameObject(2, 3, screen)

    assert obj.get_position() == (40, 60)
