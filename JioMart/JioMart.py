"""
Summary:
This Python script uses Selenium and BeautifulSoup to scrape smartphone data from the JioMart website. 
It navigates to the relevant webpage, scrolls down to load all products, extracts product information 
including image links, names, and prices, stores the data in a dictionary, converts it into a DataFrame, 
and saves it to an Excel file named "JioMart.xlsx". Finally, it prints a completion message.
"""


# Importing necessary libraries
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import pandas as pd
import time

# Setting up a headless Chrome WebDriver
option= webdriver.ChromeOptions()
option.add_argument('headless')

driver = webdriver.Chrome(options=option)

# Dictionary to store scraped data
data = {"Image_link" : [], "Name" : [], "Price" : []}

# Navigating to the JioMart webpage
driver.get("https://www.jiomart.com/c/electronics/mobiles-tablets/smartphones/777")

# Setting up actions for mouse hover
actions = ActionChains(driver, duration=2)

# Pausing to allow time for page content to load
time.sleep(5)

# Scroll down the page to load all products
SCROLL_PAUSE_TIME = 2
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        break
    last_height = new_height


# Finding all card elements containing product information
card_elements = driver.find_elements("xpath", "//ol[@class = 'ais-InfiniteHits-list jm-row jm-mb-massive']")

# Iterating through each card element to extract data
for card_element in card_elements:
    card_element_html = card_element.get_attribute("innerHTML")
    #actions.click(card_element).perform()
    soup = BeautifulSoup(card_element_html, "html.parser")
    
    # Extracting image links
    images_div = soup.find_all(class_ = "plp-card-image")
    
    for image_div in images_div:
        if image_div:
            image_tag = image_div.find('img')
            if image_tag:
                src_link = image_tag.get('data-src')
                data["Image_link"].append(src_link)
                # print(src_link)
    
    
    # Extracting product names and prices
    cards = soup.find_all(class_ = "plp-card-details-container")
    
    for card in cards:
        name = card.find(class_ = "plp-card-details-name line-clamp jm-body-xs jm-fc-primary-grey-80")
        
        data["Name"].append(name.text)
        # print(name.text)
        
        price = card.find(class_ = "jm-heading-xxs jm-mb-xxs")
        # print(price.text)
        data["Price"].append(price.text)
        
        #print(card.text.split())
    
    #print(image)
    #print("card : ", card)
    
    # print(soup.prettify())
    
    
# Creating a DataFrame from the extracted data
df = pd.DataFrame.from_dict(data)

# Saving the DataFrame to an Excel file
df.to_excel("JioMart.xlsx", index=False)

# Printing completion message
print("Work Done!!!")