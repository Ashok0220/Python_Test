import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.maximize_window()
driver.implicitly_wait(2)

driver.find_element(By.LINK_TEXT, "Click Here").click()

parentwindow = driver.window_handles
driver.switch_to.window(parentwindow[1])

textchild = driver.find_element(By.XPATH, "//h3").text

driver.switch_to.window(parentwindow[0])
assert "Opening a new window" ==driver.find_element(By.XPATH, "//h3").text
print(textchild)

driver.implicitly_wait(2)