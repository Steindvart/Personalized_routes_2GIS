import requests

base_url = "https://catalog.api.2gis.com/3.0/items"
rubric_id = '112658'  # Замените на актуальный rubric_id
api_key = '7c46258b-abf1-4770-bfe2-3098a9f90da0'  # Замените на актуальный api_key

params = {
    'rubric_id': rubric_id,
    'region_id': 1,
    'fields': 'items.rubrics,items.context,items.reviews',
    'rating': 'src.get("reviews", {}).get("rating", 0.0)',
    'page_size': 10,
    'key': api_key
}

# Создаем строку запроса
response = requests.get(base_url, params=params)

# Получаем полный URL с параметрами
full_url = response.url
print(full_url)
