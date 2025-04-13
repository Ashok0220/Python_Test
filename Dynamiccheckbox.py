import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()

checkboxs = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for check in checkboxs:
    if check.get_attribute("value") == "option2":
        check.click()
        assert check.is_selected()
        break

time.sleep(2)

# Radio Button

radiobuttons = driver.find_elements(By.CSS_SELECTOR, ".radioButton")
radiobuttons[2].click()
assert radiobuttons[2].is_selected()

# Verify Displayed or not

assert driver.find_element(By.ID, "displayed-text").is_displayed()

driver.find_element(By.ID, "hide-textbox").click()

assert  not driver.find_element(By.ID, "displayed-text").is_displayed()

time.sleep(2)

