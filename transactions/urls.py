from django.urls import path

from .views import TransactionImportView, TransactionStatsView

urlpatterns = [
    path("users/<int:user_id>/stats/", TransactionStatsView.as_view(), name="user-stats"),
    path("transactions/import/", TransactionImportView.as_view(), name="transaction-import"),

]
