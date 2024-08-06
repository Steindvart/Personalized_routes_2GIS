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

Маршруты
| Resourse   | Method  | Comment |
| --------   | ------- | ------- |
| /users/:id/routes | POST  | Запрос на формирование маршрута, текущие предпочтения в body json
