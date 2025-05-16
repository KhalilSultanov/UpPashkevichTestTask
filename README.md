# up-pashkevich-test-task

Тестовое задание для Up pashkevich.

## Стек

- Python 3.11
- Django
- Django REST Framework
- PostgreSQL
- Docker + Compose
- Poetry
- Swagger
- Ruff
- Pytest
- CI

### Склонируйте

```bash
    git clone https://github.com/KhalilSultanov/up-pashkevich-test-task.git
    cd up-pashkevich-test-task
````

### Запуск из Docker

Запустите на своем устройстве Docker Desktop, а затем выполните команду:

```bash
    docker compose up --build
```

API доступно в браузере по адресу:

* API docs: [http://localhost:8000/api/docs](http://localhost:8000/api/docs)

* Супер-пользователь для админки создастся автоматом (логин и пароль - admin)

## Запуск без Docker

### Установите зависимости Poetry

```bash
    poetry install --no-root
```

### Настройте .env

Создайте `.env` с таким же содержимым, как и в `.env.example`, но `POSTGRES_HOST=localhost`

### Миграции и запуск

```bash
    poetry run python manage.py migrate
    poetry run python manage.py createsuperuser
    poetry run python manage.py runserver
```

## Основные ручки

- `POST /api/transactions/import/` — импорт транзакций
- `GET /api/users/<user_id>/stats/` — статистика трат по дням и категориям

- `GET /api/users/` — получить всех юзеров
- `POST /api/users/` — создать нового юзера

Вот готовый раздел для README с примерами ручек и JSON-запросов:

---

Вот оформленный и структурированный раздел **Примеры API-запросов** для `README.md`:

---

## Примеры API-запросов

### Пользователи

#### Получить список пользователей

```http
GET /api/users/
```

**Ответ:**

```json
[
  {
    "id": 1,
    "name": "Иван Иванов",
    "email": "ivan@example.com"
  }
]
```

---

#### Создать нового пользователя

```http
POST /api/users/
Content-Type: application/json
```

**Тело запроса:**

```json
{
  "name": "Иван Иванов",
  "email": "ivan@example.com"
}
```

**Ответ:**

```json
{
  "id": 1,
  "name": "Иван Иванов",
  "email": "ivan@example.com"
}
```

---

### Транзакции

#### Импорт транзакций

```http
POST /api/transactions/import/
Content-Type: application/json
```

**Тело запроса:**

```json
[
  {
    "user": 1,
    "amount": "-1500.00",
    "currency": "RUB",
    "description": "Покупка кофе",
    "merchant": "Starbucks",
    "category": "string",
    "timestamp": "2025-05-15T10:00:00"
  },
  {
    "user": 1,
    "amount": "-3500.00",
    "currency": "RUB",
    "description": "Продукты",
    "merchant": "Magnit",
    "category": "string",
    "timestamp": "2025-05-15T18:00:00"
  }
]
```

**Ответ:**

```json
{
  "detail": "Transactions imported successfully"
}
```

> `user` — это ID пользователя. Предварительно создайте его через `/api/users/` или админку.

---

### Статистика

#### Получить статистику трат пользователя

```http
GET /api/users/1/stats/?from=2025-05-01&to=2025-05-16
```

**Ответ:**

```json
{
  "total_spent": "5000.00",
  "by_category": {
    "Food": "3500.00",
    "Coffee": "1500.00"
  },
  "daily_average": "312.50"
}
```

---

## Запуск тестов

```bash
    poetry run pytest
```

---

## Автор

[**Khalil**](https://t.me/itskhalilS)
