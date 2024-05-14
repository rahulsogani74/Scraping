from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome()
import time
from selenium.webdriver.support.select import Select


#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Opens the specified URL in the Chrome browser
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# Clicking on a checkbox by ID
driver.find_element(By.ID, "checkBoxOption1").click()

# Clicking on a checkbox by name
driver.find_element(By.NAME, "checkBoxOption2").click()

# Clicking on a link by link text
driver.find_element(By.LINK_TEXT, "Free Access to InterviewQues/ResumeAssistance/Material").click()

# Clicking on a link by partial link text
driver.find_element(By.PARTIAL_LINK_TEXT, "InterviewQues/ResumeAssistance/Material").click()

driver.find_element(By.CLASS_NAME, "radioButton").click()

# Clicking on a radio button by CSS selector
driver.find_element(By.CSS_SELECTOR, "[value='radio2']").click()

# Clicking on a radio button by XPath
driver.find_element(By.XPATH, "//input[@value='radio2']").click()

# Sending keys to an input field, clearing it first
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("RAj")
driver.find_element(By.XPATH, "//input[@id='name']").clear()
driver.find_element(By.XPATH, "//input[@id='name']").send_keys("oeee")

# Finding and printing the text of an element by XPath
text = driver.find_element(By.XPATH, "//legend[text()='Switch To Alert Example']").text
print(text)


driver.find_elements(By.XPATH, "//input[@type='checkbox']").click()

# Clicking multiple checkboxes
check_boxes = driver.find_elements(By.XPATH, "//input[starts-with(@name,'checkBoxOption')]")
print(check_boxes)
print(len(check_boxes))
for check_box in check_boxes:
    check_box.click()


# Clicking only the first two checkboxes
check_boxes = driver.find_elements(By.XPATH, "//input[starts-with(@name,'checkBoxOption')]")
print(check_boxes)
print(len(check_boxes))
for check_box in check_boxes:
    if check_boxes.index(check_box)+1 < 3:
        check_box.click()


check_boxes = driver.find_elements(By.XPATH, "(//input[starts-with(@name,'checkBoxOption')])[position()<3]")
print(len(check_boxes))
for check_box in check_boxes:
    check_box.click()


# Selecting options from a dropdown by index, visible text, and value
static_dropdown = driver.find_element(By.ID, "dropdown-class-example")
select = Select(static_dropdown)
select.select_by_index(2)
time.sleep(3)
select.select_by_visible_text("Option3")
time.sleep(3)
select.select_by_value("option1")

# Clicking an option in a dropdown directly by XPath
static_dropdown2 = driver.find_element(By.XPATH, "//option[@value='option2']")
static_dropdown2.click()

# Finding and printing the URL of a blinking link by class name
blinking_link = driver.find_element(By.CLASS_NAME, "blinkingText")
print(blinking_link.get_attribute("href"))


# Switching between windows
print(driver.window_handles)
print("********")
driver.find_element(By.ID, "openwindow").click()
time.sleep(2)
print(driver.window_handles)
print("********")
driver.find_element(By.ID, "opentab").click()
time.sleep(2)
print(driver.window_handles)

# Switching to a new tab and clicking on a link
driver.switch_to.window(driver.window_handles[1])
driver.find_element("xpath", "//div[@id]//a[contains(@href,'/blog')]").click()

# Switching to a frame and clicking on a link
frame_element = driver.find_element("xpath", "//iframe[@id='courses-iframe']")
driver.switch_to.frame(frame_element)
time.sleep(3)
driver.find_element("xpath", "//a[@href='consulting']").click()

# Switching back to the default content
driver.switch_to.default_content()

# Entering text into an input field
driver.find_element("xpath", "//input[@id='name']").send_keys("raja aaja")
time.sleep(3)

driver.close()