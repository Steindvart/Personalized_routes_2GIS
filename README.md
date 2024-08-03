## Проект "Персональные маршруты с AI" для хакатона в 2GIS

### Команда
- Тимлид, Fullstack: **Калашников Иван** –> s21: gehnaeli | [GitHub](https://github.com/Steindvart) | [Telegram](https://t.me/ivank_t)
-

## Описание
### Основа

1. Персонализированные маршруты, которые строятся на основе постоянных пользовательских предпочтений:
    - Любимые категории мест, их стиль, особенности, рейтинг, расстояние до них, время работы, средний чек (если коммерция).
    - Способ передвижения пользователя, время, которое пользователь может потратить на маршрут и тд.
2. Начальные данные берутся из опроса пользователя о его предпочтениях. Как, например, это сделано в Яндекс.Музыке. На основании этих данных строится рекомендательная модель (например, на основе алгоритмы k-ближайших соседей). Дальше эта модель может дополняться на основе отзывов пользователя о местах, маршрутах, вовлечённости в маршрут и т.п.
3. Рекомендательная модель, строит список мест учитывая текущий запрос (текущие предпочтения) и постоянные предпочтения (данные, собранные ранее). Дальше из этих мест строится маршрут.
    - Можно добавить функцию сохранения часто используемых маршрутов и возможность делиться маршрутами с другими пользователями.
4. Маршрут предоставляется пользователю – он может его принять или же скорректировать запрос, чтобы получить другой.

### Дополнительно

1. Маршрут может комментировать языковая модель (типа Алиса голосом или просто чат-бот). Например, пользователь приближается к тому или иному примечательному месту (не обязательно чтобы оно было в маршруте - можно сделать как доп. настройка) и ему будет выдаваться интересный факт, история об этом месте.
   - Возможность выбирать различные стили комментариев (исторический, развлекательный, познавательный) и многократность настроек на основе предпочтений пользователя.
   - Как логическое продолжение, комментатор маршрута можно выделить в отдельный сервис, который будет работать и для обычных маршрутов, в обычном режиме (при включенной опции). Например, "слева от вас - место, где все фотографируются (по фотобазе)", "самая вкусная в городе шаурма справа по ходу вашего движения (по отзывам)", "в доме напротив пять подвальных этажей", "если захотите переплыть Обь в этом месте, вам потребуются 50 минут и вторая жизнь"...

## Технологии
### Backend
- Python
- Django
- PostgreSQL

### ML/AI
- PyTorch
- scikit-learn
- pandas, NumPy
- Интеграция с ChatGPT/YandexGPT/GigaChat

### Frontend
- Vue.js
- Nuxt.js

## Польза
### Для людей
- Получение маршрутов по местам, соответствующих индивидуальным предпочтениям и потребностям, будь то их особенности, любимые категории (рестораны, музеи, парки) или удобные способы передвижения.
- Возможность открыть для себя что-то новое через запрос маршрута другим путём или по новым местам, которые уже, наоборот, отличаются от постоянных предпочтений.
- Проще найти куда сходить в новом месте в зависимости от компании, настроения и других факторов.
- Маршруты по достопремичательностям, а также комментарии и рассказы о них добавляют образовательную ценность маршрутам, делая путешествия более интересными и информативными.

#### Примеры
- Анна хочет провести день в городе и изучить новые места. На основе её предпочтений приложение предлагает маршрут, включающий посещение уютного кафе на завтрак, прогулку по парку, посещение музея и ужин в ресторане с хорошими отзывами. Анна получает также уведомления с интересными фактами о местах, которые она проходит.
- (доработать) "Золотая миля" - система строит тебе милю по барам.

### Для бизнеса и общества
- Увеличение потока клиентов: маршруты могут включать предложения для посещения определенных мест, что увеличивает поток клиентов в конкретные заведения.
- Анализ данных и целевая реклама: система собирает и анализирует данные о предпочтениях и поведении пользователей, что помогает бизнесу лучше понимать свою аудиторию и улучшать свои предложения.
- Промоакции: специальные акции и скидки пользователям, которые включают определённые заведения в свои маршруты.
- Повышение лояльности клиентов: предоставление персонализированных маршрутов и рекомендаций повышает удовлетворенность клиентов и их лояльность к платформе.
- Новые возможности для партнёрства: включение партнерских заведений в рекомендуемые маршруты может стать основой для взаимовыгодного сотрудничества и партнерских программ.
- Развитие туризма: возможность получать персонализованные маршруты может мотивировать людей к более активным путешествиям как по привычным местам, открывая в них что-то новое, так и в поездках.

#### Примеры
- Кафе "Good Coffee" становится партнером проекта. Алгоритм учитывает это кафе при построении маршрутов для пользователей, которые ищут уютные места для завтрака или обеда. Кафе видит увеличение потока новых клиентов, а пользователи получают дополнительные скидки и акции, предложенные кафе.

