from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class InternetSpeedBot:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(chrome_options)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        start_test = self.driver.find_element(By.CLASS_NAME, "js-start-test")
        start_test.click()
        time.sleep(50)

        self.down = self.driver.find_element(By.CLASS_NAME, "download-speed").text
        print(f"down: {self.down}")

        self.up = self.driver.find_element(By.CLASS_NAME, "upload-speed").text
        print(f"up: {self.up}")

    def tweet_at_provider(self, email, pwd, keys):
        self.driver.get("https://www.facebook.com/")
        email_id = self.driver.find_element(By.ID, "email")
        email_id.send_keys(email)
        pwd_id = self.driver.find_element(By.ID, "pass")
        pwd_id.send_keys(pwd)
        button = self.driver.find_element(By.NAME, "login")
        button.click()
        click_post = self.driver.find_element(By.CLASS_NAME, "x1lliihq")
        click_post.click()
        write_post = self.driver.find_element(By.CLASS_NAME, "xzsf02u")
        write_post.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {keys}")