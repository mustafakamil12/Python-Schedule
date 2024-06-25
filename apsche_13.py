from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR

def tasking_1():
    print("tasking_1")

def tasking_2():
    print("tasking_2")

def tasking_3():
    print("tasking_3")

def print_task():
    print("Task parent")

def my_listener(event):
    if event.exception:
        print('The job crashed :(')
    else:
        print('The parent job executed successfully!')
        tasking_1()
        tasking_2()
        tasking_3()

scheduler = BackgroundScheduler()
scheduler.add_job(print_task, 'interval', seconds=5)
scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
scheduler.start()

# try:
#     while True:
#         pass
# except (KeyboardInterrupt, SystemExit):
#     scheduler.shutdown()
