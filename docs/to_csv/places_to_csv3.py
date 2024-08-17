import requests
import csv
import random

def fetch_data(rubric_id, api_key):
    base_url = "https://catalog.api.2gis.com/3.0/items"
    params = {
        'rubric_id': rubric_id,
        'region_id': 1,
        'fields': 'items.id,items.name,items.address_name,items.rubrics,items.context',
        'page_size': 10,
        'key': api_key
    }

    response = requests.get(base_url, params=params)
    response.raise_for_status()  # Проверка на ошибки HTTP

    return response.json()

def write_to_csv(data, filename):
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for item in data:
            rubrics = ', '.join([rubric['name'] for rubric in item['rubrics']]) if item['rubrics'] else ''
            context = item['context'] or ''
            rating = round(random.uniform(2.9, 5.0), 1)
            writer.writerow([item['id'], item['name'], item['address_name'], rating,rubrics, context])

def main():
    api_key = "013f41f3-bf5c-45e6-b9ad-91037a03cb13" # demo2
    # api_key = "333f2738-8ebc-482c-8f34-d438836ca445" # demo1 заблокирован
    # api_key = "7c46258b-abf1-4770-bfe2-3098a9f90da0" # prod заблокирован
    rubric_ids = [165]
    # rubric_ids = [161, 165, 112658] # нельзя несколько рубрик запускать, блокируют ключи
    
    # Создаем или очищаем CSV файл
    with open('results.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['ID', 'Name', 'Address', 'Rating', 'Rubric', 'Context'])  # Заголовки

    for rubric_id in rubric_ids:
        page = 1
        while True:
            data = fetch_data(rubric_id, api_key)
            items = data.get('result', {}).get('items', [])
            total_count = data.get('result', {}).get('total', 0)
            max_page = (total_count + 10 - 1) // 10  # Рассчитываем max_page

            if not items:
                break  # Выходим из цикла, если нет данных
            
            write_to_csv(items, 'results.csv')  # Записываем данные в CSV файл
            
            if page >= max_page:
                break  # Если текущая страница больше или равна максимальной, выходим из цикла

            page += 1

if __name__ == "__main__":
    main()
