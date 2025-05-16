from datetime import datetime
from decimal import Decimal
from unittest.mock import MagicMock, patch

from django.utils.timezone import make_aware

from users.utils import check_user_limits


def test_check_user_limits_logs_warning_when_limit_exceeded():
    user = MagicMock()
    user.email = "test@example.com"
    user.daily_limit = Decimal("1000.00")

    user.transactions.filter().aggregate.return_value = {"total": Decimal("-800.00")}

    amount = Decimal("-300.00")
    tx_datetime = make_aware(datetime(2024, 11, 1, 12, 0, 0))

    with patch("users.utils.logger") as mock_logger:
        check_user_limits(user, amount, tx_datetime)

        mock_logger.warning.assert_called_once()
        assert "[DAILY] Limit exceeded" in mock_logger.warning.call_args.args[0]


def test_check_user_limits_no_warning_when_within_limit():
    user = MagicMock()
    user.email = "test@example.com"
    user.daily_limit = Decimal("1000.00")

    user.transactions.filter().aggregate.return_value = {"total": Decimal("-300.00")}

    amount = Decimal("-200.00")
    tx_datetime = make_aware(datetime(2024, 11, 1, 9, 0, 0))

    with patch("users.utils.logger") as mock_logger:
        check_user_limits(user, amount, tx_datetime)

        mock_logger.warning.assert_not_called()
