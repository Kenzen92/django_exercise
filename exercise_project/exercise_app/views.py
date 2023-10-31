from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import AddExerciseForm
from .models import Exercise
from django.contrib.auth.decorators import login_required

@login_required
def add_exercise(request):
    if request.method == "POST":
        form = AddExerciseForm(request.POST)

        if form.is_valid():
            new_exercise = form.save()
            print("Form valid: ", new_exercise)
            return redirect(reverse_lazy('index'))
        else:
            # Print form errors
            print("Invalid form:", form.errors)
            return redirect(reverse_lazy('add_exercise'))
    else:
        context = {'form': AddExerciseForm()}
        return render(request, 'exercise_app/add_exercise.html', context)


def exercise_list(request):
    exercises = Exercise.objects.all()  # Replace 'Exercise' with your model name
    print(exercises)
    return render(request, 'exercise_app/exercise_list.html', {'exercises': exercises})


def index(request):
    return render(request, 'exercise_app/index.html')
