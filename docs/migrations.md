## Работа с миграциями
- Alemic docs: https://alembic.sqlalchemy.org/en/latest/index.html

### Общие требования
1. Все команды выполняются из корня репозитория.
2. Нужно чтобы была поднята база данных PostgreSQL на `localhost:5432` и был создан пользователь `postgres` с паролем `postgres`. Целевая база данных `pers_routes_db`. Полный адрес базы данных на `localhost`: `postgresql://postgres:postgres@localhost:5432/pers_routes_db`.
3. Должна быть установлена библиоетка `alembic` в глобальном или виртуальном (`venv`) окружении. Лучше всё делать из `venv`.

### Команды
- Применение всех новых миграций: `alembic upgrade head`
- Применение отдельной миграции: `alembic upgrade <migration_id>`
- Откат всех миграций: `alembic downgrade base`