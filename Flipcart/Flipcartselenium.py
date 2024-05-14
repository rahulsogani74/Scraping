from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
import time

from selenium.webdriver.support.select import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
   
from selenium.webdriver.common.action_chains import ActionChains
   
# Navigating to the Flipkart website
driver.get('https://www.flipkart.com/')

# Finding deal banners using XPath and printing attributes of the first deal banner
deal_banners = driver.find_elements(By.XPATH, "//div[@data-clone='false']//a")
print(f"total number of deals: {len(deal_banners)}")
for deal_banner in deal_banners:
    print(deal_banner.get_attribute("href"))
    print(deal_banner.get_attribute("innerHTML"))
    print(deal_banner.get_attribute("outerHTML"))
    break


# Finding the search bar, sending keys, and clicking on the first option in the dropdown
# Entering "one plus" into the search bar and interacting with dropdown options
search_bar = driver.find_element("xpath", "//input[@type='text']")
search_bar.send_keys("one plus")
WebDriverWait(driver, 2).until(EC.visibility_of_all_elements_located(("xpath", "(//form[contains(@class, 'header-form-search')]//a)")))
first_option = driver.find_element("xpath", "(//form[contains(@class, 'header-form-search')]//a)[1]")
print(f"link present in first option: {first_option.get_attribute('href')}")
print(f"text present in first option: {first_option.text}")
first_option.click()
print(driver.current_url)

# Iterating through dropdown options, clicking on an option containing "headphones"
dropdown_options = driver.find_elements("xpath", "(//form[contains(@class, 'header-form-search')]//a)")
for index, option in enumerate(dropdown_options):
    print(f"link present in {index + 1} option: {option.get_attribute('href')}")
    print(f"text present in {index + 1} option: {option.text}")
    if "headphones" in option.text:
        option.click()
        break
else:
    print("headphones option not found")


# Using WebDriverWait to wait until the Login element is clickable, then clicking on it
login_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//a[text()='Login']"))
)
login_element.click()

# Performing mouse actions - moving to a specific element and clicking on it
actions = ActionChains(driver, duration=2000)
time.sleep(15)
more_help_element = driver.find_element("xpath", "//a[@title='Dropdown with more help links']/parent::div")
actions.move_to_element(more_help_element).click().perform()
notification_element = driver.find_element("xpath", "//a[@href='/communication-preferences/push?t=all']")
actions.click(notification_element).perform()

time.sleep(3)

driver.close()