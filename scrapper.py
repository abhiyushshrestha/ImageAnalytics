from selenium import webdriver
from time import sleep
import urllib
import urllib.request
import config

class Scrapper:

    def __init__(self):
        self.driver = webdriver.Chrome("/home/anonymous/Downloads/chromedriver_linux64/chromedriver")

    def scrape(self):
        '''
            This function login to your linkedin account and scape the profile picture of the linkedin profile you
            want
        :return: saves profile image in jpg format
        '''
        self.driver.get(config.LOGIN_URL)
        # This is used to locate the email or username field by id
        username = self.driver.find_element_by_id('username')
        # send_keys() is used to simulate key strokes as if we are typing in the username field
        username.send_keys(config.USERNAME)
        # This is used to locate the email or username field by id
        password = self.driver.find_element_by_id("password")
        # send_keys() is used to simulate key strokes as if we are typing password in the password field
        password.send_keys(config.PASSWORD)
        # locate submit button by_class_id
        log_in_button = self.driver.find_element_by_class_name('btn__primary--large')
        # .click() to mimic button click
        log_in_button.click()
        print("Please, wait for a moment we are loading your account...")
        sleep(0.5)
        print("\n\nLoading acccount successful!!!")

        profile_link = input("Enter the Linkedin profile link: ")
        self.driver.get(profile_link)
        sleep(2)
        profile_pic = self.driver.find_element_by_class_name('pv-top-card__photo')
        image_src = profile_pic.get_attribute('src')
        urllib.request.urlretrieve(image_src, "image/image.jpg")