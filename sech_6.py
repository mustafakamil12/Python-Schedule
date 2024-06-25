import helper
import schedule
import time

from schedule import repeat, every

@repeat(every(5).seconds,5,'Luigi')
@repeat(every(6).seconds,0,'Mario')
def task(arg1, arg2):
    print('Doing task...', f'args = {arg1, arg2}', helper.get_time())


while True:
    schedule.run_pending()
    time.sleep(1)
