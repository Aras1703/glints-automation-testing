# This file will be responsible to apply the filter jobs in our test case.
# This file includes an instance methods.
from selenium.webdriver.remote.webdriver import WebDriver

class GlintsFiltration:
    def __init__(self, driver:WebDriver):
        self.driver = driver
    
    def job_types(self, *category):
        #self.refresh()
        job_types = self.driver.find_element("xpath", "//div[contains(@class,'modal-dialog')]")
        types = job_types.find_elements("xpath", 
        "//div[contains(@class,'FilterList')]//div[2]//div//div[2]//div//div[contains(@class,'bfChNc')]//label[contains(@for,'jobTypes')]")
        for cat in category:
            for type in types:
                if str(type.get_attribute("innerHTML")) == str(cat).capitalize():
                    type.click()

    def remote_option(self):
        remote_work = self.driver.find_element("xpath", "//div[contains(@class,'fFULNn')]//button")
        remote_work.click()

    def work_locations(self, *towns):
        locations = self.driver.find_element("xpath", "//div[contains(@class,'modal-dialog')]")
        cities = locations.find_elements("xpath", 
        "//div[contains(@class,'FilterList')]//div[4]//div//div[2]//div//div[contains(@class,'bfChNc')]//label[contains(@for,'cities')]")
        for town in towns:
            for city in cities:
                if str(city.get_attribute("for")) == f"cities{town}":
                    city.click()

    def work_experiences(self, *years):
        experiences = self.driver.find_element("xpath", "//div[contains(@class,'modal-dialog')]")
        experience = experiences.find_elements("xpath",
        "//div[contains(@class,'FilterList')]//div[5]//div//div[2]//div//div[contains(@class,'bfChNc')]//label[contains(@for,'ExperienceFilter')]")
        for year in years:
            for exp in experience:
                if str(exp.get_attribute("for")) == f"yearsOfExperienceFilter{year}":
                    exp.click()

    def exclude_experience(self):
        exclude = self.driver.find_element("xpath", "//div[contains(@class,'FilterList')]//div[5]//div//div[2]//div[2]//div//button")
        exclude.click()
    
    def block_advertisement(self):
        block_advertise = self.driver.find_element("xpath", 
                         "//div[contains(@class,'iZIzpf')]/div/div/div/header/button")
        block_advertise.click()