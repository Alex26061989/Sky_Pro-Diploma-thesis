# config/data.py

# --- Базовые URL ---
BASE_URL = "https://www.chitai-gorod.ru"
API_BASE_URL = "https://web-agr.chitai-gorod.ru/web/api/v2"

# --- API Endpoints ---
SEARCH_ENDPOINT = "/search/facet-search"

# --- Данные для API-тестов ---
API_TOKEN = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjE5MDcxMzY1LCJpYXQiOjE3NzE4Mzk0ODEsImV4cCI6MTc3MTg0MzA4MSwidHlwZSI6MjAsImp0aSI6IjAxOWM4OWRjLWU1YmItNzYzYy05YWFjLTM4ZGJkNzQwM2NiZSIsInJvbGVzIjoxMH0.kUsoQBgesdZvFlHOhR5v3gP2rV5i0aTNA3llKBN9XvoqQGKfjKPlewFrPQ0mN8kdwiY9Sf8wbfAs-oQnC44f16bY7FZm7tLE9zCspUt6NS2G8tLJhawisTXJfineeRLQjFNoxZ1doZauvGoR2y6YeArJLOyYrLfyfoOH25odrGLuVEk_vJehacp6t41c3LlSQmDhGvspg8SAtxtqZJpIq6K94JoiquEMzE8GAgTsSYPlQpiczSCYeuW86JFrkXv8qAxQukTuJsSk3NdPJkBtoKoh56H_jdcV2hscyPc43vMYd1df-WAO6my7xtXqYI9UNxANalS5Q0LZMWEeWUbBqw"  # noqa: E501
# API_TOKEN = "Bearer YOUR_TOKEN_HERE -> # Замени на свой токен перед запуском"


# Параметры запросов
CUSTOMER_CITY_ID = "213"
AB_TEST_GROUP = "1"

# Поисковые запросы
SEARCH_QUERIES = {
    "valid_full_cyrillic": "Поднятие уровня в одиночку",
    "valid_full_latin": "Solo Leveling",
    "valid_partial": "Война",
    "empty": "",
    "specials": "\"%\"№(\"№\"*\"*\"№*№?\"*\"",
    "hieroglyphs": "を使ってリクエストを送信し、レスポン",
    "long_title": "Очень длинное название книги, которое просто невероятно длинное и занимает много места",  # noqa: E501
    "autocomplete": "Поднятие"
}

# Ожидаемые сообщения об ошибках
ERROR_MESSAGES = {
    "phrase_required": "Phrase обязательное поле",
    "invalid_url_escape": "invalid URL escape \"%%2\"",
    "invalid_phrase": "Недопустимая поисковая фраза",
    "auth_required": "Authorization обязательное поле"
}

# --- Данные для UI-тестов ---
UI_TEST_DATA = {
    "search_queries": {
        "standard": "Шариковая ручка",
        "empty": "",
        "specials": "@#$%",
        "long": "Очень длинное название книги для проверки граничных значений в поле поиска",  # noqa: E501
        "autocomplete_part": "Шариковая"
    }
}
