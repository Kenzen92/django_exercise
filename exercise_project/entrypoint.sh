#!/bin/sh

# Apply database migrations
python manage.py make migrations

python manage.py migrate

python manage.py collectstatic --noinput

# Start the Django development server
python manage.py runserver 0.0.0.0:8000
