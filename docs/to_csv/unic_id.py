import pandas as pd

# Считываем данные из CSV файла
file_path = '112658_data_similar.csv'
data = pd.read_csv(file_path)

# Извлекаем уникальные ID
unique_ids = data['ID'].unique()

# Сохраняем уникальные ID в новый файл
unique_ids_file_path = 'unique_ids.txt'
with open(unique_ids_file_path, 'w') as f:
    for unique_id in unique_ids:
        f.write(f"{unique_id}\n")

print(f"Уникальные ID сохранены в файл: {unique_ids_file_path}")
