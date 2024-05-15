from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import time

import pandas as pd

option = webdriver.ChromeOptions()
option.add_argument('headless')

driver = webdriver.Chrome(options=option)

driver.get("https://groww.in/")

actions = ActionChains(driver, duration=2)

data = {"Name" : [], "Market_Price" : [], "52_W_Low" : [], "52_W_High" : []}

time.sleep(5)

stoke_element = driver.find_element("xpath", "//a[@href = '/stocks']")
actions.move_to_element(stoke_element).click().perform()

time.sleep(5)

driver.switch_to.window(driver.window_handles[1])

filter_element = driver.find_element("xpath", "//a[@href = '/markets']")
actions.move_to_element(filter_element).click().perform()

time.sleep(5)

driver.switch_to.window(driver.window_handles[2])

time.sleep(5)

stock_details = driver.find_element("xpath", "//tbody[@style = 'position: relative;']")
actions.move_to_element(stock_details).click().perform()
stock_html = stock_details.get_attribute("innerHTML")
# print(stock_html)

soup = BeautifulSoup(stock_html, "html.parser")
# print(soup.prettify())

def stock(soup):
    names = soup.find_all(class_ = "mtp438CompanyName bodyBase")
    
    marck_prices = soup.find_all(class_ = "bodyBaseHeavy")
    
    Low_52_Wss = soup.find_all(style = "padding-top: 15px; padding-bottom: 15px; text-align: right;")
    
    High_52_wss = soup.find_all(style = "padding-right: 3%; padding-top: 15px; padding-bottom: 15px; text-align: right;") 
    
    for i in range(len(names)):
        
        # Extract only the first value from the repeated class
        name = names[i].text
        market_price = marck_prices[i].text
        low_52_week = Low_52_Wss[i].text
        High_52_week = High_52_wss[i].text
        
        # Append to data dictionary
        data["Name"].append(name)
        data["Market_Price"].append(market_price)
        data["52_W_Low"].append(low_52_week)
        data["52_W_High"].append(High_52_week)
        
        # for name in names:
        #     # print(name.text, "\t")
        #     data["Name"].append(name.text)
        
        # for marck_price in marck_prices:
        #     # print(marck_price.text, "\t")
        #     data["Market_Price"].append(marck_price.text)
            
        # for Low_52_W in Low_52_Wss:
        #     # print(Low_52_W.text)
        #     data["52_W_Low"].append(Low_52_W.text)


SCROLL_PAUSE_TIME = 2
last_height = driver.execute_script("return arguments[0].scrollHeight;", stock_details)
while True:
    stock(soup)
    driver.execute_script("arguments[0].scrollTo(0, arguments[0].scrollHeight);", stock_details)
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return arguments[0].scrollHeight;", stock_details)
    if new_height == last_height:
        break
    last_height = new_height
        
        
time.sleep(5)

df = pd.DataFrame.from_dict(data)
df.to_excel("GrowwStock.xlsx", index=False)

driver.close()
print("--- Work Done ---")