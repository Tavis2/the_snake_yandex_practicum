"""Conftest for Snake game tests."""

import os
import sys
from multiprocessing import Process
from pathlib import Path
from typing import Any

import pytest
import pytest_timeout

# Добавляем src в sys.path
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent
sys.path.insert(0, str(BASE_DIR))

# Hide the pygame screen
os.environ['SDL_VIDEODRIVER'] = 'dummy'

TIMEOUT_ASSERT_MSG = (
    'Проект работает некорректно, проверка прервана.\n'
    'Вероятные причины ошибки:\n'
    '1. Исполняемый код (например, вызов функции `main()`) оказался в '
    'глобальной зоне видимости. Как исправить: вызов функции `main` поместите '
    'внутрь конструкции `if __name__ == "__main__":`.\n'
    '2. В цикле `while True` внутри функции `main` отсутствует вызов метода '
    '`tick` объекта `clock`. Не изменяйте прекод в этой части.'
)


def import_the_snake():
    """Импорт основного модуля snake."""
    import src.game.main  # noqa


@pytest.fixture(scope='session')
def snake_import_test():
    """Проверяет импорт без зависания."""
    check_import_process = Process(target=import_the_snake)
    check_import_process.start()
    pid = check_import_process.pid
    check_import_process.join(timeout=1)
    if check_import_process.is_alive():
        os.kill(pid, 9)
        raise AssertionError(TIMEOUT_ASSERT_MSG)


@pytest.fixture(scope='session')
def _the_snake(snake_import_test):
    """Импортирует модуль src и проверяет наличие классов."""
    try:
        from src.game_objects.game_object import GameObject
        from src.game_objects.snake import Snake
        from src.game_objects.apple import Apple
    except ImportError as error:
        raise AssertionError(
            f'При импорте модулей game_objects произошла ошибка:\n'
            f'{type(error).__name__}: {error}'
        )
    
    # Проверяем наличие классов
    for class_name in ('GameObject', 'Snake', 'Apple'):
        assert globals().get(class_name), (
            f'Убедитесь, что класс `{class_name}` определен в game_objects.'
        )
    return globals()


def write_timeout_reasons(text, stream=None):
    """Заменяет вывод pytest_timeout на сообщение с причинами."""
    if stream is None:
        stream = sys.stderr
    stream.write(TIMEOUT_ASSERT_MSG)


pytest_timeout.write = write_timeout_reasons


def _create_game_object(class_name, module):
    """Создаёт объект класса с проверкой конструктора."""
    try:
        cls = module[class_name]
        # Создаём с минимальными параметрами для тестов
        if class_name == 'Apple':
            from src.game_objects.dummy_screen import DummyScreen  # предполагаем
            return cls(0, 0, DummyScreen())
        elif class_name == 'Snake':
            from src.game_objects.dummy_screen import DummyScreen
            return cls(0, 0, DummyScreen(), body_cell_amount=3)
        else:
            return cls(0, 0, None)  # GameObject
    except TypeError as error:
        raise AssertionError(
            f'При создании объекта класса `{class_name}` произошла ошибка:\n'
            f'`{type(error).__name__}: {error}`\n'
            f'Убедитесь, что конструктор принимает параметры по умолчанию.'
        )


@pytest.fixture
def game_object(_the_snake):
    """Фикстура для GameObject."""
    return _create_game_object('GameObject', _the_snake)


@pytest.fixture
def snake(_the_snake):
    """Фикстура для Snake."""
    return _create_game_object('Snake', _the_snake)


@pytest.fixture
def apple(_the_snake):
    """Фикстура для Apple."""
    return _create_game_object('Apple', _the_snake)
