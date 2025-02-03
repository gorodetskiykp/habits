from django.db import models
from django.contrib.auth.models import User


class Habit(models.Model):
    title = models.CharField(verbose_name="Привычка", max_length=200)
    created_at = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Дата изменения", auto_now=True)
    owner = models.ForeignKey(User, verbose_name="Владелец привычки", on_delete=models.CASCADE, related_name="habits")
    
    class Meta:
        ordering = "owner", "-created_at"
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"{self.title} - {self.created_at}"
