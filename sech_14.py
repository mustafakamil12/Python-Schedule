import helper
import schedule
import time
import threading


def task():
    print('Doing task...', helper.get_time())
    time.sleep(5)


def start_thread(func):
    job_one = threading.Thread(target=func)
    job_one.start()

schedule.every(1).seconds.do(start_thread, task)

while True:
    schedule.run_pending()
    time.sleep(1)

