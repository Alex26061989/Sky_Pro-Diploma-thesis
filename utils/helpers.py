# utils/helpers.py

import requests
from config.data import API_BASE_URL, API_TOKEN, SEARCH_ENDPOINT


def make_api_request(
        method: str,
        endpoint: str,
        params: dict = None,
        headers: dict = None):
    """
    Универсальная функция для выполнения API-запросов.

    Args:
        method: HTTP метод (GET, POST, PUT и т.д.)
        endpoint: путь к endpoint (например, "/search/facet-search")
        params: параметры запроса (словарь)
        headers: заголовки запроса (словарь)

    Returns:
        Response объект от requests
    """
    url = f"{API_BASE_URL}{endpoint}"

    # Базовые заголовки, если не переданы свои
    if headers is None:
        headers = {
            "Content-Type": "application/json",
            "Authorization": API_TOKEN
        }

    response = requests.request(method, url, params=params, headers=headers)
    return response


def build_search_params(
        phrase: str,
        city_id: str = "213",
        ab_group: str = "1") -> dict:
    """
    Формирует параметры для поискового запроса.

    Args:
        phrase: поисковая фраза
        city_id: ID города
        ab_group: группа A/B тестирования

    Returns:
        Словарь с параметрами для запроса
    """
    return {
        "customerCityId": city_id,
        "phrase": phrase,
        "abTestGroup": ab_group
    }


def save_response_to_file(
        response_json: dict,
        filename: str = "last_response.json"):
    """
    Сохраняет JSON ответа в файл (полезно для отладки).

    Args:
        response_json: JSON объект ответа
        filename: имя файла для сохранения
    """
    import json
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(response_json, f, ensure_ascii=False, indent=2)
    print(f"Ответ сохранен в {filename}")


def validate_json_structure(data: dict, expected_keys: list) -> bool:
    """
    Проверяет, содержит ли JSON определенные ключи.

    Args:
        data: JSON объект (словарь)
        expected_keys: список ожидаемых ключей

    Returns:
        True если все ключи присутствуют, иначе False
    """
    return all(key in data for key in expected_keys)


def extract_error_message(response_json: dict) -> str:
    """
    Извлекает сообщение об ошибке из стандартного формата ошибок API.

    Args:
        response_json: JSON объект ответа с ошибкой

    Returns:
        Текст ошибки или пустую строку
    """
    try:
        # Пробуем разные возможные пути к ошибке
        if "errors" in response_json and len(response_json["errors"]) > 0:
            if "title" in response_json["errors"][0]:
                return response_json["errors"][0]["title"]
            elif "message" in response_json["errors"][0]:
                return response_json["errors"][0]["message"]
        elif "message" in response_json:
            return response_json["message"]
        elif "title" in response_json:
            return response_json["title"]
    except (KeyError, IndexError, TypeError):
        pass
    return ""


# Пример использования (закомментировано)
if __name__ == "__main__":
    # Тестовый запуск
    params = build_search_params("Война")
    response = make_api_request("GET", SEARCH_ENDPOINT, params)
    print(f"Статус: {response.status_code}")

    if response.status_code == 200:
        data = response.json()
        save_response_to_file(data, "test_search.json")
        print(
            "JSON структура валидна?",
            validate_json_structure(
                data,
                ["data"]))
    else:
        print("Ошибка:", extract_error_message(response.json()))
