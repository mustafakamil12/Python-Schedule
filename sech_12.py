import helper
import schedule
import time
from datetime import datetime


def task():
    print('Doing task...', helper.get_time())

#schedule.every(1).to(10).seconds.until('14:30').do(task)
schedule.every(1).to(10).seconds.until(datetime(2024,8,5,14,58,40)).do(task)


while True:
    schedule.run_pending()
    time.sleep(1)