from selenium import webdriver
import time
import random
class Testlogin:

    def test_01_my_prezentation(self):
        # n = random.randint(1, 8)
        self.driver.get('https://uatstaging.myprezent.com/signin')
        time.sleep(5)
        self.driver.find_element('id','username').send_keys('amod-uat.noreply@abbvie.com ')
        ## sending user name to browser
        time.sleep(5)
        self.driver.find_element('id','password').send_keys('7b6907195ed41d261bd9')
        self.driver.find_element('id','submit').click()
        time.sleep(20)
