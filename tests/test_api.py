# tests/test_api.py

import pytest
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


@pytest.mark.api
def test_search_full_title_cyrillic():
    """Поиск по полному названию на кириллице."""
    url = f"{API_BASE_URL}{SEARCH_ENDPOINT}"
    params = build_search_params(SEARCH_QUERIES["valid_full_cyrillic"])
    response = requests.get(url, params=params, headers=HEADERS)

    assert response.status_code == 200
    data = response.json()
    assert "data" in data
    assert len(data["data"]) > 0


@pytest.mark.api
def test_search_partial_title():
    """Поиск по неполному названию."""
    url = f"{API_BASE_URL}{SEARCH_ENDPOINT}"
    params = build_search_params(SEARCH_QUERIES["valid_partial"])
    response = requests.get(url, params=params, headers=HEADERS)

    assert response.status_code == 200


@pytest.mark.api
def test_search_empty_query():
    """Поиск с пустым запросом."""
    url = f"{API_BASE_URL}{SEARCH_ENDPOINT}"
    params = build_search_params(SEARCH_QUERIES["empty"])
    response = requests.get(url, params=params, headers=HEADERS)

    assert response.status_code == 400
    data = response.json()
    error_message = extract_error_message(data)
    assert ERROR_MESSAGES["phrase_required"] in error_message

@pytest.mark.api
def test_search_special_characters():
    """Поиск со спецсимволами (допустимы коды 403 или 422)."""
    url = f"{API_BASE_URL}{SEARCH_ENDPOINT}"
    params = build_search_params(SEARCH_QUERIES["specials"])
    response = requests.get(url, params=params, headers=HEADERS)

    # Принимаем оба возможных статуса
    assert response.status_code in [403, 422], \
        f"Ожидался статус 403 или 422, получен {response.status_code}"
    
    # Проверяем, что это либо JSON с ошибкой, либо HTML с блокировкой
    content_type = response.headers.get('Content-Type', '')
    if 'application/json' in content_type:
        data = response.json()
        error_message = extract_error_message(data)
        assert error_message, "Получено пустое сообщение об ошибке"
        print(f"Получен статус {response.status_code}, сообщение: {error_message}")
    else:
        # Это HTML страница с блокировкой
        assert 'Access Blocked' in response.text or 'blocked' in response.text.lower()
        print(f"Получен статус {response.status_code} (HTML страница блокировки)")

@pytest.mark.api
def test_search_without_token():
    """Запрос без токена авторизации."""
    url = f"{API_BASE_URL}{SEARCH_ENDPOINT}"
    params = build_search_params(SEARCH_QUERIES["valid_full_cyrillic"])
    headers_without_auth = {"Content-Type": "application/json"}
    response = requests.get(url, params=params, headers=headers_without_auth)

    assert response.status_code == 401
    data = response.json()
    assert "message" in data
    assert ERROR_MESSAGES["auth_required"] in data["message"]
