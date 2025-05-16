import logging

from django.db.models import Sum
from django.utils.timezone import is_aware, make_aware

logger = logging.getLogger(__name__)


def check_user_limits(user, amount, tx_datetime):
    if not is_aware(tx_datetime):
        tx_datetime = make_aware(tx_datetime)

    day_total = user.transactions.filter(
        timestamp__date=tx_datetime.date()
    ).aggregate(total=Sum('amount'))['total'] or 0

    new_day_total = day_total + amount

    if abs(new_day_total) > user.daily_limit:
        logger.warning(f"[DAILY] Limit exceeded:"
                       f" {abs(new_day_total)} > {user.daily_limit} (User: {user.email})")
