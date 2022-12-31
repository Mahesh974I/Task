from selenium import webdriver
import time
import random
n = random.randint(1,8)
driver = webdriver.Firefox()
def my_prezentation():
    driver.get('https://uatstaging.myprezent.com/signin')
    driver.find_element('id','username').send_keys('directorvbxq5.noreply@prezent.ai')  ## sending user name to browser
    driver.find_element('id','password').send_keys('prezent123')
    driver.find_element('id','submit').click()
    time.sleep(20)
    print('Login Successfull')
def download():
    driver.find_element('xpath',"//a[@id='v-step-1']").click()
    time.sleep(20)
    print('slide clicking')
    driver.find_element('xpath',"//div[@class = ' col-sm-3 carousel-cell ']/div [1]").click()
    time.sleep(15)
    driver.find_element('xpath',"//div[@class = 'left-side-items']/div" + " "+str([n])).click()
    print('Random slide selection succesfull')
    time.sleep(5)
    print('downloading the selected slide')
    driver.find_element('xpath',"//div[@class = 'new-slide-detail-speed v-speed-dial v-speed-dial--direction-bottom']").click()
    time.sleep(3)
    driver.find_element('xpath',"//button[@id = 'download-btn-from-list'] ").click()
    time.sleep(20)
    print('test executed successfully')

if __name__ == '__main__':
    my_prezentation()
    download()
    driver.close()