import logging
from datetime import date, timedelta
from decimal import Decimal

import pytest
from rest_framework.test import APIClient

from transactions.models import Transaction
from users.models import UserModel


@pytest.mark.django_db
def test_transaction_stats_success_with_data(caplog):
    client = APIClient()
    user = UserModel.objects.create(
        email="test@example.com",
        daily_limit=Decimal("1000.00"),
    )

    Transaction.objects.create(
        user=user,
        amount=Decimal("-1500.00"),
        currency="RUB",
        category="Transport",
        timestamp=date.today()
    )
    Transaction.objects.create(
        user=user,
        amount=Decimal("-900.00"),
        currency="RUB",
        category="Food",
        timestamp=date.today() - timedelta(days=1)
    )

    date_from = (date.today() - timedelta(days=1)).isoformat()
    date_to = date.today().isoformat()

    url = f"/api/users/{user.id}/stats/?from={date_from}&to={date_to}"
    with caplog.at_level(logging.WARNING):
        response = client.get(url)

    assert response.status_code == 200
    data = response.json()

    assert Decimal(data["total_spent"]) == Decimal("2400.00")
    expected = {
        "Transport": Decimal("1500.00"),
        "Food": Decimal("900.00")
    }
    actual = {k: Decimal(v) for k, v in data["by_category"].items()}
    assert actual == expected

    assert any("Превышение дневного лимита" in msg for msg in caplog.messages)


@pytest.mark.django_db
def test_transaction_stats_invalid_date_range():
    client = APIClient()
    user = UserModel.objects.create(
        email="user@example.com",
        daily_limit=Decimal("1000.00"),
    )

    url = f"/api/users/{user.id}/stats/"
    response = client.get(url + "?from=&to=")

    assert response.status_code == 400
    assert "Both 'from' and 'to'" in response.data["detail"]
