""" 
This script scrapes data from the IndiaMart website, categorizes it based on type, and saves it to 
an Excel file named "IndiaMartData.xlsx" with each type's data stored in a separate sheet.
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Define the URL to scrape
url = "https://dir.indiamart.com/indianexporters/ho_misce.html"

# Set the user agent header to avoid bot detection
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

# Send a GET request to the URL and parse the HTML content
res = requests.get(url, headers=headers)
soup = BeautifulSoup(res.text, 'html.parser')

# Find the element containing categories and data
ctgry_element = soup.find(class_="ctgry bgnul")

# Find all elements representing category headers and corresponding data
data_header_elements = ctgry_element.find_all(class_="s-fshz s-tilem isbimbg")
data_elements = ctgry_element.find_all(class_="s-dfx s-fwp s-flx1 s-pl5")

# Create an empty dictionary to store data for each type
data_by_type = {}

# Iterate over each category header and corresponding data
for header, data_element in zip(data_header_elements, data_elements):
    type_text = header.text.strip()  # Extract category header text
    product_text = data_element.text.strip()  # Extract corresponding data text
    
    # Check if type already exists in the dictionary
    if type_text in data_by_type:
        data_by_type[type_text].append(product_text)
    else:
        data_by_type[type_text] = [product_text]

# Write each type's data to a separate sheet in Excel
with pd.ExcelWriter("IndiaMartData.xlsx") as writer:
    for type_name, products in data_by_type.items():
        df = pd.DataFrame({"Products": products})   # Create a DataFrame for each type
        df.to_excel(writer, sheet_name=type_name, index=False)  # Write DataFrame to Excel sheet with type name

