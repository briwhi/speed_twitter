from config import *
from selenium import webdriver
import time

PROMISED_DOWN = 75
PROMISED_UP = 20
CHROME_DRIVER_PATH = "C:/Users/brian/Documents/chromedriver.exe"

class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.up = int
        self.down = int

    def get_internet_speed(self):
        self.driver.get("http://speedtest.net")
        time.sleep(5)
        button = self.driver.find_element_by_css_selector(".start-button a")
        button.click()
        time.sleep(60)
        self.down = float(self.driver.find_element_by_class_name("download-speed").text)
        print(self.down)
        self.up = float(self.driver.find_element_by_class_name("upload-speed").text)
        print(self.up)

    def tweet_at_provider(self):
        pass


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
