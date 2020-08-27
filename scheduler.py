# Referrences :
# https://stackoverflow.com/questions/44779786/how-to-run-python-script-from-linux-terminal-every-hour
# https://stackoverflow.com/questions/22715086/scheduling-python-script-to-run-every-hour-accurately
# https://apscheduler.readthedocs.io/en/stable/userguide.html
# https://stackoverflow.com/questions/373335/how-do-i-get-a-cron-like-scheduler-in-python

# %run scheduler.py doesnt work there is just no way to kill the program
# JUST COPY THE ENTIRE THING IN IPYTHON AND RUN IT ... LET IT RUN
import os
import schedule
from datetime import datetime

os.chdir(r"G:/Coding/Projects/City")
print(os.getcwd())


def job():
    print("Starting execution :", datetime.now().time())
    exec(open('main.py').read())


schedule.every(1).hour.do(job)
job()
while True:
    schedule.run_pending()
