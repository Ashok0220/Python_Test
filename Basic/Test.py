import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://letcode.in/table")
driver.maximize_window()
body = driver.find_element(By.ID, "simpletable")
headers = body.find_elements(By.TAG_NAME, "th")
print(len(headers))

for i in headers:
    print(i.text)


allrows = body.find_elements(By.CSS_SELECTOR, "tbody tr")
print(len(allrows))

for i in allrows:
    colums = i.find_elements(By.TAG_NAME, "td")
    print(colums[0].text)

time.sleep(1)

