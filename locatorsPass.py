import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client/")
driver.maximize_window()
driver.find_element(By.LINK_TEXT, "Forgot password?").click()


time.sleep(3)