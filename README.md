## Проект "Умные путешествия" для хакатона в 2GIS

Генерация маршрутов для прогулки или небольшого путешествия, на основе постоянных и текущих предпочтений пользователя. С интерактивными комментариями об интересных местах поблизости в реальном времени.

### Команда
- Тимлид, Fullstack: **Калашников Иван** –> s21: gehnaeli | [Telegram](https://t.me/ivank_t) | [GitHub](https://github.com/Steindvart)
#### Frontend
- **Георгий Одияк** -> s21: riderkri | [Telegram](https://t.me/Jack_ONeill5) | [GitHub](https://github.com/Georgiy-JO)
- **Лиза Мурзакова** -> s21: regeniae | [Telegram](https://t.me/loco151416)

#### Backend
- **Егор Неделькин** -> s21: elenorau | [Telegram](https://t.me/egorgavai) | [GitHub](https://github.com/xenonlly)

#### Data Bases (Backend)
- Head: **Дарья Решетникова** -> s21: braavoss | [Telegram](https://t.me/reshetnikova_d) | [GitHub](https://github.com/reDasha)

#### ML/AI
- Head: **Татьяна Аксёнова** -> s21: ulrickro | [Telegram](https://t.me/tatavictorovna) | [GitHub](https://github.com/aksenovatv)
- **Павел** -> s21: jaycemar | [Telegram](https://t.me/jaycemar) | [GitHub](https://github.com/jaycemarpeer)

## Описание
### Основа

1. Персональные маршруты, которые строятся на основе как постоянных, так и текущих пользовательских предпочтений:
    - Постоянные предпочтения: любимые категории мест, их стиль, особенности, рейтинг и т.п.
    - Текущие предпочтения: способ передвижения пользователя, настроение, расстояние до мест, время работы, средний чек (если коммерция), время, которое пользователь может потратить на маршрут и тд.
2. Начальные данные берутся из опроса пользователя о его предпочтениях. Как, например, это сделано в Яндекс.Музыке. На основании этих данных строится рекомендательная модель (например, на основе алгоритмы k-ближайших соседей). Дальше эта модель может дополняться на основе отзывов пользователя о местах, маршрутах, вовлечённости в маршрут и т.п.
3. Рекомендательная модель, строит список мест учитывая текущие предпочтения (текущий запрос) и постоянные предпочтения (данные, собранные ранее). Из этих мест прокладывается маршрут.
    - Можно добавить функцию сохранения часто используемых маршрутов и возможность делиться маршрутами с другими пользователями.
4. Маршрут предоставляется пользователю – он может его принять или же скорректировать запрос, чтобы получить другой.

### Дополнительно

1. Маршрут может комментировать языковая модель (типа Алиса голосом или просто чат-бот). Например, пользователь приближается к тому или иному примечательному месту (не обязательно чтобы оно было в маршруте - можно сделать как доп. настройка) и ему будет выдаваться интересный факт, история об этом месте.
   - Возможность выбирать различные стили комментариев (исторический, развлекательный, познавательный) и многократность настроек на основе предпочтений пользователя.
   - Как логическое продолжение, комментатор маршрута можно выделить в отдельный сервис, который будет работать и для обычных маршрутов, в обычном режиме (при включенной опции). Например, "слева от вас - место, где все фотографируются (по фотобазе)", "самая вкусная в городе шаурма справа по ходу вашего движения (по отзывам)", "в доме напротив пять подвальных этажей", "если захотите переплыть Обь в этом месте, вам потребуются 50 минут и вторая жизнь"...

## Технологии
### Backend
- Python
- FastAPI
- PostgreSQL

### ML/AI
- PyTorch
- scikit-learn
- pandas, NumPy
- Интеграция с ChatGPT/YandexGPT/GigaChat

### Frontend
- Vue.js
- Nuxt.js + Vuetify

## Польза
### Для людей
- Получение маршрутов по местам, соответствующих индивидуальным предпочтениям и потребностям, будь то их особенности, любимые категории (рестораны, музеи, парки) или удобные способы передвижения.
- Возможность открыть для себя что-то новое через запрос маршрута другим путём или по новым местам, которые уже, наоборот, отличаются от постоянных предпочтений.
- Проще найти куда сходить в зависимости от компании, настроения и других факторов.
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
