from selenium import webdriver
import time
import random
fp = webdriver.FirefoxProfile()
fp.set_preference('browser.download.folderList', 2)
fp.set_preference('browser.download.manager.showWhenStarting', False)
fp.set_preference('browser.download.dir', "/home/mahesh/Downloads")
fp.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/msword, application/csv, application/ris, text/csv, image/png, application/pdf, text/html, text/plain, application/zip, application/x-zip, application/x-zip-compressed, application/download, application/octet-stream,application/vnd.openxmlformats-officedocument.presentationml.presentation,application/vnd.ms-powerpoint')
fp.set_preference('browser.helperApps.alwaysAsk.force', False)
fp.set_preference('browser.download.manager.alertOnEXEOpen', False)
fp.set_preference('browser.download.manager.focusWhenStarting', False)
fp.set_preference('browser.download.manager.useWindow', False)
fp.set_preference('browser.download.manager.showAlertOnComplete', False)
fp.set_preference('browser.download.manager.closeWhenDone', False)
fp.set_preference("pdfjs.disabled", True)

driver = webdriver.Firefox(fp)

n = random.randint(1,7)

# driver = webdriver.Chrome(executable_path='/home/mahesh/Downloads/chromedriver_linux64/chromedriver.exe')

def slide_login():
    driver.get('https://uatstaging.myprezent.com/signin')
    driver.find_element('id','username').send_keys('directorvbxq5.noreply@prezent.ai')
    driver.find_element('id','password').send_keys('prezent123')
    driver.find_element('id','submit').click()
    time.sleep(20)
    print('login Successful')

def slide_download():
    driver.find_element('xpath',"//a[@id='v-step-2']").click()
    time.sleep(30)
    driver.find_element('xpath',"//input[@id='global-hybrid-search']").send_keys('Goals')

    time.sleep(5)
    print('search for particular slide is completed')
    driver.find_element('xpath',"//button[@name = 'global-search-icon']").click()
    time.sleep(8)
    ## slide clicking
    driver.find_element('xpath',"//div[@class = 'slider-content-wrapper']").click()
    time.sleep(4)
    ## Selecting particular node"//div[@id='list-item-144-1"+''+str(num))
    driver.find_element('xpath',"//div[@class = 'related-products-thumbails']/div"+ " "+str([n])).click()
    time.sleep(5)
    print('selected random slide')
    driver.find_element('xpath',"//button[@id='slide-detail-download-btn--auto']").click()
    time.sleep(3)
    driver.find_element('xpath',"//button[@id = 'slide-detail-download-from-list--auto']").click()
    time.sleep(30)
    print('test executed successful')

if __name__ == '__main__':
    slide_login()
    slide_download()
    driver.close()
# driver.close()