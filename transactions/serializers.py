from rest_framework import serializers

from transactions.models import Transaction
from transactions.services.categorizer import CATEGORY_KEYWORDS, categorize


class TransactionStatsSerializer(serializers.Serializer):
    """
    Вывод статистики трат юзера
    """
    total_spent = serializers.DecimalField(max_digits=12, decimal_places=2)
    by_category = serializers.DictField(child=serializers.DecimalField(max_digits=12,
                                                                       decimal_places=2))
    daily_average = serializers.DecimalField(max_digits=12, decimal_places=2)


class TransactionImportSerializer(serializers.ModelSerializer):
    """
    Импорт транзакций

    Проверяет категорию на основе работы метода categorize()

    """

    category = serializers.CharField(required=False)

    class Meta:
        model = Transaction
        fields = ["user", "amount", "currency", "description", "merchant", "category", "timestamp"]

    def validate(self, data):
        description = data.get("description", "")
        merchant = data.get("merchant", "")
        auto_category = categorize(description, merchant)

        valid_categories = list(CATEGORY_KEYWORDS.keys()) + ["Other"]
        if not data.get("category") or data["category"] not in valid_categories:
            data["category"] = auto_category

        return data
