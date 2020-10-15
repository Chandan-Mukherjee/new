from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import Relative_Project_Path

for i in range(2):
    driver = webdriver.Chrome(
        executable_path=Relative_Project_Path.driver_path + 'chromedriver.exe')

    sec = 1.5

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
        time.sleep(sec)
        driver.find_element_by_xpath("//input[@placeholder='Enter your active Email ID / Username']").send_keys(
            'chandanmukherjee43@gmail.com')
        driver.find_element_by_xpath("//input[@placeholder='Enter your password']").send_keys('Sai@2020')
        driver.find_element_by_xpath("//button[@type='submit']").click()
        # driver.find_element_by_link_text('My Naukri').click()
        time.sleep(sec)
        action = ActionChains(driver)
        action.move_to_element(
            driver.find_element_by_xpath("//div[contains(text(),'My Naukri')]")).perform()
        time.sleep(sec)
        action.move_to_element(driver.find_element_by_link_text('Edit Profile')).click().perform()
        time.sleep(sec)
        driver.find_element_by_xpath("//span[text()='Resume Headline']").click()
        driver.find_element_by_xpath("//div[@class='resumeHeadline']/div/div/div/span[2]").click()
        current_text = driver.find_element_by_xpath("//form[@name='resumeHeadlineForm']/div[2]/div/textarea").text
        print('\n------------')
        print(current_text)
        # driver.find_element_by_link_text('Save').click()
        driver.refresh()
        time.sleep(sec)
        driver.execute_script("window.scrollTo(0, 200);")
        time.sleep(sec)
        driver.find_element_by_xpath("//span[text()='Resume Headline']").click()
        driver.find_element_by_xpath("//div[@class='resumeHeadline']/div/div/div/span[2]").click()
        if current_text == '4.6 years of experience in IT Industry. Currently working as a Test Engineer in Tech Mahindra Ltd. Expert in Software Testing using manual as well as Python Programming Language and UI automation with Selenium WebWebDriver.':
            driver.execute_script("window.scrollTo(0, 200);")
            driver.find_element_by_xpath('//*[@id="resumeHeadlineTxt"]').clear()
            driver.find_element_by_xpath('//*[@id="resumeHeadlineTxt"]').send_keys(
                '4.6 years of experience in IT Industry. Currently working as a Test Engineer in Tech Mahindra Ltd. Expert in Software Testing using manual as well as Python Programming Language and UI automation with Selenium WebDriver')
        else:
            driver.execute_script("window.scrollTo(0, 200);")
            driver.find_element_by_xpath('//*[@id="resumeHeadlineTxt"]').clear()
            driver.find_element_by_xpath('//*[@id="resumeHeadlineTxt"]').send_keys(
                '4.6 years of experience in IT Industry. Currently working as a Test Engineer in Tech Mahindra Ltd. Expert in Software Testing using manual as well as Python Programming Language and UI automation with Selenium WebWebDriver.')
        driver.find_element_by_xpath(
            "//button[text()='Save' and @class='waves-effect waves-light btn-large blue-btn' ]").click()
        # driver.find_element_by_xpath('//*[@id="resumeHeadlineTxt"]').send_keys(Keys.RETURN)
        driver.refresh()
        driver.execute_script("window.scrollTo(0, 0);")
        print('\n----Edited the text successfully----\n')
        driver.find_element_by_xpath('//img[@src="https://static.naukimg.com/s/4/100/i/naukri_Logo.png"]').click()
        time.sleep(sec)
        print('\n----Clicked on main naukri logo-----')
        # action.move_to_element(
        #     driver.find_element_by_xpath('//a[@href="https://my.naukri.com/HomePage/view"]')).perform()
        # time.sleep(sec)
        # driver.find_element_by_xpath("//a[contains(text(),'Logout')]").click()
        driver.quit()

    except Exception as e:
        driver.quit()
        print('\n############--------Script failed--------#############\n')
        print(">>>Error is>>>: \n\n\n", e)
