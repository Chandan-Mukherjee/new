from Locators.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys


class MainLogoToOpenNewTab:
    def __init__(self, driver):
        self.driver = driver

        locators = Locators()

    def click_main_logo(self):
        self.driver.find_element_by_xpath("//img[@alt='OrangeHRM']").click()

    def go_to_new_tab(self):
        self.windows = self.driver.window_handles
        self.driver.switch_to.window(self.windows[1])

    def click_on_partners_tab(self):
        self.driver.find_element_by_link_text('Partners').click()
        time.sleep(2)
        self.driver.refresh()
        self.driver.switch_to.window(self.windows[0])
