from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.implicitly_wait(2)
driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()

browserveglist = []

veglists = driver.find_elements(By.XPATH, "//tr/td[1]")


for veg in veglists:
    browserveglist.append(veg.text)

print(browserveglist)

originalsortlist = browserveglist.copy()

print(originalsortlist)

assert browserveglist == originalsortlist

