from Locators.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys


class PIMPage:
    def __init__(self, driver):
        self.driver = driver

        locators = Locators()

    def select_all_IDs(self):
        self.driver.find_element_by_link_text('PIM').click()
        checkboxes = self.driver.find_elements_by_xpath("//input[@type='checkbox']")
        for j in range(2):
            for i in checkboxes:
                i.click()
            time.sleep(2)
            for i in checkboxes:
                i.click()
            self.driver.find_element_by_id('ohrmList_chkSelectAll').click()
            time.sleep(2)

    def scroll_into_view(self):
        self.driver.execute_script('window.scrollBy(0,1000);')
        time.sleep(5)
        self.driver.execute_script('window.scrollBy(0,-1000);')
        time.sleep(5)
        self.driver.execute_script("arguments[0].scrollIntoView(true);",
                                   self.driver.find_element_by_link_text('OrangeHRM, Inc'))
        # self.driver.find_element_by_link_text('OrangeHRM, Inc').click()
        # time.sleep(2)
        # self.driver.switch_to.default_content()
