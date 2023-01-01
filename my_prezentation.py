from selenium import webdriver
import time
import random

from selenium.webdriver.common.by import By


class TestPrezentation():

    def test_01_my_prezentation(self):
        self.driver.get('https://livestaging.myprezent.com/signin')
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, '#username').send_keys('ayush-ls.noreply@abbvie.com')
        self.driver.find_element(By.CSS_SELECTOR, '#continue').click()

        ## sending user name to browser
        # time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys('870a099a729a3de2ca1d')
        self.driver.find_element(By.CSS_SELECTOR, '#submit').click()
        time.sleep(20)
        self.driver.find_element(By.CSS_SELECTOR, 'a#v-step-2').click()
        time.sleep(20)
        self.driver.find_element(By.CSS_SELECTOR, 'a#v-step-1').click()

    # def download():
    #     driver.find_element('xpath',"//a[@id='v-step-1']").click()
    #     time.sleep(20)
    #     print('slide clicking')
    #     driver.find_element('xpath',"//div[@class = ' col-sm-3 carousel-cell ']/div [1]").click()
    #     time.sleep(15)
    #     driver.find_element('xpath',"//div[@class = 'left-side-items']/div" + " "+str([n])).click()
    #     print('Random slide selection succesfull')
    #     time.sleep(5)
    #     print('downloading the selected slide')
    #     driver.find_element('xpath',"//div[@class = 'new-slide-detail-speed v-speed-dial v-speed-dial--direction-bottom']").click()
    #     time.sleep(3)
    #     driver.find_element('xpath',"//button[@id = 'download-btn-from-list'] ").click()
    #     time.sleep(20)
    #     print('test executed successfully')


    # my_prezentation()
    # download()
    # driver.close()