# conftest.py

import pytest
import sys
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Добавляем корневую папку проекта в путь поиска модулей
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

@pytest.fixture(scope="function")
def browser():
    """Фикстура для создания и закрытия браузера."""
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

def pytest_configure(config):
    """Регистрируем кастомные маркеры"""
    config.addinivalue_line("markers", "ui: UI-тесты (требуют браузер)")
    config.addinivalue_line("markers", "api: API-тесты (не требуют браузера)")
