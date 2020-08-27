import re
from datetime import datetime
import selenium


# parses numbers ending with K or M or B. Or seperated by commas.
# returns a int instance of the str number passed to it
def parse_numbers(num):
    if isinstance(num[-1], int):
        number = num
        pass
    else:
        if (num[-1].lower() == "k"):
            multiplier = 1000
            number = float(num[:-1])
            number *= multiplier
        elif (num[-1].lower() == "m"):
            multiplier = 1000000
            number = float(num[:-1])
            number *= multiplier
        elif (num[-1].lower() == "b"):
            multiplier = 1000000000
            number = float(num[:-1])
            number *= multiplier
        else:
            number = num

    try:
        output = int(number.replace(',', ''))
    except AttributeError:
        output = int(number)
    return output


def valid_data(data):
    for i in data:
        if data[i] == 0:
            return False
    return True


def get_insta(webdriver):
    insta = "https://www.instagram.com/mancity/"
    webdriver.get(insta)
    try:
        followers = webdriver.find_element_by_xpath("//span[@class='g47SY']")
        intnumber = parse_numbers(followers.get_attribute("innerhtml"))
        print("Insta followers :", intnumber)
    except selenium.common.exceptions.NoSuchElementException:
        followers = webdriver.find_element_by_xpath(
            "/ html / body / div[1] / section / main / div / header / section / ul / li[2] / a / span")
        intnumber = parse_numbers(followers.get_attribute("title"))
        print("Insta followers :", intnumber)
    return intnumber


def get_twitter(webdriver):
    twitter = "https://twitter.com/mancity"
    webdriver.get(twitter)
    try:
        followers = webdriver.find_element_by_xpath("//a[@href='/ManCity/followers']")
        data = followers.text
        regex = "([\d|,]+)"
        number = re.findall(regex, data)
        intnumber = parse_numbers(number[0])
        print("Twitter followers :", intnumber)
    except selenium.common.exceptions.NoSuchElementException:
        intnumber = 0
        pass
    return intnumber


def get_youtube(webdriver):
    youtube = "https://www.youtube.com/channel/UCkzCjdRMrW2vXLx8mvPVLdQ"
    webdriver.get(youtube)
    try:
        followers = webdriver.find_element_by_xpath(
            "/html/body/ytd-app/div/ytd-page-manager/ytd-browse/div[3]/ytd-c4-tabbed-header-renderer/app-header-layout/div/app-header/div[2]/div[2]/div/div[1]/div/div[1]/yt-formatted-string")
        intnumber = parse_numbers(followers.text.split(" ")[0])
        print("Youtube followers: ", intnumber)
    except selenium.common.exceptions.NoSuchElementException:
        followers = webdriver.find_element_by_xpath("//yt-formatted-string[@id='subscriber-count']")
        print("EXCEPT")
        print("REDDIT FOLLOWERS : ")
        print(followers.text)
        print(followers.get_attribute("innerhtml"))
        intnumber = parse_numbers(followers.text)

    return intnumber


def get_reddit(webdriver):
    reddit = "https://www.reddit.com/r/MCFC/"
    webdriver.get(reddit)
    try:
        followers = webdriver.find_element_by_xpath(
            "/html/body/div[1]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div")
        intnumber = parse_numbers(followers.text)
        print("Reddit subscribers :", intnumber)
    except selenium.common.exceptions.NoSuchElementException:
        followers = webdriver.find_element_by_xpath("//div[@class='_3XFx6CfPlg-4Usgxm0gK8R']")
        intnumber = parse_numbers(followers.text)
        print("Reddit subscribers :", intnumber)
    return intnumber


def get_facebook(webdriver):
    facebook = "https://www.facebook.com/mancity"
    webdriver.get(facebook)
    try:
        followers = webdriver.find_element_by_xpath(
            "/html/body/div[1]/div[4]/div[1]/div/div/div[2]/div[2]/div/div[3]/div[1]/div/div/div[1]/div/div/div[2]/div/div[2]/div[2]/div/div[2]/div")
        data = followers.text
        regex = "([\d|,]+)"
        number = re.findall(regex, data)
        intnumber = int(number[0].replace(',', ''))
        print("Facebook followers :", intnumber)
    except selenium.common.exceptions.NoSuchElementException:
        intnumber = 0
        pass

    return intnumber


def write_data(FollowerData):
    file = "FollowerData.csv"
    fhand = open(file, "a")
    fhand.write(str(datetime.now()))
    fhand.write(",")
    for i in FollowerData:
        val = FollowerData[i]
        fhand.write(str(val))
        fhand.write(",")
    fhand.write("\n")

    fhand.close()
    print("Writing data to disk completed !")
    return 1
