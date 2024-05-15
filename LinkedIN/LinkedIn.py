from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome()

data = {"Name" : [], "Company" : [], "Link" : []}

driver.get("https://in.linkedin.com/")

time.sleep(3)

actions = ActionChains(driver, duration=2)

job_nav_element = driver.find_element("xpath", "//li[4]/a/span")
actions.click(job_nav_element).perform()

time.sleep(5)

job_cards = driver.find_elements("xpath", "//ul[@class = 'jobs-search__results-list']")

for job_card in job_cards:
    job_card_html = job_card.get_attribute("innerHTML")
    
    soup = BeautifulSoup(job_card_html, "html.parser")
    
    links = soup.find_all("a", {"data-tracking-control-name": "public_jobs_jserp-result_search-card"})
    names = soup.find_all("h3", {"class" : "base-search-card__title"})
    companies = soup.find_all("h4", {"class" : "base-search-card__subtitle"})
    
    
    for link in links:
        # print((link.get("href")))
        data["Link"].append((link.get("href")))
        
    for name in names:
        # print(name.text)
        data["Name"].append(name.text.strip())
        
    for company in companies:
        # print(company.text)   
        data["Company"].append(company.text.strip()) 
    
time.sleep(3)

df = pd.DataFrame.from_dict(data)
df.to_excel("LinkedIn.xlsx", index=False)

driver.close() 