from . import models


def habits_list_all():
    return models.Habit.objects.all()
