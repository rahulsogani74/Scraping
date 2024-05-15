from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import pandas as pd
from bs4 import BeautifulSoup

driver = webdriver.Chrome()

data = {"Image_Path" : [], "Name" : [], "Price" : []}

driver.get("file:///C:/Users/jain%20computer/OneDrive/Desktop/Amazon.in.html")

time.sleep(3)

all_cards = driver.find_elements("xpath", "(//div[@class='s-main-slot s-result-list s-search-results sg-row'])")

for card in all_cards:
    card_data_html = card.get_attribute("innerHTML")
    soup = BeautifulSoup(card_data_html, "html.parser")
    
    image_div_elements = soup.find_all(class_ = "a-section aok-relative s-image-square-aspect")
    name_div_elements = soup.find_all(class_ = "a-size-base-plus a-color-base a-text-normal")
    prices = soup.find_all(class_ = "a-price-whole")
    
    min_length = min(len(image_div_elements), len(name_div_elements), len(prices))
    
    for i in range(min_length):
        
        image_div_element, name_elment, price = [None] * 3
        
        image = image_div_elements[i].find("img")
        image_path = image["srcset"].split(",")[0] if image else None
        data["Image_Path"].append(image_path)
        
        name = name_div_elements[i].text if name_div_elements[i] else None
        data["Name"].append(name)
            
        price = prices[i].text if prices[i] else None
        data["Price"].append(price)
    
    # for image_div_element in image_div_elements:
    #     image = image_div_element.find("img") if image_div_element else None
    #     # print(image["srcset"].split(",")[0])
    #     data["Image_Path"].append(image["srcset"].split(",")[0]) 
        
    
    # for name_elment in name_div_elements:
    #     # print(name_elment.text)
    #     name = name_elment.text if name_elment else None
    #     data["Name"].append(name) 
        
    
    # for price in prices:
    #     print(price.text)
    #     if price:
    #         price_value = price.text if price else None
    #         data["Price"].append(price_value) 
    #     else:
    #         data["Price"].append(0)
    
    
df = pd.DataFrame.from_dict(data)
df.to_excel("Amazon.xlsx", index=False)

driver.close()