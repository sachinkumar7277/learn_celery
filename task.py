# tasks.py
from celery import Celery

# Create a Celery instance
app = Celery('tasks', broker='pyamqp://guest@localhost//')  # Replace 'localhost' with your message broker server if needed.

# Define the Celery task
@app.task
def add(x, y):
    return x + y
