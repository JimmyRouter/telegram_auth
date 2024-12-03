from django.contrib.auth.models import User
from django.db import models

class TelegramUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telegram_id = models.CharField(max_length=100, unique=True)
    telegram_username = models.CharField(max_length=100, null=True, blank=True)
    is_authenticated = models.BooleanField(default=False)  # Флаг для авторизации

    def __str__(self):
        return self.telegram_username or str(self.user)