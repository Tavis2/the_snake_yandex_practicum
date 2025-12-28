"""Conftest for Snake game tests."""

import sys
import os

# Добавляем src в sys.path для корректных импортов
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

# Импортируем pygame (если установлен) или создаём минимальный мок только при необходимости
try:
    import pygame
except ImportError:
    # Минимальный мок только для Clock, если pygame не установлен
    class DummyPygame:
        class time:
            class Clock:
                def tick(self, fps=0):
                    return 16
    pygame = DummyPygame()
