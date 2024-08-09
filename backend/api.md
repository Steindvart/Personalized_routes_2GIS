### API endpoints

root: {url}/api

Users
| Resourse   | Method  | Comment |
| --------   | ------- | ------- |
| /users     | POST    | Создать пользователя
| /users     | GET    | Получить список пользователей
| /users/:id | GET     | Получить данные пользователя (его постоянные предпочтения)
| /users/:id | DELETE  | Удалить пользователя

Постоянные предпочтения пользователя
| Resourse   | Method  | Comment |
| /users/:id:/preferences | GET | Получить предпочтения пользователя
| /users/:id:/preferences | POST | Обновить предпочтения пользователя (изначально считается, что у пользователя нет предпочтений)

Маршруты
| Resourse   | Method  | Comment |
| --------   | ------- | ------- |
| /users/:id/routes | POST  | Запрос на формирование маршрута, текущие предпочтения в body json
