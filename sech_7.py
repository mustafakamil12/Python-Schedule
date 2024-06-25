import helper
import schedule
import time

def task():
    print('Doing task ...', helper.get_time())


schedule.cancel_job(task)

print('Jobs:', len(schedule.get_jobs()))

while True:
    schedule.run_pending()
    time.sleep(1)