from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd
import time

data = {"Title" : [], "Info" : [], "Rating" : [], "Image" : []}

driver = webdriver.Chrome()

driver.get("https://m.imdb.com/chart/top/")

actions = ActionChains(driver, duration=2)

time.sleep(2)

card_elements = driver.find_elements("xpath", "//ul[@class = 'ipc-metadata-list ipc-metadata-list--dividers-between sc-a1e81754-0 eBRbsI compact-list-view ipc-metadata-list--base']")

for card_element in card_elements:
    card_html = card_element.get_attribute("innerHTML")
    
    soup = BeautifulSoup(card_html, "html.parser")
    
    titles = soup.find_all("h3", {"class" : "ipc-title__text"})
    imgs = soup.find_all("img", {"class" : "ipc-image" })
    infos = soup.find_all("div", {"class" : "sc-b189961a-7 feoqjK cli-title-metadata" })
    ratings = soup.find_all("span", {"aria-label" : lambda x: x and x.startswith("IMDb rating:")})
    
    for title in titles:
        # print(title.text)
        data["Title"].append(title.text)
        
    for img in imgs:
        # print(link.get("href"))
        data["Image"].append(img.get("src").split()[0])
        
    for info in infos:
        # print(info.text.strip())
        data["Info"].append(info.text)
        
    for rating in ratings:
        # print(rating.text)
        data["Rating"].append(rating.text)
    


df = pd.DataFrame.from_dict(data)
df.to_excel("Imdb.xlsx", index=False)

driver.close()
