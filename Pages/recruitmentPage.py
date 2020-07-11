from Locators.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys


class RecruitmentPage:
    def __init__(self, driver):
        self.driver = driver

        locators = Locators()

    def candidates(self):
        self.driver.find_element_by_link_text('Recruitment').click()
        for i in range(20):
            self.driver.find_element_by_xpath("//*[@class='toggle tiptip']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@class='toggle tiptip activated']").click()

    def vacancies(self):
        self.driver.find_element_by_link_text('Vacancies').click()
        for i in range(20):
            self.driver.find_element_by_xpath("//*[@class='toggle tiptip']").click()
            time.sleep(1)
            self.driver.find_element_by_xpath("//*[@class='toggle tiptip activated']").click()

