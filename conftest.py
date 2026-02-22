# conftest.py

import pytest
import sys
import os

# Добавляем корневую папку проекта в путь поиска модулей
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


def pytest_configure(config):
    """Регистрируем кастомные маркеры"""
    config.addinivalue_line("markers", "ui: UI-тесты (требуют браузер)")
    config.addinivalue_line("markers", "api: API-тесты (не требуют браузера)")
