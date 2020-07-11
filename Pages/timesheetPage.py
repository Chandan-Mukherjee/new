from Locators.locators import Locators
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.keys import Keys


class TimesheetPage:
    def __init__(self, driver):
        self.driver = driver

        locators = Locators()

    def check_timesheet(self):
        self.driver.find_element_by_link_text('Dashboard').click()
        self.driver.find_element_by_link_text('Timesheets').click()
        emp_name = self.driver.find_element_by_id('employee')
        emp_name.clear()
        self.act = ActionChains(driver=self.driver)
        emp_name.send_keys('Linda Anderson')
        # self.act.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
        self.driver.find_element_by_id('btnView').click()
        # time.sleep(5)

    def add_timesheet(self):
        self.driver.find_element_by_id('btnAddTimesheet').click()
        self.driver.find_element_by_xpath("//img[@class='ui-datepicker-trigger']").click()
        self.act.move_to_element(self.driver.find_element_by_xpath("//a[contains(text(),'6')]")).click().perform()
        self.driver.find_element_by_id('btnAddTimesheet').click()
        time.sleep(4)
        print('Entered timesheet successfully')
