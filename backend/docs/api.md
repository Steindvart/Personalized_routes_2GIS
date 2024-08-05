### API endpoints

root: {url}/api

Users
| Resourse   | Method  | Comment |
| --------   | ------- | ------- |
| /users     | POST    | Создать пользователя
| /users     | GET    | Получить список пользователей
| /users/:id | GET     | Получить данные пользователя (его постоянные предпочтения)
| /users/:id | DELETE  | Удалить пользователя
| /users/:id:/liking | POST | Создать/Обновить предпочтения пользователя

Предпочтения (справочник)
| Resourse   | Method  | Comment |
| --------   | ------- | ------- |
| /tags | POST  | Расширить справочник предпочтений
| /tags     | GET   | Получить справочник предпочтений
| /tags/:id | DELETE     | Удалить запись из справочника предпочтений

Маршруты
| Resourse   | Method  | Comment |
| --------   | ------- | ------- |
| /users/:id/routes | POST  | Создать запрос на формирование маршрута
| /users/:id/routes     | GET   | Получить список маршрутов
| /users/:id/routes/:id | GET   | Получить детализацию маршрута
| /users/:id/routes/:id | PATCH   | Изменить атрибуты маршрута
| /users/:id/routes/:id | DELETE   | Удалить маршрут
