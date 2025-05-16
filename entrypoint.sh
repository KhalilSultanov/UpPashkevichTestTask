#!/bin/sh

echo "==> Running migrations..."
poetry run python manage.py migrate

echo "==> Creating superuser..."
poetry run python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@example.com', 'admin')
    print("Superuser created.")
else:
    print("Superuser already exists.")
END

echo "==> Starting Django server..."
poetry run python manage.py runserver 0.0.0.0:8000
