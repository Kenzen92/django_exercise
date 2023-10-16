from django.urls import path

from . import views

urlpatterns = [
    path("add-exercise", views.add_exercise, name="add-exercise"),
     path('exercise-list/', views.exercise_list, name='exercise-list'),
    path("", views.index, name="index"),
]