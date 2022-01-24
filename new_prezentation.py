import time
import random
from selenium import webdriver
random_number = random.randint(2,50)
num = random.randint(1,8)

driver = webdriver.Firefox()
# driver = webdriver.Chrome(executable_path='/home/mahesh/Downloads/chromedriver_linux64/chromedriver.exe')
def login():
    driver.get('https://uatstaging.myprezent.com/signin')
    driver.find_element('id','username').send_keys('directorvbxq5.noreply@prezent.ai')
    driver.find_element('id','password').send_keys('prezent123')
    driver.find_element('id','submit').click()
    time.sleep(20)
    print('login successfull')

def context():
    driver.find_element('xpath',"//div[contains(text(),'New Prezentation')]").click()
    time.sleep(5)
    driver.find_element('id','prezentation-name').send_keys('practice')
    time.sleep(5)
    driver.find_element('id','audience-auto-complete-list').click()
    time.sleep(5)
    driver.find_element('xpath',"//div[@role ='option']"+" " + str([random_number])).click()
    print('Type of audiance selected sucessfull')
    time.sleep(5)

    # driver.find_element('xpath',"//input[@id='presentation-type-autocomplete-list']").click()
    # time.sleep(5)
    # print('start')
    # driver.find_element('xpath',"//div[@id='list-item-144-0']//div[@id='presentation-type-content--auto'] [1]").click()
    # print('end')
    driver.find_element('xpath',"//input[@id='presentation-type-autocomplete-list']").send_keys("brand")
    driver.find_element('xpath',"//div[contains(text(),'Brand Plan')]").click()


    time.sleep(5)
    print('context created sucessfull')

def outline():

    driver.find_element('xpath',"//button[@id='next-btn']").click()
    time.sleep(8)
    driver.find_element('xpath',"//span[contains(text(),'Accept and save outline')]").click()
    time.sleep(3)
    print('outline created successful')

def slides():
    driver.find_element('xpath',"//input[@id='presentation-type--auto']").send_keys('presentation')
    driver.find_element('xpath',"//input[@id='presentation-description--auto']").send_keys('Sample presentation')
    driver.find_element('xpath',"//span[contains(text(),'Accept and Save')]").click()
    time.sleep(8)
    driver.find_element('xpath',"//div[@class = 'left-side-items'] /div" + " "+str([num])).click()
    time.sleep(5)
    driver.find_element('css selector','#download-btn-new-presentation--auto').click()
    time.sleep(5)
    driver.find_element('css selector',"#download-from-new-present-list--auto").click()
    time.sleep(10)
    print('slides download sucessfull')
    print('test executed sucessfull')

if __name__ == '__main__':
    login()
    context()
    outline()
    slides()
    driver.close()