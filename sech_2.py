import helper
import schedule
import time


def task():
    print('Doing task...', helper.get_time())
taskName = "task"
part1 = "schedule"
value = '5'
part2 = f"every({value})"

part3 = "seconds"
part4 = f"do({taskName})"
my_command = part1 + '.' + part2 + '.' + part3 + '.' +part4  
exec(my_command)
# schedule.every(5).minutes.do(task)
# schedule.every(5).hours.do(task)
# schedule.every(5).days.do(task)
# schedule.every(5).weeks.do(task)

while True:
    schedule.run_pending()
    time.sleep(1)
# 00:00