from django.db import models

# Create your models here.
from django.db import models

class Exercise(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the exercise")
    description = models.TextField(blank=True, help_text="Description of the exercise (optional)")
    category = models.CharField(max_length=50, help_text="Category of the exercise, e.g., cardio, strength, flexibility, etc.")
    duration = models.PositiveIntegerField(help_text="Duration of the exercise in minutes")
    date = models.DateField(help_text="Date when the exercise was performed")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
