from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import AddExerciseForm
from .models import Exercise


def add_exercise(request):
    if request.method == "POST":
        form = AddExerciseForm(request.POST)
        if form.is_valid():
            new_exercise = form.save()
            print("Form valid: ", new_exercise)
            return redirect(reverse_lazy('index'))
    else:
        context = {'form': AddExerciseForm()}
        return render(request, 'exercise_app/add_exercise.html', context)


def exercise_list(request):
    exercises = Exercise.objects.all()  # Replace 'Exercise' with your model name
    print(exercises)
    return render(request, 'exercise_app/exercise_list.html', {'exercises': exercises})


def index(request):
    return render(request, 'exercise_app/index.html')


