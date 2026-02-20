# pages/main_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class MainPage(BasePage):
    """
    Page Object для главной страницы сайта Читай-город.
    """
    
    # Локаторы элементов на главной странице
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[type='search']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    AUTOCOMPLETE_DROPDOWN = (By.CSS_SELECTOR, ".autocomplete-suggestions")
    AUTOCOMPLETE_ITEMS = (By.CSS_SELECTOR, ".autocomplete-suggestion")
    CATALOG_BUTTON = (By.XPATH, "//a[contains(text(), 'Каталог')]")
    CART_BUTTON = (By.XPATH, "//a[contains(@href, '/cart')]")
    
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://www.chitai-gorod.ru"
    
    def open(self):
        """Открывает главную страницу."""
        self.driver.get(self.url)
        # Ждем, чтобы страница полностью загрузилась
        self.wait_for_url_contains("chitai-gorod")
    
    def search(self, query: str):
        """
        Выполняет поиск по заданному запросу.
        
        Args:
            query: поисковый запрос
        """
        self.input_text(self.SEARCH_INPUT, query)
        self.click_element(self.SEARCH_BUTTON)
    
    def get_search_input_value(self) -> str:
        """
        Возвращает текущее значение в поле поиска.
        
        Returns:
            str
        """
        return self.find_element(self.SEARCH_INPUT).get_attribute("value")
    
    def is_autocomplete_displayed(self) -> bool:
        """
        Проверяет, отображается ли выпадающий список автоподстановки.
        
        Returns:
            bool
        """
        return self.is_element_present(self.AUTOCOMPLETE_DROPDOWN, timeout=3)
    
    def get_autocomplete_suggestions(self) -> list:
        """
        Возвращает список текстов из подсказок автоподстановки.
        
        Returns:
            list of str
        """
        if not self.is_autocomplete_displayed():
            return []
        
        items = self.find_elements(self.AUTOCOMPLETE_ITEMS)
        return [item.text for item in items if item.text]
    
    def clear_search_input(self):
        """Очищает поле поиска."""
        self.find_element(self.SEARCH_INPUT).clear()
    
    def go_to_catalog(self):
        """Переходит в каталог."""
        self.click_element(self.CATALOG_BUTTON)
    
    def go_to_cart(self):
        """Переходит в корзину."""
        self.click_element(self.CART_BUTTON)