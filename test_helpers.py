# test_helpers.py - временный файл для проверки
from utils.helpers import build_search_params, make_api_request, extract_error_message
from config.data import SEARCH_ENDPOINT, SEARCH_QUERIES

# Тест 1: Проверяем формирование параметров
params = build_search_params(SEARCH_QUERIES["valid_partial"])
print("Параметры запроса:", params)

# Тест 2: Делаем реальный запрос к API
print("\nВыполняем запрос...")
response = make_api_request("GET", SEARCH_ENDPOINT, params)
print(f"Статус ответа: {response.status_code}")

# Тест 3: Если ошибка - показываем сообщение
if response.status_code != 200:
    error_msg = extract_error_message(response.json())
    print(f"Сообщение об ошибке: {error_msg}")
else:
    print("Запрос успешен!")
    data = response.json()
    if data.get("data"):
        print(f"Найдено элементов: {len(data['data'])}")
