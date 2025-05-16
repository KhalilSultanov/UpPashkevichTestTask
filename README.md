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

## Запуск тестов

```bash
    poetry run pytest
```

---

## Автор

[**Khalil**](https://t.me/itskhalilS)
