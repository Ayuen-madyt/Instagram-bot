from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

PATH = "C:\Program Files (x86)\chromedriver.exe"


class instabot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(PATH) 
        self.login()
        
        
    def login(self):
        self.driver.get('https://www.instagram.com/')
        sleep(2)
        self.driver.find_element_by_name('username').send_keys(self.username)
        password_field = self.driver.find_element_by_name('password')
        password_field.send_keys(self.password)
        password_field.send_keys(Keys.RETURN)
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
    
    #search gainwithmchina
    def search_user(self):
        self.driver.find_element_by_xpath("//input[@placeholder='Search']").send_keys("iam cardi b")
               
bot = instabot('iun_madyt', 'madytiun.com')
bot.serach_user()

