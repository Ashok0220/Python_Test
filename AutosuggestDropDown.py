import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(2)

#List of webElement
countrys = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

#len() ==> length
print(len(countrys))

for count in countrys:
    if count.text == "India":
        count.click()
        break

time.sleep(2)

# Get Attribute of values to dynamic text oon the browser and verify

assert driver.find_element(By.ID, "autosuggest").get_attribute("value") == "India"