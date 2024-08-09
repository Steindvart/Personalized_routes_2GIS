## Запуск виртуального окружения
1. Развернуть вирутальное окружение: `python -m venv venv`
2. Активировать **venv**:
    - Windows: `.\venv\Scripts\activate`
    - Unix/MacOS: `source venv/bin/activate`
3. Установить зависимости: `pip install -r requirements.txt`

## Запуск сервера
- `uvicorn main:app --reload`
- При стандартных настройках, сервер будет доступен по `http://127.0.0.1:8000`