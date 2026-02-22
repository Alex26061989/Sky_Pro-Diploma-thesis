# pages/main_page.py

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import time


class MainPage(BasePage):
    """
    Page Object для главной страницы сайта Читай-город.
    """

    SEARCH_INPUT = (By.CSS_SELECTOR, "input#app-search.search-form__input")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button.chg-app-button[type='submit']")
    AUTOCOMPLETE_DROPDOWN = (By.CSS_SELECTOR, ".suggests-modal")
    AUTOCOMPLETE_ITEMS = (By.CSS_SELECTOR, ".suggests-list button")
    CATALOG_BUTTON = (By.CSS_SELECTOR, "button.catalog-btn")
    CART_BUTTON = (By.CSS_SELECTOR, "button[aria-label='Корзина']")
    
    # Локаторы для модального окна с городом
    CITY_MODAL = (By.CSS_SELECTOR, ".header-location-popup, .location-modal, [class*='location']")
    CITY_CONFIRM_BUTTON = (By.CSS_SELECTOR, ".header-location-popup button, .location-modal button, button:contains('Да'), button:contains('Верно')")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.chitai-gorod.ru"

    def close_city_modal_if_present(self):
        """Закрывает модальное окно с выбором города, если оно появилось."""
        try:
            time.sleep(2)  # Ждем появления модального окна
            if self.is_element_present(self.CITY_MODAL, timeout=3):
                print("Найдено модальное окно с городом, закрываем...")
                confirm_btn = self.find_element(self.CITY_CONFIRM_BUTTON, timeout=2)
                confirm_btn.click()
                time.sleep(1)
                print("Модальное окно закрыто")
        except Exception as e:
            print(f"Нет модального окна или ошибка: {e}")

    def open(self):
        """Открывает главную страницу."""
        self.driver.get(self.url)
        self.wait_for_page_load()
        time.sleep(2)
        self.close_city_modal_if_present()  # Закрываем модальное окно после загрузки

    def search(self, query: str):
        """Выполняет поиск."""
        search_input = self.find_element(self.SEARCH_INPUT, timeout=15)
        search_input.clear()
        search_input.send_keys(query)
        time.sleep(1)

        try:
            search_button = self.find_element(self.SEARCH_BUTTON, timeout=5)
            search_button.click()
        except Exception:
            search_input.send_keys(Keys.RETURN)

    def get_search_input_value(self) -> str:
        """Возвращает значение в поле поиска."""
        return self.find_element(self.SEARCH_INPUT).get_attribute("value")

    def is_autocomplete_displayed(self) -> bool:
        """Проверяет отображение автоподстановки."""
        time.sleep(1)
        return self.is_element_present(self.AUTOCOMPLETE_DROPDOWN, timeout=3)

    def get_autocomplete_suggestions(self) -> list:
        """Возвращает список подсказок."""
        if not self.is_autocomplete_displayed():
            return []

        try:
            items = self.find_elements(self.AUTOCOMPLETE_ITEMS, timeout=2)
            if items:
                return [item.text for item in items if item.text]
        except Exception:
            pass

        dropdown = self.find_element(self.AUTOCOMPLETE_DROPDOWN)
        lines = [line.strip() for line in dropdown.text.split('\n') if line.strip()]
        return lines

    def clear_search_input(self):
        """Очищает поле поиска."""
        self.find_element(self.SEARCH_INPUT).clear()

    def go_to_catalog(self):
        """Переходит в каталог."""
        try:
            self.close_city_modal_if_present()  # Сначала закрываем модальное окно
            
            catalog_btn = self.find_element(self.CATALOG_BUTTON, timeout=10)
            catalog_btn.click()
            time.sleep(3)
            print(f"URL после клика: {self.driver.current_url}")
        except Exception as e:
            print(f"Ошибка при клике на каталог: {e}")
            self.driver.get("https://www.chitai-gorod.ru/catalog")
            time.sleep(2)

    def go_to_cart(self):
        """Переходит в корзину."""
        try:
            self.close_city_modal_if_present()  # Сначала закрываем модальное окно
            
            cart_btn = self.find_element(self.CART_BUTTON, timeout=10)
            cart_btn.click()
            time.sleep(3)
            print(f"URL после клика: {self.driver.current_url}")
        except Exception as e:
            print(f"Ошибка при клике на корзину: {e}")
            self.driver.get("https://www.chitai-gorod.ru/cart")
            time.sleep(2)