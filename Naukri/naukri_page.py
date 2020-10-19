from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configparser import ConfigParser
import os
import Relative_Project_Path
import time
import pyautogui

# 1. This three lines are for opening chrome in incognito mode...
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(
    executable_path=Relative_Project_Path.driver_path + 'chromedriver.exe', options=chrome_options)
print("\n--Opened Chrome in incognito mode.")

# 2. Config file reading
print('\n---The current directory is: ' + str(os.getcwd()))
os.chdir(Relative_Project_Path.config_init_file_path)
config = ConfigParser()
config.read('config.ini')
# config['DEFAULT']['url']
print('\n---Read the config file and data is collected from that.')
os.chdir(Relative_Project_Path.naukri_path)

try:
    driver.get(config['naukri']['url'])
    driver.maximize_window()
    windows = driver.window_handles
    try:
        for i in windows:
            if not i == windows[0]:
                driver.switch_to.window(i)
                driver.close()
    except Exception as e:
        print(e)
    driver.switch_to.window(windows[0])
    driver.find_element_by_id('login_Layer').click()
    element = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']")))
    driver.find_element_by_xpath("//input[@placeholder='Enter your active Email ID / Username']").send_keys(
        config['naukri']['email']
    )
    driver.find_element_by_xpath("//input[@placeholder='Enter your password']").send_keys(config['naukri']['password'])
    driver.find_element_by_xpath("//button[@type='submit']").click()
    time.sleep(5)
    element1 = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'My Naukri')]")))
    action = ActionChains(driver)
    action.move_to_element(
        driver.find_element_by_xpath("//div[contains(text(),'My Naukri')]")).perform()
    element2 = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.LINK_TEXT, "Edit Profile")))
    action.move_to_element(driver.find_element_by_link_text('Edit Profile')).click().perform()
    element3 = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Resume Headline']")))
    driver.find_element_by_xpath("//span[text()='Resume Headline']").click()
    driver.find_element_by_xpath("//div[@class='resumeHeadline']/div/div/div/span[2]").click()
    current_text = driver.find_element_by_xpath("//form[@name='resumeHeadlineForm']/div[2]/div/textarea").text
    print("\nCurrent Resume Headline is: ")
    print(current_text)
    # driver.find_element_by_link_text('Save').click()
    driver.refresh()
    driver.execute_script("window.scrollTo(0, 200);")
    element4 = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Resume Headline']")))
    driver.find_element_by_xpath("//span[text()='Resume Headline']").click()
    driver.find_element_by_xpath("//div[@class='resumeHeadline']/div/div/div/span[2]").click()
    if current_text == config['naukri']['CurrentText']:
        driver.execute_script("window.scrollTo(0, 200);")
        print("\n----Resume Headline changed to: ")
        print(
            config['naukri']['OtherText'])
        driver.find_element_by_xpath('//*[@id="resumeHeadlineTxt"]').clear()
        driver.find_element_by_xpath('//*[@id="resumeHeadlineTxt"]').send_keys(
            config['naukri']['OtherText'])
    else:
        driver.execute_script("window.scrollTo(0, 200);")
        driver.find_element_by_xpath('//*[@id="resumeHeadlineTxt"]').clear()
        print("\n----Resume Headline changed to: ")
        print(
            config['naukri']['CurrentText'])
        driver.find_element_by_xpath('//*[@id="resumeHeadlineTxt"]').send_keys(
            config['naukri']['CurrentText'])
    driver.find_element_by_xpath(
        "//button[text()='Save' and @class='waves-effect waves-light btn-large blue-btn' ]").click()
    # driver.find_element_by_xpath('//*[@id="resumeHeadlineTxt"]').send_keys(Keys.RETURN)
    driver.refresh()
    driver.execute_script("window.scrollTo(0, 0);")
    print('\n----Edited the text successfully----')
    try:
        time.sleep(2)
        elementCV = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR,
                                        "#attachCV")))
        driver.find_element_by_css_selector(
            "#attachCV").send_keys(
            'C:\\Users\\Chandan Mukherjee\\Desktop\\Final and Updated CV\\Chandan Mukherjee.pdf')
        print('\n---CV is updated.')
    except Exception as e:
        print('\n---unable to attach CV')
        print('\n', e)
    try:
        time.sleep(2)
        driver.find_element_by_css_selector(
            "#attachCV").click()
        time.sleep(4)  # waiting for window popup to open
        pyautogui.write(
            "C:\\Users\\Chandan Mukherjee\\Desktop\\Final and Updated CV\\Chandan Mukherjee.pdf")  # path of File
        pyautogui.press('enter')
        print('\n---CV is updated.')
    except Exception as e:
        print('\n---unable to attach CV')
        print('\n', e)

    element5 = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//img[@src="https://static.naukimg.com/s/4/100/i/naukri_Logo.png"]')))
    driver.find_element_by_xpath('//img[@src="https://static.naukimg.com/s/4/100/i/naukri_Logo.png"]').click()
    print('\n----Clicked on main naukri logo-----')
    # action.move_to_element(
    #     driver.find_element_by_xpath('//a[@href="https://my.naukri.com/HomePage/view"]')).perform()
    # driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
    print("\n----Test Successful, Updated your naukri profile----")
    print("\n---Smile :):):) ---")

except Exception as e:
    print('\n############--------Script failed--------#############')
    print("\n>>>Error is>>>: \n", e)

finally:
    driver.quit()
