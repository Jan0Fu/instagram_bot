from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

USERNAME = ""
PASSWORD = ""
FOLLOW_ACCOUNT = "chefsteps"
URL = "https://www.instagram.com/accounts/login/"
DRIVER_PATH = "/Users/jano/chromedriver"


class InstaFollower:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(driver_path)

    def login(self):
        self.driver.get(URL)
        sleep(3)
        user_field = self.driver.find_element(By.CSS_SELECTOR, "._ab3a input")
        user_field.send_keys(USERNAME)
        sleep(5)
        password_field = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        password_field.send_keys(PASSWORD)
        sleep(3)
        password_field.send_keys(Keys.ENTER)
        sleep(5)
        save_info = self.driver.find_element(By.CSS_SELECTOR, '._ac8f button')
        save_info.click()
        sleep(3)
        turn_notification = self.driver.find_element(By.CSS_SELECTOR, '._a9-z button')
        turn_notification.click()
        sleep(3)

    def find_followers(self):
        pass

    def follow(self):
        pass


InstaBot = InstaFollower(DRIVER_PATH)
InstaBot.login()
