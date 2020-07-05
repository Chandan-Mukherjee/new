from selenium import webdriver
import time
import openpyxl
from configparser import ConfigParser
import os
import logging
import shutil


class BaseClass:
    # complete framework making: https://www.youtube.com/watch?v=BURK7wMcCwU
    # pip install html-testRunner

    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path=r"C:\Users\Chandan Mukherjee\PycharmProjects\ProperProjectChandan\Browsers\chromedriver.exe")
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(30)
        shutil.rmtree(r'C:\Users\Chandan Mukherjee\PycharmProjects\ProperProjectChandan\Screenshots')
        os.mkdir(r'C:\Users\Chandan Mukherjee\PycharmProjects\ProperProjectChandan\Screenshots')
        logging.basicConfig(
            filename=r'C:\Users\Chandan Mukherjee\PycharmProjects\ProperProjectChandan\Screenshots\log.txt',
            filemode='a+', level='DEBUG')

    def excelReader(self):
        logging.warning('This is just a sample warning.')
        # https://www.youtube.com/watch?v=AOTCpZbC80Y
        self.file = openpyxl.load_workbook(
            r"C:\Users\Chandan Mukherjee\PycharmProjects\ProperProjectChandan\testdata.xlsx")
        self.sheet = self.file.active
        print(self.sheet.cell(row=1, column=1).value)

    def configReader(self):
        logging.info('Running config files.')
        # https://www.youtube.com/watch?v=jBwfq6UMxkY
        # https://www.youtube.com/watch?v=Gdw0-QGq-z0
        # config.ini , this name is not mandatory, you can give any name.
        self.config = ConfigParser()
        self.config.read('config.ini')
        print(self.config.sections())
        self.site = self.config['DEFAULT']['url']
        print(self.site)

    def websiteGo(self):
        self.configReader()
        self.website_login()
        self.excelReader()
        self.screenShot()

    def website_login(self):
        self.driver.get(self.site)
        username = self.driver.find_element_by_id('txtUsername')
        username.clear()
        username.send_keys(self.config['DEFAULT']['username'])
        password = self.driver.find_element_by_id('txtPassword')
        password.clear()
        password.send_keys(self.config['DEFAULT']['password'])
        self.driver.find_element_by_id('btnLogin').click()
        self.driver.find_element_by_link_text('Welcome Admin').click()
        self.driver.find_element_by_link_text('Logout').click()
        time.sleep(3)

    def screenShot(self):
        logging.info('Taking screenshot...')
        os.chdir(r'C:\Users\Chandan Mukherjee\PycharmProjects\ProperProjectChandan\Screenshots')
        current_time = '_'.join(time.ctime().split(':'))
        print(current_time)
        self.driver.get_screenshot_as_file(current_time + '.png')

    def quit_browser(self):
        self.driver.quit()


if __name__ == '__main__':
    BaseClass().websiteGo()
