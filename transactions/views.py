from django.db.models import Sum
from django.utils.dateparse import parse_date
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from transactions.models import Transaction
from transactions.serializers import TransactionStatsSerializer
from users.models import UserModel


@extend_schema(
    tags=["Transactions"],
    parameters=[
        OpenApiParameter(
            name="from",
            type=OpenApiTypes.DATE,
            required=True,
            location=OpenApiParameter.QUERY,
            description="Start date in format YYYY-MM-DD"
        ),
        OpenApiParameter(
            name="to",
            type=OpenApiTypes.DATE,
            required=True,
            location=OpenApiParameter.QUERY,
            description="End date in format YYYY-MM-DD"
        ),
    ]
)
class TransactionStatsView(APIView):
    def get(self, request, user_id):
        date_from = parse_date(request.query_params.get("from"))
        date_to = parse_date(request.query_params.get("to"))

        if not date_from or not date_to:
            return Response({"detail": "Both 'from' and 'to' dates are required in YYYY-MM-DD format."},
                            status=status.HTTP_400_BAD_REQUEST)

        user = get_object_or_404(UserModel, id=user_id)

        transactions = Transaction.objects.filter(
            user=user,
            timestamp__date__gte=date_from,
            timestamp__date__lte=date_to
        )

        total_spent = transactions.aggregate(total=Sum("amount"))["total"] or 0

        by_category_qs = transactions.values("category").annotate(total=Sum("amount"))
        by_category = {entry["category"]: entry["total"] for entry in by_category_qs}

        days_count = (date_to - date_from).days + 1
        daily_average = total_spent / days_count if days_count > 0 else 0

        data = {
            "total_spent": abs(total_spent),
            "by_category": {k: abs(v) for k, v in by_category.items()},
            "daily_average": abs(daily_average)
        }

        serializer = TransactionStatsSerializer(data)
        return Response(serializer.data)
