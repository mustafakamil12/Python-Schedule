import helper
import schedule
import time


def task():
    print('Doing task...', helper.get_time())

schedule.every().monday.at('10:00').do(task)
schedule.every().tuesday.at('15:00').do(task)

# schedule.run_all()
schedule.run_all(delay_seconds=1)


while True:
    schedule.run_pending()
    time.sleep(1)