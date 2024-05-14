"""
Summary:
The script navigates to the Flipkart website and selects the 'Mobiles' category.
It then selects multiple brands by clicking checkboxes.
The script defines a function to extract data (such as image path, name, price, and rating) from each product card on the page.
It loops through multiple pages to extract data from each page.
After collecting data from all pages, it creates a DataFrame using pandas and saves it to an Excel file.
Finally, it closes the browser window.

"""

# Importing required modules
from selenium import webdriver

# Importing the By class for locating elements
from selenium.webdriver.common.by import By

# Importing WebDriverWait for waiting for elements
from selenium.webdriver.support.ui import WebDriverWait

# Importing expected_conditions for defining expected conditions
from selenium.webdriver.support import expected_conditions as EC

# Importing ActionChains for performing mouse actions
from selenium.webdriver.common.action_chains import ActionChains

# Importing Select class for interacting with dropdowns
from selenium.webdriver.support.select import Select

# Importing pandas for data manipulation
import pandas as pd

# Importing BeautifulSoup for HTML parsing
from bs4 import BeautifulSoup

# Importing time module for pausing execution
import time

# Initializing a dictionary to store data
data = {"Image_Path": [], "Name": [], "Actual_Price": [], "Price": [], "Rating": []}

# Initializing a Chrome WebDriver instance
driver = webdriver.Chrome()
driver.get("https://www.flipkart.com/")

# Initializing ActionChains for performing mouse actions
actions = ActionChains(driver, duration=2000)
time.sleep(3)

# Navigating to the 'Mobiles' category
ctgy_element = driver.find_element("xpath", "//a[@aria-label='Mobiles']")
actions.click(ctgy_element).perform()

# mobile_first_choice = driver.find_element("xpath", "//*[@id='container']/div/div[3]/div[16]/div/div[1]/div[2]/a/span")
# actions.click(mobile_first_choice).perform()

# time.sleep(3)


# Navigating to the 'Mobiles' category
brands = ['SAMSUNG', 'vivo', 'OPPO', 'realme', 'POCO', 'MOTOROLA']
for brand in brands:
    input_element = driver.find_element("xpath", f"(//div[text() = '{brand}']/parent::label)[1]")
    actions.click(input_element).perform()
    time.sleep(3)

# first_input = driver.find_element("xpath", "(//div[text() = 'SAMSUNG']/parent::label)[1]")
# actions.click(first_input).perform()
# time.sleep(3)


# second_input = driver.find_element("xpath", "(//div[text() = 'vivo']/parent::label)[1]")
# actions.click(second_input).perform()
# time.sleep(3)

# first_input = driver.find_element("xpath", "(//div[text() = 'OPPO']/parent::label)[1]")
# actions.click(first_input).perform()
# time.sleep(3)


# second_input = driver.find_element("xpath", "(//div[text() = 'realme']/parent::label)[1]")
# actions.click(second_input).perform()
# time.sleep(3)

# first_input = driver.find_element("xpath", "(//div[text() = 'POCO']/parent::label)[1]")
# actions.click(first_input).perform()
# time.sleep(3)


# second_input = driver.find_element("xpath", "(//div[text() = 'MOTOROLA']/parent::label)[1]")
# actions.click(second_input).perform()
# time.sleep(3)

# container_elements = driver.find_elements("xpath","(//div[@style = 'flex-grow: 1; overflow: auto;'])[1]")

# for container_element in container_elements:
#     container_element_html = container_element.get_attribute("innerHTML")
#     soup = BeautifulSoup(container_element_html, "html.parser")

#     div_elements = soup.find_all("div", recursive=False)
#     card_elements = div_elements[1:-4]
#     for card_element in card_elements:
#         name_price_rating_elements = card_element.find_all("div")
#         img_element = card_element.find("img").get("src")
#         #name_element = card_element.find_all("div")[14].find("span").find("div").text.strip()

#         #rating_element = card_element.find_all("div")[14].text.strip()
#         #price_element1 = card_element.find("div").find_all("div")[0].find_all("div")
        
#         name_element = card_element.find('div', {"class":'KzDlHZ'}).text.strip()
        
#         #price_element1 = card_element.find_element(By.XPATH, ".//a/div[3]/div[2]/div[1]/div[1]/div[1]").text.strip()
#         price_element2 = card_element.find('div', {"class":'Nx9bqj _4b5DiR'}).text.strip()
#         price_element1 = card_element.find('div', {"class":'yRaY8j ZYYwLA'}).text.strip()
#         rating_element = card_element.find('div', {"class":'XQDdHH'}).text.strip()
        
