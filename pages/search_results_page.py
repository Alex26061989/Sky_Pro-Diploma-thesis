# pages/search_results_page.py

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchResultsPage(BasePage):
    """
    Page Object для страницы результатов поиска.
    """
    
    # Локаторы
    RESULTS_TITLES = (By.CSS_SELECTOR, ".product-title a")
    NO_RESULTS_MESSAGE = (By.CSS_SELECTOR, ".catalog-empty-message")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message")
    SEARCH_QUERY_DISPLAY = (By.CSS_SELECTOR, ".search-query-display")
    PAGINATION = (By.CSS_SELECTOR, ".pagination")
    SORT_DROPDOWN = (By.CSS_SELECTOR, ".sort-select")
    FILTER_SIDEBAR = (By.CSS_SELECTOR, ".filter-sidebar")
    
    def __init__(self, driver):
        super().__init__(driver)
    
    def get_results_count(self) -> int:
        """
        Возвращает количество найденных товаров на текущей странице.
        
        Returns:
            int
        """
        titles = self.driver.find_elements(*self.RESULTS_TITLES)
        return len(titles)
    
    def get_result_titles(self) -> list:
        """
        Возвращает список названий найденных товаров.
        
        Returns:
            list of str
        """
        titles = self.driver.find_elements(*self.RESULTS_TITLES)
        return [title.text for title in titles if title.text]
    
    def is_no_results_message_displayed(self) -> bool:
        """
        Проверяет, отображается ли сообщение об отсутствии результатов.
        
        Returns:
            bool
        """
        return self.is_element_present(self.NO_RESULTS_MESSAGE)
    
    def get_no_results_message_text(self) -> str:
        """
        Возвращает текст сообщения об отсутствии результатов.
        
        Returns:
            str
        """
        if self.is_no_results_message_displayed():
            return self.find_element(self.NO_RESULTS_MESSAGE).text
        return ""
    
    def is_error_message_displayed(self) -> bool:
        """
        Проверяет, отображается ли сообщение об ошибке.
        
        Returns:
            bool
        """
        return self.is_element_present(self.ERROR_MESSAGE)
    
    def get_error_message_text(self) -> str:
        """
        Возвращает текст сообщения об ошибке.
        
        Returns:
            str
        """
        if self.is_error_message_displayed():
            return self.find_element(self.ERROR_MESSAGE).text
        return ""
    
    def get_search_query_displayed(self) -> str:
        """
        Возвращает отображаемый поисковый запрос на странице результатов.
        
        Returns:
            str
        """
        if self.is_element_present(self.SEARCH_QUERY_DISPLAY):
            return self.find_element(self.SEARCH_QUERY_DISPLAY).text
        return ""
    
    def has_pagination(self) -> bool:
        """
        Проверяет, есть ли пагинация (много результатов).
        
        Returns:
            bool
        """
        return self.is_element_present(self.PAGINATION)
    
    def has_filters(self) -> bool:
        """
        Проверяет, отображается ли сайдбар с фильтрами.
        
        Returns:
            bool
        """
        return self.is_element_present(self.FILTER_SIDEBAR)