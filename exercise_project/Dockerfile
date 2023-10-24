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

# Copy the entrypoint script
COPY entrypoint.sh /app/entrypoint.sh

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh


CMD ["/app/entrypoint.sh"]
