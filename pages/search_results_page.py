# pages/search_results_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time

class SearchResultsPage(BasePage):
    """
    Page Object для страницы результатов поиска.
    """

    PRODUCT_TITLES = (By.CSS_SELECTOR, "a.product-card__title, .product-title a, .catalog-product__name, .product-card__name a, [data-testid='product-title']")  # noqa: E501
    NO_RESULTS_MESSAGE = (By.CSS_SELECTOR, ".catalog-empty-message, .not-found-message")

    def __init__(self, driver):
        super().__init__(driver)

    def get_results_count(self) -> int:
        """Возвращает количество найденных товаров."""
        time.sleep(3)
        titles = self.driver.find_elements(*self.PRODUCT_TITLES)
        count = len(titles)
        print(f"Найдено заголовков товаров: {count}")
        
        # Если заголовков нет, попробуем найти карточки товаров
        if count == 0:
            cards = self.driver.find_elements(By.CSS_SELECTOR, ".product-card, .catalog-product")
            count = len(cards)
            print(f"Найдено карточек товаров: {count}")
        
        return count

    def wait_for_results(self, timeout: int = 10):
        """Ожидает загрузки результатов поиска."""
        time.sleep(3)
        print("Ожидание результатов завершено")