# tests/test_ui.py

import pytest
import time
import allure
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from config.data import UI_TEST_DATA

@allure.feature("UI тесты")
@allure.severity(allure.severity_level.CRITICAL)
class TestUISearch:

    @allure.title("Поиск товара по полному названию")
    @allure.description("Проверка поиска по полному названию 'Шариковая ручка'")
    def test_search_by_full_title(self, browser):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(browser)
            main_page.open()

        with allure.step(f"Ввести поисковый запрос: {UI_TEST_DATA['search_queries']['standard']}"):
            search_query = UI_TEST_DATA["search_queries"]["standard"]
            main_page.search(search_query)

        with allure.step("Дождаться загрузки результатов"):
            time.sleep(3)

        with allure.step("Проверить результаты поиска"):
            results_page = SearchResultsPage(browser)
            results_page.wait_for_results()
            results_count = results_page.get_results_count()
            
        with allure.step(f"Проверить, что найдены товары по запросу '{search_query}'"):
            assert results_count > 0, f"Нет товаров по запросу '{search_query}'"

    @allure.title("Поиск по длинному названию")
    def test_search_by_long_title(self, browser):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(browser)
            main_page.open()

        with allure.step("Ввести длинный поисковый запрос"):
            long_query = UI_TEST_DATA["search_queries"]["long"]
            main_page.search(long_query)

        with allure.step("Проверить, что запрос не обрезался"):
            input_value = main_page.get_search_input_value()
            assert input_value == long_query, "Запрос в поле поиска изменился"

    @allure.title("Проверка автоподстановки")
    def test_autocomplete_suggestions(self, browser):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(browser)
            main_page.open()

        with allure.step(f"Ввести частичный запрос: {UI_TEST_DATA['search_queries']['autocomplete_part']}"):
            partial_query = UI_TEST_DATA["search_queries"]["autocomplete_part"]
            main_page.input_text(main_page.SEARCH_INPUT, partial_query)

        with allure.step("Проверить появление автоподстановки"):
            assert main_page.is_autocomplete_displayed(), "Автоподстановка не появилась"

        with allure.step("Проверить наличие подсказок"):
            suggestions = main_page.get_autocomplete_suggestions()
            assert len(suggestions) > 0, "Список подсказок пуст"

    @allure.title("Поиск с пустым запросом")
    def test_search_empty_query(self, browser):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(browser)
            main_page.open()

        with allure.step("Очистить поле поиска и выполнить поиск"):
            main_page.clear_search_input()
            main_page.search("")

        with allure.step("Проверить, что поиск не выполнен"):
            current_url = browser.current_url
            assert "search" not in current_url, "Поиск с пустым запросом не должен работать"

    @allure.title("Поиск со спецсимволами")
    def test_search_special_characters(self, browser):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(browser)
            main_page.open()

        with allure.step("Ввести спецсимволы в поиск"):
            special_query = UI_TEST_DATA["search_queries"]["specials"]
            main_page.search(special_query)

        with allure.step("Проверить, что товары не найдены"):
            results_page = SearchResultsPage(browser)
            results_page.wait_for_results()
            results_count = results_page.get_results_count()
            assert results_count == 0, "Найдены товары по спецсимволам"

    @allure.title("Навигация в каталог")
    def test_catalog_navigation(self, browser):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(browser)
            main_page.open()

        with allure.step("Перейти в каталог"):
            main_page.go_to_catalog()

        with allure.step("Проверить URL каталога"):
            current_url = browser.current_url
            assert "catalog" in current_url.lower() or "category" in current_url.lower(), \
                f"Переход в каталог не произошел, URL: {current_url}"

    @allure.title("Доступ к корзине")
    def test_cart_access(self, browser):
        with allure.step("Открыть главную страницу"):
            main_page = MainPage(browser)
            main_page.open()

        with allure.step("Перейти в корзину"):
            main_page.go_to_cart()

        with allure.step("Проверить URL корзины"):
            current_url = browser.current_url
            assert "cart" in current_url.lower(), f"Переход в корзину не произошел, URL: {current_url}"