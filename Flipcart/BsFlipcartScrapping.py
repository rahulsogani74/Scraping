"""
This code performs web scraping on Flipkart to retrieve iPhone product names and prices, stores the data 
in a DataFrame, and saves it to an Excel file named "data.xlsx".
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Initialize a dictionary to store data
data = {"Title" : [], "Price" : []}

# URL of the website to scrape
url = "https://www.flipkart.com/search?q=iphone&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_4_1_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_4_1_na_na_na&as-pos=4&as-type=RECENT&suggestionId=iphone&requestId=25f7bc18-57b4-469e-8340-39f955783d06&as-backfill=on"

# Set headers to simulate a request from a browser
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Send a GET request to the URL
res = requests.get(url, headers=headers)

# Create a BeautifulSoup object    
soup = BeautifulSoup(res.text, 'html.parser')

# Printing the prettified HTML content
print(soup.prettify())

# Finding the discount section
dis = soup.find(class_="tUxRFH")
print(dis)

print("\n")

# Selecting all product names
names = soup.select("div.KzDlHZ")

# Extracting and printing product names
for name in names:
    print(name.string)
    data["Title"].append(name.string)

# Selecting all product prices
prices = soup.select("div.cN1yYO")

# Extracting and printing product prices
for price in prices:
    print(price.find(class_="Nx9bqj").get_text())
    data["Price"].append(price.find(class_="Nx9bqj").get_text())

# for price in prices:
#     print(price.string)
#     data["price"].append(price.string)
    
# Creating a DataFrame from the collected data    
df = pd.DataFrame.from_dict(data)

# Saving the DataFrame to an Excel file
df.to_excel("data.xlsx", index=False)

# Printing the DataFrame
print(df)