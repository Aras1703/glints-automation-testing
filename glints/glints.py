import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import glints.constants as const
from glints.glints_filtration import GlintsFiltration
from glints.glints_report import GlintsReport
from prettytable import PrettyTable
import time


class Glints(webdriver.Chrome):
    def __init__(self, driver_path=r"C:\Selenium Drivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        #options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_experimental_option("detach", True)
        super(Glints, self).__init__(service=Service(ChromeDriverManager().install()),
                                       options=options)
        self.implicitly_wait(15)
        self.maximize_window()
    
    def quit(self):
        if self.teardown == True:
            self.quit()

    def glints_test(self):
        self.get(const.BASE_URL)
        self.implicitly_wait(15)
        self.maximize_window()

    def dropdown_languages(self, language):
        choose_language = self.find_element("xpath", "//span[@class]")
        choose_language.click()

        pick = self.find_element("xpath", f"//li[{const.languages[language]}]")
        pick.click()

    def to_login_page(self, email_phone, password):
        login_page = self.find_element("xpath", "//nav//div[5]//div[3]//div//span")
        login_page.click()

    #def credential(self, email_phone, password):
        put_email = self.find_element("id", "login-form-email")
        put_email.send_keys(email_phone)

        put_password = self.find_element("id", "login-form-password")
        put_password.send_keys(password)

        login = self.find_element("xpath", "//form/div[4]//button")
        login.click()

    def to_jobs_page(self):
        time.sleep(2)
        #self.refresh()
        jobs_page = self.find_element("css selector", "a[aria-label='Jobs page']")
        jobs_page.click()

    def to_explore_page(self):
        time.sleep(2)
        #self.refresh()
        explore_page = self.find_element("xpath", "//ul/li[2]//button")
        explore_page.click()

    def search_jobs(self, search):
        search_box = self.find_element("xpath", "//div[contains(@class,'jIWpso')]//div[1]//input")
        search_box.click()
        search_box.send_keys(search)

        searching = self.find_element("css selector", "button[aria-label='Search button']")
        searching.click()
    
    def job_filtration(self):
        filter = GlintsFiltration(driver=self)
        filter.job_types('internship', 'freelance')
        filter.remote_option()
        filter.work_locations(const.loc.get("Jkt"), const.loc.get("Bdg"))
        #filter.block_advertisement()
        filter.work_experiences(const.exp.get("<1"), const.exp.get("1-3"))
        filter.exclude_experience()
    
    def report_summary(self):
        job_boxes = self.find_element("xpath", "//div[contains(@class,'dPOPcp')]")
        report = GlintsReport(job_boxes)
        #print(len(report.pull_deal_boxes()))
        display_table = PrettyTable(
            field_names=["Job Position (Roles)", "Company", "Location"]
        )
        display_table.add_rows(report.retrieve_boxes_attributes())
        print(display_table)
        
        
