from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import pandas as pd
import time

driver = webdriver.Chrome()

data = {"RANK" : [], "NAME" : [], "NET WORTH" : [],	"CHANGE" : [],	"AGE" : [],	"SOURCE" : [], "COUNTRY/TERRITORY" : []}

driver.get("https://www.forbes.com/real-time-billionaires/#350f4d883d78")

actions = ActionChains(driver, duration=2)

time.sleep(3)

cards_elements = driver.find_elements("xpath", "//table[@ng-table-dynamic = 'tableParams with columns']")

for card_element in cards_elements:
    card_html = card_element.get_attribute("innerHTML")
    # print(card_html)
    
    soup = BeautifulSoup(card_html, "html.parser")
    
    ranks = soup.find_all("td", {"class" : "rank"})
    names = soup.find_all("td", {"class" : "name"} )
    Net_Worths = soup.find_all("td", {"class" : "Net Worth"})
    changes = soup.find_all("td", {"class" : "change"})
    ages = soup.find_all("td", {"class" : "age"})
    sources = soup.find_all("td", {"class" : "source"})
    countrys = soup.find_all("td", {"class" : "Country/Territory"})
    
    for i in range(len(names)):
        rank = ranks[i].text
        name = names[i].text
        Net_Worth = Net_Worths[i].text
        change = changes[i].text
        age = ages[i].text 
        source = sources[i].text
        country = countrys[i].text
        
        # print(name, "\t", Net_Worth, "\t", change, "\t", age, "\t", source, "\t", country)
        data["RANK"].append(rank)
        data["NAME"].append(name)
        data["NET WORTH"].append(Net_Worth)
        data["CHANGE"].append(change)
        data["AGE"].append(age)
        data["SOURCE"].append(source)
        data["COUNTRY/TERRITORY"].append(country)
        

df = pd.DataFrame.from_dict(data)
df.to_excel("ForbesTopRichestPeople.xlsx", index=False)
        
driver.close()