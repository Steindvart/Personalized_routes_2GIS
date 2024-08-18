## Запуск виртуального окружения
1. Развернуть вирутальное окружение: `python -m venv venv`
2. Активировать **venv**:
    - Windows: `.\venv\Scripts\activate`
    - Unix/MacOS: `source venv/bin/activate`
3. Установить зависимости: `pip install -r requirements.txt`
4. Creat **.env** file in /backend:
```
T_GIS_API_KEY=<key here>
GIGA_CHAT_API_TOKEN=<key here>

DB_HOST=localhost
DB_PORT=5432
DB_NAME=pers_routes_db
DB_USER=postgres
DB_PASS=postgres
```

## Запуск сервера
- `python ./main.py`
- При стандартных настройках, сервер будет доступен по `http://127.0.0.1:8000`