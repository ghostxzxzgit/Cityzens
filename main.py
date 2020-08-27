from sel import *
from helper import *

# usage : cd into dir and execute scheduler.py
# program would fetch data every 4 hours and once when execution of scheduler starts
# to interrupt execution ctrl+C anytime
# periodically commit FollowerData.csv to github
# TODO write the plotting function

if __name__ == '__main__':
    FollowerData = {'FB': 0, 'Reddit': 0, 'YT': 0, 'Twitter': 0, 'Insta': 0}
    while (not valid_data(FollowerData)):
        FollowerData = get_follower_data(FollowerData)

    # print(FollowerData)
    write_data(FollowerData)
