import helper
import schedule
import time


def task():
    print('Doing task...', helper.get_time())

schedule.every().minute.do(task).tag('work', '1')
schedule.every().hour.do(task).tag('fun', '1')
schedule.every().day.do(task).tag('work', '2')
schedule.every().week.do(task).tag('fun', '2')

fun = schedule.get_jobs('fun')
work = schedule.get_jobs('work')

print(fun)
print(work)

while True:
    schedule.run_pending()
    print('Jobs:', len(schedule.get_jobs()))
    schedule.clear('fun')
    time.sleep(1)