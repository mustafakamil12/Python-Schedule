import helper
import schedule
import time

from schedule import repeat, every


# @repeat(every(5).seconds)           # Create task
# @repeat(every().minute.at(':30'))
@repeat(every(2).minutes.at(':17'))
def task():
    print('Doing task...', helper.get_time())

while True:
    schedule.run_pending()
    time.sleep(1)
