from selenium import webdriver
import time
import random

from selenium.webdriver.common.by import By


class Testlogin:

    def test_01_my_prezentation(self):
        # n = random.randint(1, 8)
        self.driver.get('https://uatstaging.myprezent.com/signin')
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,'#username').send_keys('amod-uat.noreply@abbvie.com ')
        ## sending user name to browser
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,'#password').send_keys('7b6907195ed41d261bd9')
        self.driver.find_element(By.CSS_SELECTOR,'#submit').click()
        time.sleep(20)
