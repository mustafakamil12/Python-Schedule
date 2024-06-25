from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler
from datetime import datetime

def display(msg):
    print("Message: ", msg)    
    # print(job_id)
    # job_id.remove()
    # scheduler.shutdown(wait=False)

scheduler = BlockingScheduler()
# scheduler.add_job(display, 'cron', hour=19, second='*', args=["Job 1"])
# scheduler.add_job(display, 'cron', hour=19, second='*/5', args=["Job 1"])
# scheduler.add_job(display, 'cron', month = '1-8', hour=19, second='*/3', args=["Job 1"])
scheduler.add_job(display, 'cron', month = '1-5,7-8', hour=22, second='*/3', args=["Job 1"])
# scheduler.add_job(display, 'cron', args=["Job 1"], day = 13, second=30)
# scheduler.add_job(display, 'cron', args=["Job 1"], day = 13, minute = 35, second=30)
# scheduler.add_job(display, 'cron', args=["Job 1"], day = 13, hour = 22, second=30)
scheduler.start()
sleep(10)