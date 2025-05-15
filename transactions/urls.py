from django.urls import path
from .views import TransactionStatsView

urlpatterns = [
    path("users/<int:user_id>/stats/", TransactionStatsView.as_view(), name="user-stats"),
]
