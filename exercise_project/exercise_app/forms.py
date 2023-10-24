from django import forms
from datetime import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse_lazy
from .models import Exercise


class AddExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'category', 'duration', 'date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('add-exercise')
        self.helper.add_input(Submit('submit', 'Submit'))
        # Update the 'date' field to use the DateInput widget
        self.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
