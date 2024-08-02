## Проект "Персонализованные маршруты с AI" для хакатона в 2GIS

### Команда
- Тимлид, Fullstack – @steindvart | gehnaeli
-

## Описание (набросок)

1. Персонализированные маршруты, которые строятся на основе пользовательских предпочтений: любимые категории мест, их стиль (?), способ передвижения пользователя, расстояние, отзывы, время работы, средний чек (если коммерция), время, которое пользователь может на это потратить и тд.
2. Начальные данные берутся из опроса пользователя о его предпочтениях. Как, например, это сделано в Яндекс.Музыке. На основании этих данных строится рекомендательная модель (например, на основе алгоритмы k-ближайших соседей). Дальше эта модель может дополняться на основе отзывов пользователя о тех или иных маршрутах, местах и тд.
3. Рекомендательная модель, строит список мест учитывая текущий запрос (текущие предпочтения) и постоянные предпочтения (данные, собранные ранее). Дальше из этих мест строится маршрут.
4. Маршрут предоставляется пользователю – он может его принять или же скорректировать запрос, чтобы получить другой.
5. + Как дополнение – маршрут может комментировать языковая модель (типа Алиса голосом, или просто чат-бот). Например, пользователь приближается к тому или иному примечательному месту (не обязательно чтобы оно было в маршруте - можно сделать как доп. настройка) и ему будет выдаваться интересный факт, история об этом месте.