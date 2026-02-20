# pages/base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BasePage:
    """
    Базовый класс для всех Page Object.
    Содержит общие методы для работы со страницами.
    """
    
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Таймаут 10 секунд
    
    def find_element(self, locator: tuple):
        """
        Находит один элемент с явным ожиданием его видимости.
        
        Args:
            locator: кортеж (By.XPATH, "значение") или (By.CSS_SELECTOR, "значение")
        
        Returns:
            WebElement
        """
        return self.wait.until(EC.visibility_of_element_located(locator))
    
    def find_elements(self, locator: tuple):
        """
        Находит все элементы, соответствующие локатору.
        
        Args:
            locator: кортеж (By.XPATH, "значение")
        
        Returns:
            list of WebElement
        """
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
    
    def click_element(self, locator: tuple):
        """
        Кликает по элементу после ожидания его кликабельности.
        
        Args:
            locator: кортеж (By.XPATH, "значение")
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
    
    def input_text(self, locator: tuple, text: str):
        """
        Вводит текст в поле ввода.
        
        Args:
            locator: кортеж (By.XPATH, "значение")
            text: текст для ввода
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)
    
    def get_text(self, locator: tuple) -> str:
        """
        Возвращает текст элемента.
        
        Args:
            locator: кортеж (By.XPATH, "значение")
        
        Returns:
            str
        """
        return self.find_element(locator).text
    
    def is_element_present(self, locator: tuple, timeout: int = 5) -> bool:
        """
        Проверяет, присутствует ли элемент на странице (без исключения).
        
        Args:
            locator: кортеж (By.XPATH, "значение")
            timeout: время ожидания в секундах
        
        Returns:
            bool
        """
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except:
            return False
    
    def wait_for_url_contains(self, text: str):
        """
        Ожидает, что URL содержит определенный текст.
        
        Args:
            text: текст, который должен быть в URL
        """
        self.wait.until(EC.url_contains(text))