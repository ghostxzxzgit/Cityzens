from sel import *

# usage : cd into dir and execute scheduler.py
# program would fetch data every 4 hours and once when execution of scheduler starts
# to interrupt execution ctrl+C anytime
# periodically commit FollowerData.csv to github
# TODO write the plotting function
# TODO if all 5 platforms dont return data at first attempt,
#  only retry the unsucessful platform not all of them again

if __name__ == '__main__':
    FollowerData = []
    while ((len(FollowerData)) != 5):
        FollowerData = get_follower_data()

    # print(FollowerData)
    write_data(FollowerData)
