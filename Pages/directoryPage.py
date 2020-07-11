from Locators.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class DirectoryPage:
    def __init__(self, driver):
        self.driver = driver

        locators = Locators()

    def search_directory(self):
        self.driver.find_element_by_link_text('Directory').click()
        try:
            select = Select(self.driver.find_element_by_id('searchDirectory_job_title'))
            for text in range(11):
                select.select_by_value(str(text))
                time.sleep(1)
                self.driver.find_element_by_id('searchBtn').click()
                time.sleep(3)
        except Exception as e:
            print(e)
