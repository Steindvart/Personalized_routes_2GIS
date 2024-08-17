import pandas as pd
import difflib
import json

# Загрузить CSV файл
df = pd.read_csv('165_results_rating.csv')

# Функция для поиска наиболее похожей строки
def find_similar(row):
    # Применяем подходящие параметры для сравнения
    rating = row['Rating']
    rubric = row['Rubric']
    context = row['Context']
    
    # Поиск остальных строк
    similar_row = None
    max_similarity = -1
    
    for _, candidate in df.iterrows():
        # Игнорируем саму строку
        if candidate['ID'] == row['ID'] or candidate['Name'] == row['Name']:
            continue
        
        # Сравнения по рейтингам
        rating_difference = abs(candidate['Rating'] - rating)
        
        # Сравнение рубрик
        rubric_similarity = difflib.SequenceMatcher(None, rubric, candidate['Rubric']).ratio()
        
        # Сравнение контекстов
        context_similarity = difflib.SequenceMatcher(None, context, candidate['Context']).ratio()
        
        # Веса для каждого условия (можно настроить)
        total_similarity = (1 / (1 + rating_difference)) + rubric_similarity + context_similarity
        
        # Сравниваем с максимальным
        if total_similarity > max_similarity:
            max_similarity = total_similarity
            similar_row = candidate
    
    return similar_row

# Создание нового DataFrame для результатов
results = []

# Поиск наиболее похожих строк
for _, row in df.iterrows():
    similar = find_similar(row)
    if similar is not None:
        results.append(similar)

# Создание DataFrame с результатами
results_df = pd.DataFrame(results)

# Сохранение результата в CSV файл
results_df.to_csv('165_results_rating_similar.csv', index=False)

print("Сохранение завершено!")
