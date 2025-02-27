from django.urls import path

from . import views


app_name = "habits"
urlpatterns = [
    path("new/", views.new_habit, name="new_habit"),
    path("", views.habits_list, name="habits_list"),
    path("habit/<int:id>", views.habit_detail, name="habit_detail"),
]
