import helper
import schedule
import time


def task(arg1, arg2):
    print('Doing task...', f'args = {arg1, arg2}', helper.get_time())

schedule.every(5).seconds.do(task, 10, 'Mustafa')

while True:
    schedule.run_pending()
    time.sleep(1)
