"""# Referrences :
# https://stackoverflow.com/questions/44779786/how-to-run-python-script-from-linux-terminal-every-hour
# https://stackoverflow.com/questions/22715086/scheduling-python-script-to-run-every-hour-accurately
# https://apscheduler.readthedocs.io/en/stable/userguide.html
# https://stackoverflow.com/questions/373335/how-do-i-get-a-cron-like-scheduler-in-python

# %run scheduler.py doesnt work there is just no way to kill the program
# JUST COPY THE ENTIRE THING IN IPYTHON AND RUN IT ... LET IT RUN
import os
from apscheduler.schedulers.blocking import BlockingScheduler
# from apscheduler.schedulers.background import BackgroundScheduler

os.chdir(r"G:/Coding/Projects/City")
print(os.getcwd())


def job():
    exec(open('test.py').read())


scheduler = BlockingScheduler()


def stop_job():
    A = input()
    if
    if isinstance(A, str):
        scheduler.shutdown(wait=False)



scheduler.add_job(job, "interval", seconds=20)
scheduler.add_job(stop_job, "interval", seconds=10)
scheduler.start()
"""

import schedule


def job():
    print("I'm working...")


schedule.every(1).hour.do(job)
job()
while True:
    schedule.run_pending()