import sys
from types import SimpleNamespace


class DummyClock:
    """Mock pygame.time.Clock."""

    def tick(self, fps=0):
        """Mock tick."""
        return 16


def _empty_list():
    return []


pygame_mock = SimpleNamespace(
    time=SimpleNamespace(Clock=DummyClock),
    K_w=119,
    K_s=115,
    K_a=97,
    K_d=100,
    QUIT=256,
    key=SimpleNamespace(get_pressed=_empty_list),
    event=SimpleNamespace(get=_empty_list),
    draw=SimpleNamespace(
        rect=lambda *args, **kwargs: None,
        line=lambda *args, **kwargs: None,
    ),
)

sys.modules['pygame'] = pygame_mock
sys.modules['pygame.time'] = pygame_mock.time
