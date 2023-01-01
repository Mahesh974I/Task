from selenium import webdriver
import time
import random

from selenium.webdriver.common.by import By


class Testlogin:

    def test_01_my_prezentation(self):
        # n = random.randint(1, 8)
        self.driver.get('https://livestaging.myprezent.com/signin')
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,'#username').send_keys('ayush-ls.noreply@abbvie.com')
        self.driver.find_element(By.CSS_SELECTOR,'#continue').click()

        ## sending user name to browser
        # time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,'#password').send_keys('870a099a729a3de2ca1d')
        self.driver.find_element(By.CSS_SELECTOR,'#submit').click()
        time.sleep(20)
