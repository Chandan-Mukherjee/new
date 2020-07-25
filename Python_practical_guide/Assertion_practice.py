from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(
    executable_path=r'C:\Users\Chandan Mukherjee\PycharmProjects\ProperProjectChandan\Browsers\chromedriver.exe')

try:
    print('test1')
    assert 2 == 3, 'assetion failed'
except Exception as e:
    print(e)
    driver.close()
    print('test2')
