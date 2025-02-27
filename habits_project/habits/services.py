from django.shortcuts import get_object_or_404

from . import models


def habits_list_all():
    return models.Habit.objects.all()


def habit(id: int):
    return get_object_or_404(models.Habit, pk=id)
