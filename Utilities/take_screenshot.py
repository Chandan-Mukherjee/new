import os
import sys
import time


class Take_Screenshot:
    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self):
        print('The current directory is: ' + str(os.getcwd()))
        newDir = os.chdir(r'C:\Users\Chandan Mukherjee\PycharmProjects\ProperProjectChandan\Screenshots')
        print(f"Changed the directory to: 'C:\\Users\\Chandan Mukherjee\\PycharmProjects\\ProperProjectChandan\\Screenshots'")
        current_time = time.ctime()
        empty_list = []
        for i in str(current_time):
            if not (i == ' ' or i == ':'):
                empty_list.append(i)
        self.driver.get_screenshot_as_file(''.join(empty_list) + '.png')
