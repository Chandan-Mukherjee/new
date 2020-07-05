from Locators.locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        locators = Locators()
        self.welcome_link_text = locators.welcome_link_text
        self.logout_button_link_text = locators.logout_button_link_text

    def click_on_welcome(self):
        self.driver.find_element_by_link_text(self.welcome_link_text).click()

    def click_logout(self):
        self.driver.find_element_by_link_text(self.logout_button_link_text).click()
