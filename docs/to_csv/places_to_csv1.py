import requests
import csv
import json

# Параметры
# API_KEY = "013f41f3-bf5c-45e6-b9ad-91037a03cb13" # demo2
# API_KEY = "333f2738-8ebc-482c-8f34-d438836ca445" # demo1
API_KEY = "7c46258b-abf1-4770-bfe2-3098a9f90da0" # prod
RUBRIC_ID = 165
REGION_ID = 1
PAGE_SIZE = 10

# URL API
base_url = "https://catalog.api.2gis.com/3.0/items"
# Параметры для запроса
params = {
    'rubric_id': RUBRIC_ID,
    'region_id': REGION_ID,
    'fields': 'items.rubrics,items.context,items.reviews',
    'page_size': PAGE_SIZE,
    'key': API_KEY
}

# Определяем max_page
# params['page'] = 1
response = requests.get(base_url, params=params)
if response.status_code != 200:
    print("Error fetching data from API.")
    exit()

data = response.json()

# Получаем общее количество записей и рассчитываем max_page
total_items = data['result']['total']
max_page = (total_items + PAGE_SIZE - 1) // PAGE_SIZE  # вычисляем количество страниц

# Файл для записи данных
output_file = str(RUBRIC_ID) + '_data.csv'
# output_file = f"{RUBRIC_ID}_data.csv"


# Открываем файл для записи
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    # Заголовки CSV
    fieldnames = ['ID', 'Name', 'Address', 'Rating', 'Rubric', 'Context']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Проходим по страницам от 1 до max_page
    for page in range(1, max_page + 1):
        params['page'] = page
        response = requests.get(base_url, params=params)
        
        if response.status_code == 200:
            data = response.json()
            items = data.get('result', {}).get('items', [])
            
            for item in items:
                # Получаем необходимые данные
                item_id = item.get('id')
                item_name = item.get('name')
                item_address = item.get('address_name')
                rating = item.get('reviews', {}).get('general_rating', 0.0)
                # Обрабатываем рубрики
                rubrics = item.get('rubrics', [])
                rubric_names = [rubric.get('name') for rubric in rubrics]
                # Обрабатываем контекст
                context = item.get('context', {})
                
                # Проверяем наличие контекста, если пусто, оставляем None
                context_info = context if context else None

                # Записываем данные в CSV
                writer.writerow({
                    'ID': item_id,
                    'Name': item_name,
                    'Address': item_address,
                    'Rating': rating,
                    'Rubric': ', '.join(rubric_names),
                    'Context': context_info
                })
        else:
            print(f"Ошибка при получении данных: {response.status_code}, {response.text}")

print(f"Данные успешно записаны в файл {output_file}.")
print(f"max_page = {max_page}")
