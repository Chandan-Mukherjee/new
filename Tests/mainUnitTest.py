# import time
import unittest
import os
# import sys
from selenium import webdriver
from configparser import ConfigParser
from Pages.homePage import HomePage
from Pages.loginpage import Loginpage
from Pages.userPage import UserPage
from Pages.timesheetPage import TimesheetPage
from Pages.mainLogoToOpenNewTab import MainLogoToOpenNewTab
from Pages.directoryPage import DirectoryPage
from Pages.PIMpage import PIMPage
from Pages.recruitmentPage import RecruitmentPage
from Utilities.take_screenshot import Take_Screenshot
import Relative_Project_Path
from Utilities.logging import Get_log

# import HTMLTestRunner




# from selenium.webdriver.common.action_chains import ActionChains


# sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


def test_sample2():
    print('This is a sample test case.')


class SampleUnitTest(unittest.TestCase):
    # https://www.youtube.com/watch?v=BURK7wMcCwU
    # (most important 33 mins)
    # 43 mins

    def setUp(self) -> None:
        print('This is method level setup.')
        self.driver = webdriver.Chrome(
            executable_path=Relative_Project_Path.driver_path+'chromedriver.exe')
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(30)
        self.config = ConfigParser()
        self.config.read('config.ini')
        self.site = self.config['DEFAULT']['url']

    def tearDown(self) -> None:
        print('This is method level teardown.')

    @classmethod
    def setUpClass(cls) -> None:
        print('This is class level setUp.')

    @classmethod
    def tearDownClass(cls) -> None:
        print('This is class level teardown.')

    def test_sample(self):
        take_screenshot = Take_Screenshot(self.driver)
        get_log = Get_log(self.driver)

        self.driver.get(self.site)
        login = Loginpage(driver=self.driver)
        login.enter_username(self.config['DEFAULT']['username'])
        login.enter_password(self.config['DEFAULT']['password'])
        # get_log.log.info('Logged in to ')

        login.click_enter()
        homepage = HomePage(self.driver)
        take_screenshot.take_screenshot()

        userpage = UserPage(self.driver)
        userpage.click_on_users()
        take_screenshot.take_screenshot()

        timesheetpage = TimesheetPage(self.driver)
        timesheetpage.check_timesheet()
        timesheetpage.add_timesheet()
        take_screenshot.take_screenshot()

        mainLogoToOpenNewTab = MainLogoToOpenNewTab(self.driver)
        mainLogoToOpenNewTab.click_main_logo()
        mainLogoToOpenNewTab.go_to_new_tab()
        mainLogoToOpenNewTab.click_on_partners_tab()
        take_screenshot.take_screenshot()

        directoryPage = DirectoryPage(self.driver)
        directoryPage.search_directory()
        take_screenshot.take_screenshot()

        pimpage = PIMPage(self.driver)
        pimpage.select_all_IDs()
        pimpage.scroll_into_view()
        take_screenshot.take_screenshot()

        recruitmentpage = RecruitmentPage(self.driver)
        recruitmentpage.candidates()
        recruitmentpage.vacancies()
        take_screenshot.take_screenshot()

        homepage.click_on_welcome()
        take_screenshot.take_screenshot()
        homepage.click_logout()

        # time.sleep(3)


if __name__ == '__main__':
    unittest.main()
