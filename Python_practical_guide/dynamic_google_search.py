import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(
    executable_path=r'C:\Users\Chandan Mukherjee\PycharmProjects\ProperProjectChandan\Browsers\chromedriver.exe')

try:
    # ActionChains(driver)
    driver.get('https://google.com')
    driver.maximize_window()
    driver.implicitly_wait(10)
    time.sleep(2)
    driver.find_element_by_name('q').send_keys('selenium')
    time.sleep(2)
    all_items = driver.find_elements_by_xpath("//ul/li/div/div/div/span/b")
    for items in all_items:
        print(items.text)
        if items.text == 'download':
            print(f'Clicked on {items.text}')
            items.click()
    time.sleep(2)
except Exception as e:
    print(e)
finally:
    driver.quit()
