import time
import unittest
# import os
# import sys
from selenium import webdriver
from configparser import ConfigParser
from Pages.homePage import HomePage
from Pages.loginpage import Loginpage
import HTMLTestRunner


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
            executable_path=r"C:\Users\Chandan Mukherjee\PycharmProjects\ProperProjectChandan\Browsers\chromedriver.exe")
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
        self.driver.get(self.site)
        login = Loginpage(driver=self.driver)
        login.enter_username(self.config['DEFAULT']['username'])
        login.enter_password(self.config['DEFAULT']['password'])

        login.click_enter()
        homepage = HomePage(self.driver)
        homepage.click_on_welcome()
        homepage.click_logout()

        time.sleep(3)


if __name__ == '__main__':
    HTMLTestRunner.main()
