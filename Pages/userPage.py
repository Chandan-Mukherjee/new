from Locators.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
import time


class UserPage:
    def __init__(self, driver):
        self.driver = driver

        locators = Locators()

    def click_on_users(self):
        admin_button = self.driver.find_element_by_id('menu_admin_viewAdminModule')
        actions = ActionChains(self.driver)
        actions.move_to_element(admin_button)
        actions.perform()
        # time.sleep(1)
        actions.move_to_element(self.driver.find_element_by_id('menu_admin_UserManagement')).perform()
        # time.sleep(1)
        actions.move_to_element(self.driver.find_element_by_id('menu_admin_viewSystemUsers')).click().perform()
        # time.sleep(1)
