from django.shortcuts import render

from . import services


def new_habit(request):
    pass


def habits_list(request):
    habits = services.habits_list_all()
    template = "habits/habits_list.html"
    context = {
        "habits": habits,
    }
    return render(request, template, context)


def habit_detail(request, id):
    habit = services.habit(id)
    template = "habits/habit_detail.html"
    context = {
        "habit": habit,
    }
    return render(request, template, context)