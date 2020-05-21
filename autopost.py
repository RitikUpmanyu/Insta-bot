import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import *
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pprint import pprint as pp
from time import sleep

from instapy import InstaPy
from secrets import *

import autoit
import time

e = sys.exit

home = os.path.dirname(sys.argv[0])
if not home or not home.strip("."):
    home = os.path.dirname(os.path.abspath(__file__))


# INSTA_USER  = os.environ.get('INSTA_USER')
# INSTA_PWD 	= os.environ.get('INSTA_PWD')

import traceback

try:
    import cStringIO
except ImportError:
    import io as cStringIO


phototext = "hello world!! #mom #meme"


def upload(browser, phototext, photopath):

    browser.find_element_by_xpath(
        "/html/body/div[1]/section/nav[2]/div/div/div[2]/div/div/div[3]"
    ).click()
    time.sleep(1.5)

    autoit.win_activate(
        "File Upload"
    )  # open can change by your os language if not open change that
    time.sleep(2)
    autoit.control_send("File Upload", "Edit1", photopath)
    time.sleep(1.5)
    autoit.control_send("File Upload", "Edit1", "{ENTER}")
    time.sleep(1)
    try:
        browser.find_element_by_xpath("//button[span='Expand']").click()
        time.sleep(1)
    except Exception as e:
        print(e)
        pass
    browser.find_element_by_xpath(
        "/html/body/div[1]/section/div[1]/header/div/div[2]/button"
    ).click()
    time.sleep(2)
    ta = browser.find_elements(By.XPATH, "//textarea")

    for part in phototext.split("\n"):
        pp(part)
        if part:
            ta[0].send_keys(part)
            ActionChains(browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(
                Keys.SHIFT
            ).key_up(Keys.ENTER).perform()
        else:
            pass
    time.sleep(4)

    browser.find_element_by_xpath(
        "/html/body/div[1]/section/div[1]/header/div/div[2]/button"
    ).click()


if __name__ == "__main__":

    session = InstaPy(username=INSTA_USERNAME, password=INSTA_PASSWORD)
    session.login()

    sleep(5)

    photopath = "C:\\insta\\YOUR DIR4.jpg"  # or any file you wanna post
    upload(session.browser, phototext, photopath)

    # session.browser.close()