#         # print("card :", img_element, "\n" )
#         # print("card :", name_element, "\n" )
#         # print("card :", rating_element, "\n")
        
#         # print("card :", price_element1, "\n")
#         # print("card :", price_element2, "\n")
        
# #time.sleep(3)


# Function to extract data from each page
def data_get(driver):
    container_elements = driver.find_elements("xpath","(//div[@style = 'flex-grow: 1; overflow: auto;'])[1]")

    for container_element in container_elements:
        container_element_html = container_element.get_attribute("innerHTML")
        soup = BeautifulSoup(container_element_html, "html.parser")

        div_elements = soup.find_all("div", recursive=False)
        card_elements = div_elements[1:-2]
        for card_element in card_elements:
            img_element = card_element.find("img").get("src")
            #name_element = card_element.find_all("div")[14].find("span").find("div").text.strip()

            #rating_element = card_element.find_all("div")[14].text.strip()
            #price_element1 = card_element.find("div").find_all("div")[0].find_all("div")
            
            name_element = card_element.find('div', {"class":'KzDlHZ'}).text.strip()
            
            #price_element1 = card_element.find_element(By.XPATH, ".//a/div[3]/div[2]/div[1]/div[1]/div[1]").text.strip()
            
            try:
                price_element1 = card_element.find('div', {"class": 'yRaY8j ZYYwLA'}).text.strip()
                
            except:
                price_element1 = "Not Available"
                
            try:
                price_element2 = card_element.find('div', {"class":'Nx9bqj _4b5DiR'}).text.strip()
                
            except:
                price_element2 = "Not Available"
        
            rating_element = card_element.find('div', {"class":'XQDdHH'}).text.strip()
            
            # Appending data to the dictionary
            data["Image_Path"].append(img_element)
            
            data["Name"].append(name_element)
            
            data["Actual_Price"].append(price_element1)
            
            data["Price"].append(price_element2)
            
            data["Rating"].append(rating_element)
            
            
            # print("card :", img_element, "\n" )
            
            # print("card :", name_element, "\n" )
            # print("card :", rating_element, "\n")
            
            # print("card :", price_element1, "\n")
            # print("card :", price_element2, "\n")
            
    time.sleep(3)
     

        
# Looping through multiple pages to extract data
while True:
    # time.sleep(3)
    # container_elements = driver.find_elements("xpath","(//div[@style = 'flex-grow: 1; overflow: auto;'])[1]")

    # for container_element in container_elements:
    #     container_element_html = container_element.get_attribute("outerHTML")
    #     soup = BeautifulSoup(container_element_html, "html.parser")
    #     #print(soup.prettify())
    #     div_elements = soup.find_all("div", recursive=False)
    
    #     card_elements = div_elements[1:-4]
    #     for card_element in card_elements:
    #         name_price_rating_elements = card_element.find_all("div")
    #         img_element = card_element.find("img").get("src")
    #         #name_element = card_element.find_all("div")[14].find("span").find("div").text.strip()

    #         #rating_element = card_element.find_all("div")[14].text.strip()
    #         #price_element1 = card_element.find("div").find_all("div")[0].find_all("div")
        
    #         name_element = card_element.find('div', {"class":'KzDlHZ'}).text.strip()
        
    #         #price_element1 = card_element.find_element(By.XPATH, ".//a/div[3]/div[2]/div[1]/div[1]/div[1]").text.strip()
    #         price_element2 = card_element.find('div', {"class":'Nx9bqj _4b5DiR'}).text.strip()
    #         price_element1 = card_element.find('div', {"class":'yRaY8j ZYYwLA'}).text.strip()
    #         rating_element = card_element.find('div', {"class":'XQDdHH'}).text.strip()
            
    try:         
        next_btn_element = driver.find_element("xpath", "//span[text()='Next']")
        time.sleep(3)
        
        if next_btn_element:
            next_btn_element.click()
            data_get(driver)
            time.sleep(3)

    except:
       break


# Extracting data from the last page
data_get(driver)

time.sleep(5)

# Creating a DataFrame from the collected data and saving it to an Excel file
df = pd.DataFrame.from_dict(data)
df.to_excel("flipcartMobileData.xlsx", index=False)
print(df)

# Closing the browser window
driver.close()