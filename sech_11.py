import helper
import schedule
import time


def task():
    print('Doing task...', helper.get_time())

schedule.every(1).to(10).seconds.do(task)


while True:
    schedule.run_pending()
    time.sleep(1)