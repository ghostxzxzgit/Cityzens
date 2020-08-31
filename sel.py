from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
from helper import *


def get_follower_data(FollowerData):
    from selenium import webdriver

    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    print(userAgent)
    options.add_argument(f'user-agent={userAgent}')

    chromedriver_path = 'G:/Coding/chromedriver.exe' # Change this to your own chromedriver path!
    webdriver = webdriver.Chrome(chrome_options = options, executable_path = chromedriver_path)
    print("Manchester City Social Media Following")

    if FollowerData["FB"] == 0:
        FB = get_facebook(webdriver)
        FollowerData["FB"] = FB
    if FollowerData["Reddit"] == 0:
        Reddit = get_reddit(webdriver)
        FollowerData["Reddit"] = Reddit
    if FollowerData["YT"] == 0:
        YT = get_youtube(webdriver)
        FollowerData["YT"] = YT
    if FollowerData["Twitter"] == 0:
        Twitter = get_twitter(webdriver)
        FollowerData["Twitter"] = Twitter
    if FollowerData["Insta"] == 0:
        Insta = get_insta(webdriver)
        FollowerData["Insta"] = Insta
    webdriver.close()
    webdriver.quit()
    return FollowerData
