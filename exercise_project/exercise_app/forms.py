from django import forms
from datetime import datetime
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.urls import reverse_lazy
# from .models import Exercise

subjectChoices = (
    (1, 'Web development'),
    (2, 'Pussyclaarting'),
    (3, 'Skullduggery')
)

class AddExerciseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = reverse_lazy('index')
        self.helper.add_input(Submit('submit', 'Submit'))


    name = forms.CharField()
    age = forms.IntegerField()
    subject_choice = forms.ChoiceField(
    choices = subjectChoices,
    widget= forms.RadioSelect)
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'max': datetime.now().date()})
    )