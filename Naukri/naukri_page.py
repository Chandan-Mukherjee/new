from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import Relative_Project_Path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# This three lines are for opening chrome in incognito mode...
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

driver = webdriver.Chrome(
    executable_path=Relative_Project_Path.driver_path + 'chromedriver.exe', options=chrome_options)
print("\n\n--Opened Chrome in incognito mode.")

driver.get('https://google.com')

sec = 3

try:
    driver.get('https://www.naukri.com')
    # time.sleep(3)
    driver.maximize_window()
    # driver.quit()
    windows = driver.window_handles
    try:
        for i in windows:
            if not i == windows[0]:
                driver.switch_to.window(i)
                driver.close()
    except Exception as e:
        print(e)
    driver.switch_to.window(windows[0])
    # driver.switch_to_default_content()
    driver.find_element_by_id('login_Layer').click()
    # time.sleep(sec)
    element = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter your active Email ID / Username']")))
    driver.find_element_by_xpath("//input[@placeholder='Enter your active Email ID / Username']").send_keys(
        'chandanmukherjee43@gmail.com')
    driver.find_element_by_xpath("//input[@placeholder='Enter your password']").send_keys('Sai@2020')
    driver.find_element_by_xpath("//button[@type='submit']").click()
    # driver.find_element_by_link_text('My Naukri').click()
    # time.sleep(sec)
    element1 = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'My Naukri')]")))
    action = ActionChains(driver)
    action.move_to_element(
        driver.find_element_by_xpath("//div[contains(text(),'My Naukri')]")).perform()
    # time.sleep(sec)
    element2 = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.LINK_TEXT, "Edit Profile")))
    action.move_to_element(driver.find_element_by_link_text('Edit Profile')).click().perform()
    # time.sleep(sec)
    element3 = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Resume Headline']")))
    driver.find_element_by_xpath("//span[text()='Resume Headline']").click()
    driver.find_element_by_xpath("//div[@class='resumeHeadline']/div/div/div/span[2]").click()
    current_text = driver.find_element_by_xpath("//form[@name='resumeHeadlineForm']/div[2]/div/textarea").text
    print('\n\n------------')
    print("\n\nCurrent Resume Headline is: ")
    print(current_text)
    # driver.find_element_by_link_text('Save').click()
    driver.refresh()
    # time.sleep(sec)
    driver.execute_script("window.scrollTo(0, 200);")
    # time.sleep(sec)
    element4 = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Resume Headline']")))
    driver.find_element_by_xpath("//span[text()='Resume Headline']").click()
    driver.find_element_by_xpath("//div[@class='resumeHeadline']/div/div/div/span[2]").click()
    if current_text == '4.6 years of experience in IT Industry. Currently working as a Test Engineer in Tech Mahindra Ltd. Expert in Software Testing using manual as well as Python Programming Language and UI automation with Selenium WebWebDriver.':
        driver.execute_script("window.scrollTo(0, 200);")
        print("\n\n----Resume Headline changed to: ")
        driver.find_element_by_xpath('//*[@id="resumeHeadlineTxt"]').clear()
        driver.find_element_by_xpath('//*[@id="resumeHeadlineTxt"]').send_keys(
            '4.6 years of experience in IT Industry. Currently working as a Test Engineer in Tech Mahindra Ltd. Expert in Software Testing using manual as well as Python Programming Language and UI automation with Selenium WebDriver')
    else:
        driver.execute_script("window.scrollTo(0, 200);")
        driver.find_element_by_xpath('//*[@id="resumeHeadlineTxt"]').clear()
        print("\n\n----Resume Headline changed to: ")
        driver.find_element_by_xpath('//*[@id="resumeHeadlineTxt"]').send_keys(
            '4.6 years of experience in IT Industry. Currently working as a Test Engineer in Tech Mahindra Ltd. Expert in Software Testing using manual as well as Python Programming Language and UI automation with Selenium WebWebDriver.')
    driver.find_element_by_xpath(
        "//button[text()='Save' and @class='waves-effect waves-light btn-large blue-btn' ]").click()
    # driver.find_element_by_xpath('//*[@id="resumeHeadlineTxt"]').send_keys(Keys.RETURN)
    driver.refresh()
    driver.execute_script("window.scrollTo(0, 0);")
    print('\n\n----Edited the text successfully----')
    element5 = WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.XPATH, '//img[@src="https://static.naukimg.com/s/4/100/i/naukri_Logo.png"]')))
    driver.find_element_by_xpath('//img[@src="https://static.naukimg.com/s/4/100/i/naukri_Logo.png"]').click()
    # time.sleep(sec)
    print('\n\n----Clicked on main naukri logo-----')
    # action.move_to_element(
    #     driver.find_element_by_xpath('//a[@href="https://my.naukri.com/HomePage/view"]')).perform()
    # time.sleep(sec)
    # driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
    driver.quit()
    print("\n\n----Test Successful, U[dated your naukri profile----")
    print("\n\n---Smile :):):) ---")

except Exception as e:
    driver.quit()
    print('\n\n############--------Script failed--------#############')
    print("\n\n>>>Error is>>>: \n\n", e)
