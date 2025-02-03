from django.urls import path

from . import views

urlpatterns = [
    path("new/", views.new_habit, name="new_habit"),
    path("", views.habits_list, name="habits_list"),
]
