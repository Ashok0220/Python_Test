import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, "a[href*='/angularpractice/shop']").click()

products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for i in products:
    mobiles = i.find_element(By.XPATH, "div/h4/a").text
    if mobiles == "Blackberry":
        i.find_element(By.XPATH, "div/button").click()


driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))

driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()

driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
ordermessage = driver.find_element(By.CLASS_NAME, "alert-success").text

print(ordermessage)

assert "Success! Thank you!" in ordermessage

