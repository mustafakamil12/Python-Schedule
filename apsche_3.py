from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler

def display():
    print("This function has been executed")
    print(job_id)
    job_id.remove()

scheduler = BlockingScheduler()
job_id = scheduler.add_job(display, 'interval', seconds = 3)

scheduler.start()