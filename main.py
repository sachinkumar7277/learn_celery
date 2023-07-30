# main.py
from task import add

result = add.delay(4, 6)  # This will queue the task for execution.
print("Task queued. Result will be available shortly.")
