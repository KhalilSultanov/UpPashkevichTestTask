from rest_framework import serializers


class TransactionStatsSerializer(serializers.Serializer):
    total_spent = serializers.DecimalField(max_digits=12, decimal_places=2)
    by_category = serializers.DictField(child=serializers.DecimalField(max_digits=12, decimal_places=2))
    daily_average = serializers.DecimalField(max_digits=12, decimal_places=2)
