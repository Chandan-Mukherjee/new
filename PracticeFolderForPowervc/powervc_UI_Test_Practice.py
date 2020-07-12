from selenium import webdriver
import Relative_Project_Path
import os
import time
from selenium.webdriver.common.keys import Keys


# This page contains desired capabilities to avoid the certificate issues of browsers

class Open_powervc_new_UI:

    def __init__(self):
        pass

    @staticmethod
    def open_ui():
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--start-maximized")
        prefs = {"profile.default_content_settings.popups": 0,
                 "download.default_directory": r"C:\Users\ChandanMukherjee\Desktop\\",
                 # IMPORTANT - ENDING SLASH V IMPORTANT
                 "directory_upgrade": True}
        options.add_experimental_option("prefs", prefs)
        chromedriver = Relative_Project_Path.driver_path + 'chromedriver.exe'
        driver = webdriver.Chrome(executable_path=chromedriver, options=options)
        driver.maximize_window()
        driver.delete_all_cookies()
        driver.implicitly_wait(20)
        driver.get('https://9.47.80.165/')
        time.sleep(10)
        driver.find_element_by_id('username').send_keys('root')
        driver.find_element_by_id('password').send_keys('passw0rd')
        driver.find_element_by_id('loginButton').click()
        driver.find_element_by_xpath("//button[@aria-label='User']").click()
        driver.find_element_by_xpath("//button[@tabindex='0']").click()
        driver.find_element_by_xpath("//button[@tabindex='0']").send_keys(Keys.ENTER)
        print(driver.title)


open_powervc_new_ui = Open_powervc_new_UI
open_powervc_new_ui.open_ui()
