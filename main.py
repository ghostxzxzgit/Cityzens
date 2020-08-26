from sel import *


if __name__ == '__main__':
    FollowerData = []
    while ((len(FollowerData)) != 5):
        FollowerData = get_follower_data()

    # print(FollowerData)
    write_data(FollowerData)
