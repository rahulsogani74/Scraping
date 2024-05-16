from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time 
import pandas as pd

data = {"Rank" : [], "Name" : [], "Revenue" : [], "Year" : []} 

driver = webdriver.Chrome()

driver.get("https://en.wikipedia.org/wiki/List_of_highest-grossing_films")

card_elements = driver.find_elements("xpath", "(//table[@class = 'wikitable sortable plainrowheaders sticky-header col4right col5center col6center jquery-tablesorter'])//tbody")

for card_element in card_elements:
    card_html = card_element.get_attribute("innerHTML")
    # print(card_html)
    
    soup = BeautifulSoup(card_html, "html.parser")
    
    lists = soup.find_all("tr")
    
    for list in lists:
        # print(list.text)
        # card_data = list.text.strip()
        Rank = list.find("td").text
        Name = list.find("th").text
        Revenue = list.find_all("td")[2].text
        Year = list.find_all("td")[3].text
        
        # print(card_data)
        
        # Rank = card_data[0]
        # Name = card_data[2]
        # Revenue = card_data[3]
        # Year = card_data[4]
        
        # print(Rank, "\t", Name) 
          
        data["Rank"].append(Rank)
        data["Name"].append(Name)
        data["Revenue"].append(Revenue)
        data["Year"].append(Year)
        

df = pd.DataFrame.from_dict(data)
df.to_excel("HighestGrossingFilms.xlsx", index=False)     