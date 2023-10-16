# Use the official Python image as a parent image
FROM python:latest

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE=exercise_project.settings

# Set the working directory
WORKDIR /app

# Copy the project files into the container
COPY exercise_project/ /app/

# Install dependencies
COPY requirements.txt /app/
RUN pip install -r requirements.txt


# Expose the port that Django runs on (default is 8000)
EXPOSE 8000

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
