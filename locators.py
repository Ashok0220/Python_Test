import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Ashok Babu")
driver.find_element(By.NAME, "email").send_keys("Ashok@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("password")
driver.find_element(By.ID, "exampleCheck1").click()


#Static DropDown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(0)
dropdown.select_by_visible_text("Female")


#Using CSS_Selector
driver.find_element(By.CSS_SELECTOR, "#inlineRadio2").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
text = driver.find_element(By.CLASS_NAME, "alert-success").text
print(text)

assert "Success" in text

time.sleep(2)