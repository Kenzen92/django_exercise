from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AddExerciseForm
from .models import Exercise



def add_exercise(request):
    context = {'form': AddExerciseForm()}
    return render(request, 'exercise_app/add_exercise.html', context)

def exercise_list(request):
    exercises = Exercise.objects.all()  # Replace 'Exercise' with your model name
    return render(request, 'exercise_app/exercise_list.html', {'exercises': exercises})


def index(request):
    return render(request, 'exercise_app/index.html')


