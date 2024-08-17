import requests

base_url = "https://catalog.api.2gis.com/3.0/items"
rubric_id = '161'  # Замените на актуальный rubric_id
api_key = '013f41f3-bf5c-45e6-b9ad-91037a03cb13'  # Замените на актуальный api_key

params = {
    'rubric_id': rubric_id,
    'region_id': 1,
    'fields': 'items.id,items.name,items.address_name,items.rubrics,items.context',
    'rating': 'src["reviews"]["rating"]',
    'page_size': 10,
    'key': api_key
}

# Создаем строку запроса
response = requests.get(base_url, params=params)

# Получаем полный URL с параметрами
full_url = response.url
print(full_url)
