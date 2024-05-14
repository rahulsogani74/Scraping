from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initializing a Chrome WebDriver instance
driver = webdriver.Chrome()

from selenium.webdriver.support.select import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
   
from selenium.webdriver.common.action_chains import ActionChains
   
# Navigating to the Flipkart website   
driver.get('https://www.flipkart.com/')

# Performing mouse actions to click on the Login element
actions = ActionChains(driver, duration=2000)
login_element = driver.find_element("xpath", "//a[@title='Login']")
actions.move_to_element(login_element).click().perform()

# Entering login credentials and requesting OTP
login_id_input = driver.find_element("xpath", "//span[text()='Enter Email/Mobile number']")
actions.click(login_id_input).send_keys("saj000777@gmail.com").perform()

request_otp = driver.find_element("xpath", "//button[text() = 'Request OTP']")

actions.click(request_otp).perform()
time.sleep(5)

# Waiting for the captcha frame to appear
press_hold = ("xpath", "//*[@id='px-captcha']//iframe[3]" )
WebDriverWait(driver, 5).until(EC.visibility_of_element_located(press_hold))

time.sleep(10)


# Switching to the captcha frame and performing press and hold action
frame_element = driver.find_element("xpath", "//*[@id='px-captcha']//iframe[3]")

driver.switch_to(frame_element)
time.sleep(3)
press_and_hold = driver.find_element("xpath", "//p[text()='Press & Hold']" )
actions.click_and_hold(press_and_hold).perform()
time.sleep(5)
actions.release().perform()

# Waiting for the cart element to be visible
cart_element = ("xpath", "//a[@href='/viewcart?exploreMode=true&preference=FLIPKART']" )
WebDriverWait(driver, 5).until(EC.visibility_of_element_located(cart_element))

# Extracting information about items in the cart
card_items = driver.find_elements("xpath", "//div[@style='box-shadow: rgba(0, 0, 0, 0.2) 0px 1px 2px 0px;']" )
for card_item in card_items:
    image = card_item.find_element("xpath", "//span//div//img").get_attribute("src")
    print(image)
    link = card_item.get_attribute("href")
    print(link)
    name = card_item.find_element("xpath", "//div[4]]").text()
    print(name)
    

time.sleep(3)
# Closing the browser window
driver.close()