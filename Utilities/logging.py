import os
import sys
import time
import logging
import traceback


class Get_log:
    def __init__(self, driver):
        self.driver = driver

    def log(self):
        os.chdir(r'C:\Users\Chandan Mukherjee\PycharmProjects\ProperProjectChandan\Utilities')
        logging.basicConfig(filename='log.txt', filemode='a+', level=logging.DEBUG)

