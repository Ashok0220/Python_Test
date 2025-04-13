import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# driver = webdriver.Firefox()
# driver = webdriver.Edge()

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()

driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("at")
time.sleep(2)

Products = driver.find_elements(By.XPATH, "//div[@class='products']/div")

for product in Products:
    product.find_element(By.XPATH, "div/button").click()
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()

#tr td:nth-child(5) p  ==> CSS Selector
amounts = driver.find_elements(By.XPATH, "//tr/td[5]/p")

Sum = 0
for amount in amounts:
    Sum = Sum + int(amount.text)

print(Sum)

textamt = int (driver.find_element(By.XPATH, "//span[@class='totAmt']").text)

assert Sum == textamt

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
print(driver.find_element(By.CLASS_NAME, "promoInfo").text)

