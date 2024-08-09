# Описание и пример заполнения базы данных для персонализированных маршрутов


## Описание базы данных

База данных использует различные таблицы для хранения информации о пользователях, категориях, критиерях оценки (полях) и значениях этих критериев (полей), а также для хранения индивидуальных предпочтений пользователей.

## Структура базы данных

1. **Таблица `users`** — Хранит данные пользователей:
   - `id` (BIGINT) — Уникальный идентификатор пользователя.
   - `name` (VARCHAR) — Имя пользователя.
   - `password` (VARCHAR) — Пароль пользователя.
   - `email` (VARCHAR) — Электронная почта пользователя (уникальна).

2. **Таблица `categories`** — Хранит категории предпочтений:
   - `id` (BIGINT) — Уникальный идентификатор категории.
   - `name` (VARCHAR) — Название категории (например, "Рестораны").

3. **Таблица `fields`** — Хранит критерии (поля), доступные для категорий:
   - `id` (BIGINT) — Уникальный идентификатор поля.
   - `name` (VARCHAR) — Название поля (например, "Кухня").
   - `units` (VARCHAR) — Единицы измерения (например, "км", "рубли").

4. **Таблица `fields_values`** — Хранит значения критериев (полей):
   - `id` (BIGINT) — Уникальный идентификатор значения.
   - `field_id` (BIGINT) — Ссылка на поле, к которому относится значение.
   - `value` (VARCHAR) — Значение поля (например, "Итальянская").

5. **Таблица `preferences`** — Хранит предпочтения пользователей:
   - `id` (BIGINT) — Уникальный идентификатор предпочтения.
   - `user_id` (BIGINT) — Ссылка на пользователя, которому принадлежит предпочтение.
   - `category_id` (BIGINT) — Ссылка на категорию предпочтения.
   - `rating` (DECIMAL) — Рейтинг предпочтения.
   - `options` (VARCHAR) — Все поля предпочтения в связке с категориями в формате JSON. (например,
   '{"Кухня": "Итальянская", "Ценовой диапазон": "500-1500", "Максимальное расстояние": "5 км"}')

6. **Таблица `categories_fields`** — Связывает категории и поля:
   - `category_id` (BIGINT) — Ссылка на категорию.
   - `field_id` (BIGINT) — Ссылка на поле.

## Пример заполнения

```sql
INSERT INTO users (id, name, password, email)
VALUES (1, 'Иван Иванов', 'hashed_password', 'ivan@example.com');

INSERT INTO categories (id, name)
VALUES (1, 'Рестораны');

INSERT INTO fields (id, name, units)
VALUES (1, 'Кухня', '');

INSERT INTO categories_fields (category_id, field_id)
VALUES (1, 1);

INSERT INTO fields_values (id, field_id, value)
VALUES (1, 1, 'Итальянская');

INSERT INTO preferences (id, user_id, category_id, rating, options)
VALUES 
(
    1, 
    1, 
    1, 
    4.5, 
    (
        SELECT jsonb_object_agg(f.name, fv.value)
        FROM fields f
        JOIN fields_values fv ON f.id = fv.field_id
        WHERE f.id IN (SELECT field_id FROM categories_fields WHERE category_id = 1)
    )
);
```

# Динамическое создание поля options в формате json в приложении
```python
import json
import psycopg2

# Подключение к базе данных PostgreSQL
conn = psycopg2.connect("dbname=your_db user=your_user password=your_password")
cur = conn.cursor()

# Получаем поля и их значения для определенной категории
cur.execute("""
    SELECT f.name, fv.value
    FROM fields f
    JOIN fields_values fv ON f.id = fv.field_id
    WHERE f.id IN (SELECT field_id FROM categories_fields WHERE category_id = %s)
""", (1,))

# Создаем словарь из результатов
options = {row[0]: row[1] for row in cur.fetchall()}

# Преобразуем в JSON
options_json = json.dumps(options)

# Используем JSON в запросе к базе данных
cur.execute("""
    UPDATE preferences
    SET options = %s
    WHERE id = %s
""", (options_json, 1))

conn.commit()
cur.close()
conn.close()
