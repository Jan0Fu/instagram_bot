from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep
import random

USERNAME = ""
PASSWORD = ""
FOLLOW_ACCOUNT = "chefsteps/followers"
URL = "https://www.instagram.com/"
DRIVER_PATH = Service("/Users/jano/chromedriver")
op = webdriver.ChromeOptions()


class InstaFollower:
    def __init__(self, driver_path, op):
        self.driver = webdriver.Chrome(service=driver_path, options=op)

    def login(self):
        self.driver.get(URL)
        sleep(2)
        self.driver.find_element(By.NAME, "username").send_keys(USERNAME)
        self.driver.find_element(By.NAME, "password").send_keys(PASSWORD)
        self.driver.find_element(By.ID, "loginForm").click()

    def find_followers(self):
        sleep(5)
        self.driver.get(URL + FOLLOW_ACCOUNT)
        sleep(4)

    def follow(self):
        try:
            list_of_followers = self.driver.find_elements(By.CSS_SELECTOR, 'button')
            for item in list_of_followers:
                if item.text == "Follow":
                    item.click()
                    sleep(random.randint(5, 10))
        except Exception as e:
            print(e)


instaBot = InstaFollower(DRIVER_PATH, op)
instaBot.login()
instaBot.find_followers()
instaBot.follow()
