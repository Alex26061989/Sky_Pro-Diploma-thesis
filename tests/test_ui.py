# tests/test_ui.py

import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage
from config.data import UI_TEST_DATA


@pytest.fixture(scope="function")
def browser():
    """Фикстура для создания и закрытия браузера."""
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@pytest.mark.ui
def test_search_by_full_title(browser):
    """Поиск товара по полному названию."""
    main_page = MainPage(browser)
    main_page.open()

    search_query = UI_TEST_DATA["search_queries"]["standard"]
    print(f"\nПоисковый запрос: {search_query}")
    
    main_page.search(search_query)
    
    # Ждем загрузки
    time.sleep(3)
    
    # Сохраняем скриншот
    browser.save_screenshot("search_results.png")
    print("Скриншот сохранен как search_results.png")
    
    # Выводим текущий URL
    print(f"Текущий URL: {browser.current_url}")
    
    # Ищем все ссылки на странице
    all_links = browser.find_elements(By.TAG_NAME, "a")
    print(f"Всего ссылок на странице: {len(all_links)}")
    
    # Покажем первые 10 ссылок с текстом
    for i, link in enumerate(all_links[:10]):
        text = link.text
        if text and len(text) > 3:
            print(f"Ссылка {i+1}: {text[:50]}...")

    results_page = SearchResultsPage(browser)
    results_page.wait_for_results()

    results_count = results_page.get_results_count()
    print(f"Найдено товаров: {results_count}")
    
    assert results_count > 0, f"Нет товаров по запросу '{search_query}'"


@pytest.mark.ui
def test_search_by_full_title(browser):
    """Поиск товара по полному названию."""
    main_page = MainPage(browser)
    main_page.open()

    search_query = UI_TEST_DATA["search_queries"]["standard"]
    print(f"\nПоисковый запрос: {search_query}")

    main_page.search(search_query)

    time.sleep(3)
    
    # Проверяем заголовок страницы
    page_title = browser.title
    print(f"Заголовок страницы: {page_title}")
    
    # Проверяем, нет ли сообщения об ошибке
    page_source = browser.page_source
    if "технические работы" in page_source.lower():
        print("⚠️ Сайт на техническом обслуживании!")
    elif "not found" in page_source.lower() or "404" in page_source:
        print("⚠️ Страница не найдена!")
    
    browser.save_screenshot("search_results.png")
    print("Скриншот сохранен как search_results.png")
    print(f"Текущий URL: {browser.current_url}")

    all_links = browser.find_elements(By.TAG_NAME, "a")
    print(f"Всего ссылок на странице: {len(all_links)}")

    results_page = SearchResultsPage(browser)
    results_page.wait_for_results()

    results_count = results_page.get_results_count()
    print(f"Найдено товаров: {results_count}")

    assert results_count > 0, f"Нет товаров по запросу '{search_query}'"


@pytest.mark.ui
def test_autocomplete_suggestions(browser):
    """Проверка автоподстановки."""
    main_page = MainPage(browser)
    main_page.open()

    partial_query = UI_TEST_DATA["search_queries"]["autocomplete_part"]
    main_page.input_text(main_page.SEARCH_INPUT, partial_query)

    assert main_page.is_autocomplete_displayed(), "Автоподстановка не появилась"

    suggestions = main_page.get_autocomplete_suggestions()
    assert len(suggestions) > 0, "Список подсказок пуст"


@pytest.mark.ui
def test_search_empty_query(browser):
    """Поиск с пустым запросом."""
    main_page = MainPage(browser)
    main_page.open()

    main_page.clear_search_input()
    main_page.search("")

    current_url = browser.current_url
    assert "search" not in current_url, "Поиск с пустым запросом не должен работать"


@pytest.mark.ui
def test_search_special_characters(browser):
    """Поиск со спецсимволами."""
    main_page = MainPage(browser)
    main_page.open()

    special_query = UI_TEST_DATA["search_queries"]["specials"]
    main_page.search(special_query)

    results_page = SearchResultsPage(browser)
    results_page.wait_for_results()

    results_count = results_page.get_results_count()
    assert results_count == 0, "Найдены товары по спецсимволам"


@pytest.mark.ui
def test_catalog_navigation(browser):
    """Навигация через каталог."""
    main_page = MainPage(browser)
    main_page.open()
    main_page.go_to_catalog()

    current_url = browser.current_url
    assert "catalog" in current_url.lower() or "category" in current_url.lower(), \
        f"Переход в каталог не произошел, URL: {current_url}"


@pytest.mark.ui
def test_cart_access(browser):
    """Доступ к корзине."""
    main_page = MainPage(browser)
    main_page.open()
    main_page.go_to_cart()

    current_url = browser.current_url
    assert "cart" in current_url.lower(), f"Переход в корзину не произошел, URL: {current_url}"