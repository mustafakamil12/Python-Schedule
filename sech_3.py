import helper
import schedule
import time


def task():
    print('Doing task...', helper.get_time())

schedule.every().minute.at(':15').do(task)
# schedule.every().hour.at(':15').do(task)

# schedule.every(2).minutes.at(':10').do(task)
# schedule.every(10).hours.at(':15').do(task)
# schedule.every().day.at('15:15:40').do(task)  # or '15:15'

# schedule.ever().monday.do(task)
# schedule.every().monday.at('15:15').do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
