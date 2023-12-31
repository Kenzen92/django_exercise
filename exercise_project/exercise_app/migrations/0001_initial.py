# Generated by Django 4.2.6 on 2023-10-15 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the exercise', max_length=100)),
                ('description', models.TextField(blank=True, help_text='Description of the exercise (optional)')),
                ('category', models.CharField(help_text='Category of the exercise, e.g., cardio, strength, flexibility, etc.', max_length=50)),
                ('duration', models.PositiveIntegerField(help_text='Duration of the exercise in minutes')),
                ('date', models.DateField(help_text='Date when the exercise was performed')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
