from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from datetime import datetime

def display(msg):
    print("Message: ", msg)    
    # print(job_id)
    # job_id.remove()
    # scheduler.shutdown(wait=False)

scheduler = BlockingScheduler()
scheduler.add_job(display, 'date', run_date = datetime(2024,5,13,1,42,0), args=["Job 1"])


scheduler.start()
sleep(10)