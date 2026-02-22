# config/data.py

# --- Базовые URL ---
BASE_URL = "https://www.chitai-gorod.ru"
API_BASE_URL = "https://web-agr.chitai-gorod.ru/web/api/v2"

# --- API Endpoints ---
SEARCH_ENDPOINT = "/search/facet-search"

# --- Данные для API-тестов ---
API_TOKEN = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL3VzZXItcmlnaHQiLCJzdWIiOjE5MDcxMzY1LCJpYXQiOjE3NzE3ODA5MzUsImV4cCI6MTc3MTc4NDUzNSwidHlwZSI6MjAsImp0aSI6IjAxOWM4NjVmLThlY2MtN2MyZi04NDU1LWIyNDAxN2NiOTAyNyIsInJvbGVzIjoxMH0.l-YgKgdZ5YdOR2_ZVqXvp0NTZzZ5AYseqKQ_JAE7XVe5FewOiFIHXNYgEjDknTsy9EtrExY4rUCJLv9cE5AyBvLFq3AITl5lH-z8P8kl8pQqQhdT8ArWLYxBcjmgrhteTSdwE9jy5JZ1oG_rwQNseQ8hW_RuSuKQDa7t1W73Ofpqubt9Mxcgdw_EDns6EOEjRYKMhu0kENsMGMgcrZiIQM1Qvg4kaWp_NwOOoAf4xTq54WVONIiiYZXIXXAootpd8H04b_7ruaz8ZBQHDd5yGAhfuDcFd6Gdo_9aTeXrT16mI6s3Sh-QW6gB-optY4to0ipkvVMjaSHQyiL-73tqhw"  # noqa: E501

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
