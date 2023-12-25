from Internet_speed_test import InternetSpeedBot
import time
from selenium.webdriver.common.by import By

PROMISED_DOWN = 150
PROMISED_UP = 10
FB_EMAIL = "my_email"
FB_PWD = "my_pwd"

IntSpeedBot = InternetSpeedBot()
IntSpeedBot.driver.get("https://www.speedtest.net/")
time.sleep(5)

privacy = IntSpeedBot.driver.find_element(By.ID, "onetrust-accept-btn-handler")
privacy.click()
time.sleep(3)

IntSpeedBot.get_internet_speed()
IntSpeedBot.tweet_at_provider(email=FB_EMAIL, pwd=FB_PWD, keys=f"{PROMISED_DOWN}down/{PROMISED_UP}up")



