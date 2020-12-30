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
        self.driver.get("http://www.twitter.com")
        login = self.driver.find_element_by_link_text("Log in")
        login.click()
        time.sleep(1)
        user = self.driver.find_element_by_name("session[username_or_email]")
        user.send_keys(TWITTER_EMAIL)
        t_pass = self.driver.find_element_by_name("session[password]")
        t_pass.send_keys(TWITTER_PASS)
        login_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div')
        login_button.click()
        time.sleep(1)
        tweet_compose = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div')
        tweet = f"Down: {self.down} Up:{self.up}"
        tweet_compose.send_keys(tweet)
        tweet_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]')
        tweet_button.click()
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
