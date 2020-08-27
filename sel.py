from fake_useragent import UserAgent
from selenium.webdriver.chrome.options import Options
import re
from helper import *
from datetime import datetime
import selenium


def get_follower_data():
    from selenium import webdriver
    FollowerData = []

    options = Options()
    ua = UserAgent()
    userAgent = ua.random
    print(userAgent)
    options.add_argument(f'user-agent={userAgent}')

    chromedriver_path = 'C:/Users/unitel/Downloads/chromedriver.exe'  # Change this to your own chromedriver path!
    webdriver = webdriver.Chrome(chrome_options=options, executable_path=chromedriver_path)
    print("Manchester City Social Media Following")

    facebook = "https://www.facebook.com/mancity"
    webdriver.get(facebook)

    try:
        followers = webdriver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div")
        data = followers.text
        regex = "([\d|,]+)"
        number = re.findall(regex, data)
        intnumber = int(number[0].replace(',', ''))
        FollowerData.append(intnumber)
        print("Facebook followers :", intnumber)
    except selenium.common.exceptions.NoSuchElementException:
        pass

    reddit = "https://www.reddit.com/r/MCFC/"

    webdriver.get(reddit)

    try:
        followers = webdriver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div")
        intnumber = parse_numbers(followers.text)
        print("Reddit subscribers :", intnumber)
        FollowerData.append(intnumber)
    except selenium.common.exceptions.NoSuchElementException:
        followers = webdriver.find_element_by_xpath("//div[@class='_3XFx6CfPlg-4Usgxm0gK8R']")
        intnumber = parse_numbers(followers.text)
        print("Reddit subscribers :", intnumber)
        FollowerData.append(intnumber)

    youtube = "https://www.youtube.com/channel/UCkzCjdRMrW2vXLx8mvPVLdQ"

    webdriver.get(youtube)

    try:
        followers = webdriver.find_element_by_xpath(
            "/html/body/ytd-app/div/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/app-header-layout/div/app-header/div[2]/div[2]/div/div[1]/div/div[1]/yt-formatted-string")
        intnumber = parse_numbers(followers.text.split(" ")[0])
        FollowerData.append(intnumber)
        print("Youtube followers: ", intnumber)
    except selenium.common.exceptions.NoSuchElementException:
        followers = webdriver.find_element_by_xpath("//yt-formatted-string[@id='subscriber-count']")
        print("EXCEPT")
        print("REDDIT FOLLOWERS : ")
        print(followers.text)
        print(followers.get_attribute("innerhtml"))
        FollowerData.append(followers.text)

    twitter = "https://twitter.com/mancity"

    webdriver.get(twitter)

    try:
        followers = webdriver.find_element_by_xpath("//a[@href='/ManCity/followers']")
        data = followers.text
        regex = "([\d|,]+)"
        number = re.findall(regex, data)
        intnumber = parse_numbers(number[0])
        FollowerData.append(intnumber)
        print("Twitter followers :", intnumber)
    except selenium.common.exceptions.NoSuchElementException:
        pass

    insta = "https://www.instagram.com/mancity/"

    webdriver.get(insta)

    try:
        followers = webdriver.find_element_by_xpath("//span[@class='g47SY']")
        intnumber = parse_numbers(followers.get_attribute("innerhtml"))
        FollowerData.append(intnumber)
        print("Insta followers :", intnumber)
    except selenium.common.exceptions.NoSuchElementException:
        followers = webdriver.find_element_by_xpath(
            "/ html / body / div[1] / section / main / div / header / section / ul / li[2] / a / span")
        intnumber = parse_numbers(followers.get_attribute("title"))
        FollowerData.append(intnumber)
        print("Insta followers :", intnumber)

    webdriver.close()
    webdriver.quit()
    # print(FollowerData)
    return FollowerData


def write_data(FollowerData):
    fhand = open("FollowerData.csv", "a")
    fhand.write(str(datetime.now()))
    for i in FollowerData:
        fhand.write(",")
        fhand.write(str(i))
    fhand.write("\"")
    fhand.close()
    return 1
