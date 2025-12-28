"""Conftest for Snake game tests."""

import os
import sys


sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))


class DummyPygame:
    """Minimal mock for pygame when not installed."""

    class TimeClass:
        """Mock for pygame.time."""

        class ClockClass:
            """Mock for pygame.time.Clock."""

            def tick(self, fps: int = 0) -> int:
                """Mock tick method returning 16ms."""
                return 16

    time = TimeClass()


try:
    import pygame 
except ImportError:
    pygame = DummyPygame()
