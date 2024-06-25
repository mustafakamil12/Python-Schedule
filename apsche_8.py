from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler

def display(msg):
    print("Message: ", msg)    
    # print(job_id)
    # job_id.remove()
    # scheduler.shutdown(wait=False)

scheduler = BackgroundScheduler()
scheduler.add_job(display, 'interval', seconds = 3, args=["Job 1"])
scheduler.add_job(display, 'interval', seconds = 5, args=["Job 2"])

scheduler.start()
print("Hello World")