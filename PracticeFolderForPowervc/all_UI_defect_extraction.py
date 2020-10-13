from selenium import webdriver
import Relative_Project_Path
import os
import time


class All_UI_Defect_Extraction:

    def __init__(self):
        pass

    @staticmethod
    def extract_defect():
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")
        prefs = {"profile.default_content_settings.popups": 0,
                 "download.default_directory": r"C:\Users\ChandanMukherjee\Desktop\\",
                 # IMPORTANT - ENDING SLASH V IMPORTANT
                 "directory_upgrade": True}
        options.add_experimental_option("prefs", prefs)
        chromedriver = Relative_Project_Path.driver_path + 'chromedriver.exe'
        driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=options)
        driver.maximize_window()
        driver.delete_all_cookies()
        driver.implicitly_wait(200)
        driver.get(
            'https://jazz04.rchland.ibm.com:12443/jazz/web'
            '/projects/Janus#action=com.ibm.team.workitem.runSavedQuery&id=_PZ2B0JjVEeqCTZE3K1N-Uw&index=1&orderBy=owner&direction=ascending&itemsPerPage=all&preserveFilter=true')

        driver.find_element_by_id('jazz_app_internal_LoginWidget_0_userId').send_keys('chandn23@in.ibm.com')
        driver.find_element_by_id('jazz_app_internal_LoginWidget_0_password').send_keys('Sai@202012345678901')
        driver.find_element_by_xpath("//button[@type='submit']").click()
        os.chdir(r'C:\Users\ChandanMukherjee\Desktop')
        driver.find_element_by_xpath("//img[@alt='Download as Spreadsheet (.csv)']").click()
        time.sleep(60)
        driver.find_element_by_xpath("//span[@class='caret jazz-ui-MenuPopup-caret']").click()


all_ui_defect_extraction = All_UI_Defect_Extraction
all_ui_defect_extraction.extract_defect()
