"""
Summary:
This Python script utilizes Selenium and BeautifulSoup to scrape data from the Myntra website. 
It navigates to the men's t-shirts section, iterates through the product cards on multiple pages, 
extracts information such as image links, names, types, prices, ratings, and actual prices (if available),
and stores the data in a dictionary. The extracted data is then converted into a DataFrame and saved 
to an Excel file named "Myntra.xlsx". Finally, a completion message is printed.
"""
# Importing necessary libraries
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import pandas as pd
import time


# Setting up Chrome WebDriver
driver = webdriver.Chrome()

# Dictionary to store scraped data
data = {"Image_Link": [], "Name": [], "Type": [], "Rating": [], "Price": [], "Actual_Price": []}

# Navigating to the Myntra webpage
driver.get("https://www.myntra.com/men-tshirts?f=Categories%3ALounge%20Tshirts&rf=Price%3A1106.0_2013.0_1106.0%20TO%202013.0")

# Setting up actions for mouse hover
actions = ActionChains(driver, duration=2)

time.sleep(3)

# Function to extract card information
def card(driver):
    # Finding all card elements containing product information
    card_elements = driver.find_elements("xpath", "//ul[@class='results-base']")

    for card_element in card_elements:
        card_element_html = card_element.get_attribute("innerHTML")
        soup = BeautifulSoup(card_element_html, "html.parser")
        
        products = soup.find_all(class_="product-base")
        
        # Iterating through each product to extract data
        for product in products:
            # Initialize variables
            link, name, prod_type, price, rating, actual_price = [None] * 6
            
            # Extracting image link 
            images = product.find_all(class_="img-responsive")
            link = images[0].find("img").get('src') if images else None
            
            # Extracting product name
            names = product.find_all(class_="product-brand")
            name = names[0].text if names else None
            
            # Extracting product type
            types = product.find_all(class_="product-product")
            prod_type = types[0].text if types else None
            
            # Extracting product price
            prices = product.find_all(class_="product-discountedPrice")
            if not prices:
                prices = product.find_all(class_="product-price")
            price = prices[0].text if prices else None
            
            # Extracting product rating
            ratings = product.find_all(class_="product-ratingsContainer")
            rating = ratings[0].text if ratings else None
            
            # Extracting actual price (if available)
            Actual_Prices = product.find_all(class_="product-strike")
            actual_price = Actual_Prices[0].text if Actual_Prices else None
            
            # Appending data to dictionary
            data["Image_Link"].append(link)
            data["Name"].append(name)
            data["Type"].append(prod_type)
            data["Price"].append(price)
            data["Rating"].append(rating)
            data["Actual_Price"].append(actual_price)
           

# Looping through pages to extract all data
while True:
    card(driver)
    try:
        next_element = driver.find_element("xpath", "//li[@class='pagination-next']")
        actions.click(next_element).perform()
        time.sleep(2)
    except:
        break


# Creating a DataFrame from the extracted data
df = pd.DataFrame.from_dict(data)

# Saving the DataFrame to an Excel file
df.to_excel("Mintra.xlsx", index=False)

# Printing completion message
print("Work Done!!!")
