from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import glints.constants as const

option = Options()
option.add_experimental_option("detach", True)

driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), 
                          options = option)

def glints_test():
    driver.get(const.BASE_URL)
    driver.implicitly_wait(15)
    driver.maximize_window()

def dropdown_languages(language):
    choose_language = driver.find_element("xpath", "//span[@class]")
    choose_language.click()

    pick = driver.find_element("xpath", f"//li[{const.languages[language]}]")
    pick.click()

def to_login_page():
    login_page = driver.find_element("xpath", "//nav//div[5]//div[3]//div//span")
    login_page.click()

    put_email = driver.find_element("id", "login-form-email")
    put_email.click()
    put_email.send_keys(const.credential['email'])

    put_password = driver.find_element("id", "login-form-password")
    put_password.click()
    put_password.send_keys(const.credential['password'])

    login = driver.find_element("xpath", "//form/div[4]//button")
    login.click()

def to_jobs_page():
    jobs_page = driver.find_element("css selector", "a[aria-label='Jobs page']")
    jobs_page.click()

    #jobs_page = driver.find_element("xpath", "//nav/div[1]/a")
    #jobs_page.click()

def to_explore_page():
    explore_page = driver.find_element("xpath", "//ul/li[2]//button")
    explore_page.click()

def search_jobs(search):
    search_box = driver.find_element("xpath", "//div[contains(@class,'jIWpso')]//div[1]//input")
    search_box.click()
    search_box.send_keys(search)
    
    searching = driver.find_element("css selector", "button[aria-label='Search button']")
    searching.click()

def job_types(*category):
    job_types = driver.find_element("xpath", "//div[contains(@class,'modal-dialog')]")
    types = job_types.find_elements("xpath", 
    "//div[contains(@class,'FilterList')]//div[2]//div//div[2]//div//div[contains(@class,'bfChNc')]//label[contains(@for,'jobTypes')]")
    for cat in category:
        for type in types:
            if str(type.get_attribute("innerHTML")) == str(cat).capitalize():
                type.click()

def remote_option():
    remote_work = driver.find_element("xpath", "//div[contains(@class,'fFULNn')]//button")
    remote_work.click()

def work_locations(*towns):
    locations = driver.find_element("xpath", "//div[contains(@class,'modal-dialog')]")
    cities = locations.find_elements("xpath", 
    "//div[contains(@class,'FilterList')]//div[4]//div//div[2]//div//div[contains(@class,'bfChNc')]//label[contains(@for,'cities')]")
    for town in towns:
        for city in cities:
            if str(city.get_attribute("for")) == f"cities{town}":
                city.click()

def work_experiences(*years):
    experiences = driver.find_element("xpath", "//div[contains(@class,'modal-dialog')]")
    experience = experiences.find_elements("xpath",
    "//div[contains(@class,'FilterList')]//div[5]//div//div[2]//div//div[contains(@class,'bfChNc')]//label[contains(@for,'ExperienceFilter')]")
    for year in years:
        for exp in experience:
            if str(exp.get_attribute("for")) == f"yearsOfExperienceFilter{year}":
                exp.click()

def exclude_experience():
    exclude = driver.find_element("xpath", "//div[contains(@class,'FilterList')]//div[5]//div//div[2]//div[2]//div//button")
    exclude.click()

def block_advertises():
    block_advertise = driver.find_element("xpath", 
                     "//div[contains(@class,'iZIzpf')]/div/div/div/header/button")
    block_advertise.click()