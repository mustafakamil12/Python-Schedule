import helper
import schedule
import time

from schedule import repeat, every

# @repeat(every(10).seconds)
def task():
    print('Doing task...', helper.get_time())

# schedule.every(5).seconds.do(task)
# schedule.every(5).minutes.do(task)
# schedule.every(5).hours.do(task)
# schedule.every(5).days.do(task)
# schedule.every(5).weeks.do(task)

# schedule.every().minute.at(':15').do(task)
# schedule.every().hour.at(':15').do(task)

# schedule.every(10).hour.at(':15').do(task)
# schedule.every().day.at('15:15:40').do(task)

# schedule.ever().monday.do(task)
# schedule.every().monday.at('15:15').do(task)

# @repeat(every(5).seconds, 5, 'Mustafa')
# @repeat(every(6).seconds, 0, 'Mario')
# def task(arg1, arg2):
#     print('Doing task...', f'args = {arg1, arg2}', helper.get_time())


# schedule.every(5).seconds.do(task, 10, 'Mustafa')

# schedule.cancel_job(task)
# print(schedule.get_jobs())

# while True:
#     schedule.run_pending()
#     time.sleep(1)

# -------- using job for 1 time ----------

# def task():
#     print('Doing task ...', helper.get_time())

#     return schedule.CancelJob

# schedule.every(5).seconds.do(task)
# schedule.every(5).seconds.do(task)
# schedule.every(5).seconds.do(task)
# schedule.every(5).seconds.do(task)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
#     print('Jobs:', len(schedule.get_jobs()))
#     schedule.clear()

# schedule.every().minute.do(task).tag('work', '1')
# schedule.every().hour.do(task).tag('fun', '1')
# schedule.every().day.do(task).tag('work', '2')
# schedule.every().week.do(task).tag('fun', '2')

# fun = schedule.get_jobs('fun')
# work = schedule.get_jobs('work')

# print(fun)
# print(work)

# while True:
#     schedule.run_pending()
#     print('Jobs:', len(schedule.get_jobs()))
#     schedule.clear('fun')
#     time.sleep(1)

# schedule.every(1).to(10).seconds.do(task)
# schedule.every(10).seconds.until('13:14').do(task)

# schedule.every().monday.at('10:00').do(task)
# schedule.every().tuesday.at('15:00').do(task)

# schedule.run_all(delay_seconds=1)

# while True:
#     schedule.run_pending()
#     time.sleep(1)

