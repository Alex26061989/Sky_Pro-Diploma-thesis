# tests/test_api.py

import pytest
import allure
import requests
from config.data import (
    API_BASE_URL, API_TOKEN, SEARCH_ENDPOINT,
    SEARCH_QUERIES, ERROR_MESSAGES
)
from utils.helpers import build_search_params, extract_error_message

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": API_TOKEN
}


@allure.feature("API тесты")
@allure.severity(allure.severity_level.CRITICAL)
class TestAPISearch:

    @allure.title("Поиск по полному названию на кириллице")
    def test_search_full_title_cyrillic(self):
        with allure.step("Подготовить параметры запроса"):
            url = f"{API_BASE_URL}{SEARCH_ENDPOINT}"
            params = build_search_params(SEARCH_QUERIES["valid_full_cyrillic"])

        with allure.step("Выполнить GET запрос"):
            response = requests.get(url, params=params, headers=HEADERS)

        with allure.step("Проверить статус ответа 200"):
            assert response.status_code == 200

        with allure.step("Проверить наличие данных в ответе"):
            data = response.json()
            assert "data" in data
            assert len(data["data"]) > 0

    @allure.title("Поиск по неполному названию")
    def test_search_partial_title(self):
        with allure.step("Подготовить параметры запроса"):
            url = f"{API_BASE_URL}{SEARCH_ENDPOINT}"
            params = build_search_params(SEARCH_QUERIES["valid_partial"])

        with allure.step("Выполнить GET запрос"):
            response = requests.get(url, params=params, headers=HEADERS)

        with allure.step("Проверить статус ответа 200"):
            assert response.status_code == 200

    @allure.title("Поиск с пустым запросом")
    def test_search_empty_query(self):
        with allure.step("Подготовить параметры с пустым запросом"):
            url = f"{API_BASE_URL}{SEARCH_ENDPOINT}"
            params = build_search_params(SEARCH_QUERIES["empty"])

        with allure.step("Выполнить GET запрос"):
            response = requests.get(url, params=params, headers=HEADERS)

        with allure.step("Проверить статус ответа 400"):
            assert response.status_code == 400

        with allure.step("Проверить сообщение об ошибке"):
            data = response.json()
            error_message = extract_error_message(data)
            assert ERROR_MESSAGES["phrase_required"] in error_message

    @allure.title("Поиск со спецсимволами")
    def test_search_special_characters(self):
        with allure.step("Подготовить запрос со спецсимволами"):
            url = f"{API_BASE_URL}{SEARCH_ENDPOINT}"
            params = build_search_params(SEARCH_QUERIES["specials"])

        with allure.step("Выполнить GET запрос"):
            response = requests.get(url, params=params, headers=HEADERS)

        with allure.step("Проверить статус ответа (403 или 422)"):
            assert response.status_code in [403, 422], \
                f"Ожидался статус 403 или 422, получен {response.status_code}"

        with allure.step("Проверить наличие ошибки"):
            content_type = response.headers.get('Content-Type', '')
            if 'application/json' in content_type:
                data = response.json()
                error_message = extract_error_message(data)
                assert error_message, "Получено пустое сообщение об ошибке"
            else:
                assert 'Access Blocked' in response.text or 'blocked' in response.text.lower()

    @allure.title("Запрос без токена авторизации")
    def test_search_without_token(self):
        with allure.step("Подготовить запрос без токена"):
            url = f"{API_BASE_URL}{SEARCH_ENDPOINT}"
            params = build_search_params(SEARCH_QUERIES["valid_full_cyrillic"])
            headers_without_auth = {"Content-Type": "application/json"}

        with allure.step("Выполнить GET запрос без авторизации"):
            response = requests.get(url, params=params, headers=headers_without_auth)

        with allure.step("Проверить статус ответа 401"):
            assert response.status_code == 401

        with allure.step("Проверить сообщение об ошибке"):
            data = response.json()
            assert "message" in data
            assert ERROR_MESSAGES["auth_required"] in data["message"]