# This file will be responsible for parsing the specific data
# i.e. Job roles/position, company name, company location, salary, and minimum experience.
from selenium.webdriver.remote.webelement import WebElement
import time

class GlintsReport:
    def __init__(self, boxes_section:WebElement):
        self.boxes_section = boxes_section
        self.job_roles = self.pull_job_position()
        self.companies = self.pull_company_name()
        self.location = self.pull_location()

    def pull_job_position(self):
        return self.boxes_section.find_elements(
            "xpath", 
            "//div[contains(@class, 'flLvib')]//div[contains(@class,'tUeGY')]//div//div//div//div[2]//h3[contains(@class,'iiWRnN')]")

    def pull_company_name(self):
        return self.boxes_section.find_elements(
            "xpath",
            "//div[contains(@class, 'flLvib')]//div[contains(@class,'tUeGY')]//div//div//div//div[2]//span[contains(@class,'xZssc')]//div//a")

    def pull_location(self):
        return self.boxes_section.find_elements(
            "xpath",
            "//div[contains(@class, 'flLvib')]//div[contains(@class,'tUeGY')]//div//div//div[2]/div[1]//span"
        )

    def retrieve_boxes_attributes(self):
        collect_job_position = []
        for job_role in self.job_roles:
            role = job_role.get_attribute("innerHTML").strip()
            collect_job_position.append(role)
        #print(collect_job_position[:9])
        
        collect_companies_name = []
        for company in self.companies:
            company_name = company.get_attribute("innerHTML").strip()
            collect_companies_name.append(company_name)
        #print(collect_companies_name[:9])

        collect_companies_location = []
        for loc in self.location:
            company_loc = loc.get_attribute("innerHTML").strip()
            collect_companies_location.append(company_loc)

        job_position = collect_job_position[:10]
        companies_name = collect_companies_name[:10]
        companies_loc = collect_companies_location[:10]
        collect_all = list(zip(job_position, companies_name, companies_loc))
        
        return collect_all

        #collect_job_position = []
        #collect_companies_name = []
        #for job_role, company in zip(self.job_roles, self.companies):
        #    role = job_role.get_attribute("innerHTML").strip()
        #    company_name = company.get_attribute("innerHTML").strip()
        #    collect_job_position.append(role)
        #    collect_companies_name.append(company_name)
        #print(collect_job_position[:9])
        #print(collect_companies_name[:9])