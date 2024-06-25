from apscheduler.schedulers.background import BackgroundScheduler
import time

# Define the function to be executed as the scheduled task
def my_task():
    print("Executing scheduled task...")
    # Simulate some work
    time.sleep(2)
    # Return a result
    return "Task completed successfully"

# Create a scheduler
scheduler = BackgroundScheduler()

# Add the task to the scheduler
scheduler.add_job(my_task, 'interval', seconds=5)

# Start the scheduler
scheduler.start()

# Wait for the task to execute
time.sleep(10)

# Check the execution result
# Note: This example assumes that the task returns a result
# If the task does not return a result, you may need to handle the result differently
job = scheduler.get_job('my_task')  # Get the job by its ID
if job:
    print("Last execution result:", job.result)
else:
    print("No such job found")

# Shut down the scheduler
scheduler.shutdown()
