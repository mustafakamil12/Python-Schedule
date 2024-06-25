import helper
import schedule
import time

def task():
    print('Doing task ...', helper.get_time())

    return schedule.CancelJob

schedule.every(5).seconds.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
    print('Jobs pending:', len(schedule.get_jobs()))
