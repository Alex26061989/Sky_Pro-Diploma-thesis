# pages/base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import time


class BasePage:
    """
    Базовый класс для всех Page Object.
    Содержит общие методы для работы со страницами.
    """

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator: tuple, timeout: int = 10):
        """
        Находит один элемент с явным ожиданием его видимости.

        Args:
            locator: кортеж (By.XPATH, "значение") или (By.CSS_SELECTOR, "значение")
            timeout: таймаут ожидания в секундах

        Returns:
            WebElement
        """
        wait = WebDriverWait(self.driver, timeout)
        try:
            return wait.until(EC.visibility_of_element_located(locator))
        except Exception as e:
            print(f"Не удалось найти элемент. Ошибка: {e}")
            self.driver.save_screenshot(f"error_{int(time.time())}.png")
            raise

    def find_elements(self, locator: tuple, timeout: int = 10):
        """
        Находит все элементы, соответствующие локатору.

        Args:
            locator: кортеж (By.XPATH, "значение")
            timeout: таймаут ожидания в секундах

        Returns:
            list of WebElement
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_all_elements_located(locator))

    def click_element(self, locator: tuple, timeout: int = 10):
        """
        Кликает по элементу после ожидания его кликабельности.

        Args:
            locator: кортеж (By.XPATH, "значение")
            timeout: таймаут ожидания в секундах
        """
        wait = WebDriverWait(self.driver, timeout)
        try:
            element = wait.until(EC.element_to_be_clickable(locator))
            element.click()
        except Exception as e:
            print(f"Не удалось кликнуть по элементу. Ошибка: {e}")
            element = self.find_element(locator, timeout)
            self.driver.execute_script("arguments[0].click();", element)

    def input_text(self, locator: tuple, text: str):
        """
        Вводит текст в поле ввода.

        Args:
            locator: кортеж (By.XPATH, "значение")
            text: текст для ввода
        """
        try:
            element = self.find_element(locator)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            print(f"Не удалось ввести текст. Ошибка: {e}")
            self.driver.execute_script(
                "arguments[0].value = arguments[1];",
                self.find_element(locator),
                text
            )

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
        Проверяет, присутствует ли элемент на странице.

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
        except BaseException:
            return False

    def wait_for_url_contains(self, text: str, timeout: int = 10):
        """
        Ожидает, что URL содержит определенный текст.

        Args:
            text: текст, который должен быть в URL
            timeout: время ожидания в секундах
        """
        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))

    def wait_for_page_load(self, timeout: int = 10):
        """Ждет полной загрузки страницы."""
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.execute_script(
                "return document.readyState") == "complete"
        )
        time.sleep(1)
