# install selenium and instapy
# only works in firefox browser , install firefox webdriver --> put it in path


from time import sleep
from selenium import webdriver
from secrets import *


class LoginPage:
    def __init__(self, browser):
        self.browser = browser

    def login(self, username, password):
        username_input = self.browser.find_element_by_css_selector(
            "input[name='username']"
        )
        password_input = self.browser.find_element_by_css_selector(
            "input[name='password']"
        )
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = browser.find_element_by_xpath("//button[@type='submit']")
        login_button.click()
        sleep(5)


class HomePage:
    def __init__(self, browser):
        self.browser = browser
        self.browser.get("https://www.instagram.com/")

    def go_to_login_page(self):
        sleep(2)
        return LoginPage(self.browser)


browser = webdriver.Firefox()
browser.implicitly_wait(5)


def test_login_page(browser):
    home_page = HomePage(browser)
    login_page = home_page.go_to_login_page()
    login_page.login(INSTA_USERNAME, INSTA_PASSWORD)

    errors = browser.find_elements_by_css_selector("#error_message")
    assert len(errors) == 0


test_login_page(browser)


def go_to_profile():
    browser.implicitly_wait(3)
    not_now_notif = browser.find_element_by_xpath(
        "/html/body/div[4]/div/div/div[3]/button[2]"
    )
    profile_button = browser.find_element_by_xpath(
        "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/a/img"
    )
    not_now_notif.click()
    profile_button.click()


go_to_profile()
