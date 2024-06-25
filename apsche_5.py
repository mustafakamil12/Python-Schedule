from time import sleep
from apscheduler.schedulers.background import BackgroundScheduler, BlockingScheduler

def display(msg):
    print(msg)    
    print(job_id)
    # job_id.remove()
    # scheduler.shutdown(wait=False)

scheduler = BlockingScheduler()
job_id = scheduler.add_job(display, 'interval', seconds = 3, args=["Hello World"])
if job_id:
    print('please note job id still available')
else:
    print('please advise job id not available any more')
scheduler.start()
