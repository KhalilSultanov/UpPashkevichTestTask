from django.db import models


class UserModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    daily_limit = models.DecimalField(max_digits=10, decimal_places=2, default=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
